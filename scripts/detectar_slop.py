#!/usr/bin/env python3
"""Detector de slop de IA por densidad (ES/EN).

No emite veredictos de autoría: cuenta señales medibles por cada 1.000 palabras
y marca dónde están. Umbrales en references/umbrales.md.

Uso:
    python3 detectar_slop.py <archivo> [--verbose]
    python3 detectar_slop.py --autotest
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

# (nombre, peso, patrones). El peso refleja qué tan fiable es la señal.
CATEGORIAS = [
    ("residuo-chat", 4, [
        r"¡?(excelente|gran|buena) pregunta!?", r"¡?claro!?,? (aquí|te)",
        r"con (mucho )?gusto te", r"espero que (te sirva|esto ayude)",
        r"¿(qué opinas|te gustaría que)", r"great question", r"certainly[,!]",
        r"i'?d be happy to", r"i hope this helps", r"as an ai",
        r"utm_source=chatgpt", r"turn\d+search\d+",
    ]),
    ("cita-fantasma", 3, [
        r"los? estudios? (demuestran|muestran|sugieren)", r"los expertos coinciden",
        r"la investigación sugiere", r"los datos prueban", r"está demostrado que",
        r"studies show", r"experts agree", r"research suggests", r"data proves",
    ]),
    ("paralelismo-negativo", 3, [
        r"no (se trata|es) (solo |sólo |únicamente )?(de |sobre )?\w[^.;]{0,60}\b(sino|es)\b",
        r"no solo \w[^.;]{0,60}\bsino\b", r"más que \w[^.;]{0,40}, es ",
        r"it'?s not (just |about )?\w[^.;]{0,60}it'?s ",
        r"not just \w[^.;]{0,50}\bbut\b",
    ]),
    ("metacomentario", 3, [
        r"en este (artículo|post|documento|apartado|capítulo)",
        r"(como|mientras) (veremos|exploraremos|analizaremos)",
        r"echemos un vistazo", r"antes de (continuar|empezar|profundizar)",
        r"ahora que (hemos|ya) (cubierto|visto)", r"vale la pena (señalar|mencionar)",
        r"(es|resulta) importante (destacar|señalar|notar|mencionar)",
        r"cabe (mencionar|destacar|señalar)", r"in this (article|post|document|section)",
        r"let'?s take a (closer )?look", r"it'?s (important|worth) (to )?not(e|ing)",
    ]),
    ("lexico-epoca", 2, [
        r"\bprofundi(zar|cemos)\b", r"\btapiz\b", r"\btestimonio de\b", r"\bintrincad",
        r"\bpanorama (actual|digital|cambiante)", r"\bcrucial\b", r"\bsubray(a|ar|ando)",
        r"\bostenta\b", r"\bvibrante\b", r"\bfomentar\b", r"\bperdurable\b",
        r"\bse erige como\b", r"\bsirve como\b", r"\brepresenta un (momento|hito)",
        r"\bdelv(e|ing)\b", r"\btapestry\b", r"\bpivotal\b", r"\bunderscor(e|ing|es)\b",
        r"\bshowcas(e|ing)\b", r"\bfostering\b", r"\bintricate\b", r"\bgarner\b",
    ]),
    ("marketing", 2, [
        r"\brevolucionari", r"de vanguardia", r"clase mundial", r"cambio de paradigma",
        r"al siguiente nivel", r"desbloquea(r)? (el|tu)", r"empoderar?",
        r"impulsar la innovación", r"en el mundo (acelerado|actual)",
        r"sin fricción", r"game.?changer", r"cutting.?edge", r"seamless",
        r"unlock (your|the)", r"in today'?s fast.?paced world",
    ]),
    ("relleno", 2, [
        r"con el fin de\b", r"con el objetivo de\b", r"debido al hecho de que",
        r"a pesar del hecho de que", r"en este momento del tiempo",
        r"tiene la capacidad de", r"es capaz de\b", r"tomar en consideración",
        r"llevar a cabo una", r"in order to\b", r"due to the fact that",
        r"has the ability to", r"at this point in time",
    ]),
    ("matizacion", 2, [
        r"podría (potencialmente|posiblemente)", r"se podría argumentar",
        r"hasta cierto punto", r"en términos generales", r"en cierta medida",
        r"parecería que", r"could potentially", r"might possibly",
        r"one could argue", r"to a certain extent",
    ]),
    ("cierre-vacio", 3, [
        r"en conclusión", r"en (última instancia|definitiva)",
        r"de cara al futuro", r"solo el tiempo lo dirá",
        r"ambos tienen sus (fortalezas|ventajas)",
        r"la (decisión|elección) es tuya", r"a pesar de sus \w+, \w+ enfrenta",
        r"in conclusion", r"only time will tell", r"the choice is yours",
    ]),
    ("inflacion-latinizante", 1, [
        r"\butiliza(r|mos|n|ndo)?\b", r"\bfacilita(r|mos|n)?\b", r"\bapalanca(r)?\b",
        r"\bleverag(e|ing)\b", r"\butiliz(e|ing|es)\b",
    ]),
    ("cola-gerundio", 2, [
        r",\s*(destacando|subrayando|reflejando|resaltando|enfatizando|mostrando|marcando)\b",
        r",\s*(highlighting|underscoring|showcasing|reflecting|emphasizing)\b",
    ]),
]

CONECTORES_INICIO = re.compile(
    r"^\s*(#+\s*)?(además|asimismo|por (otro lado|ende|lo tanto)|sin embargo|"
    r"no obstante|en consecuencia|adicionalmente|furthermore|moreover|additionally|"
    r"however|therefore)\b", re.I)

TRIPLETE = re.compile(r"\b\w+, \w+(?: \w+)? y \w+\b|\b\w+, \w+,? and \w+\b", re.I)
EM_DASH = re.compile(r"—|--")
TITLE_CASE = re.compile(r"^#{1,6} (?:[A-Z][a-z]+ ){2,}[A-Z][a-z]+\s*$")
GERUNDIO_INICIO = re.compile(r"^\s*\w+(ando|iendo|ing)\b", re.I)


def analizar(texto):
    lineas = texto.splitlines()
    palabras = len(re.findall(r"\b[\wáéíóúñü']+\b", texto, re.I))
    hallazgos = defaultdict(list)
    peso_total = 0

    for nombre, peso, patrones in CATEGORIAS:
        for patron in patrones:
            rx = re.compile(patron, re.I)
            for n, linea in enumerate(lineas, 1):
                for m in rx.finditer(linea):
                    hallazgos[nombre].append((n, m.group(0).strip()))
                    peso_total += peso

    # Señales estructurales
    parrafos = [p for p in re.split(r"\n\s*\n", texto) if p.strip()]
    conectores = sum(1 for p in parrafos if CONECTORES_INICIO.match(p))
    if parrafos and conectores / len(parrafos) > 0.5:
        hallazgos["apilamiento-conectores"].append(
            (0, f"{conectores}/{len(parrafos)} párrafos abren con conector"))
        peso_total += 3

    em = len(EM_DASH.findall(texto))
    if palabras and em * 1000 / palabras > 20:
        hallazgos["rayas-largas"].append((0, f"{em} en {palabras} palabras"))
        peso_total += 2

    trip = len(TRIPLETE.findall(texto))
    if palabras and trip * 200 / palabras > 1:
        hallazgos["regla-de-tres"].append((0, f"{trip} trípticos en {palabras} palabras"))
        peso_total += 2

    for n, linea in enumerate(lineas, 1):
        if TITLE_CASE.match(linea):
            hallazgos["title-case"].append((n, linea.strip()))
            peso_total += 1
        if GERUNDIO_INICIO.match(linea) and len(linea.split()) > 6:
            hallazgos["apertura-gerundio"].append((n, linea.strip()[:60]))
            peso_total += 1

    oraciones = [s for s in re.split(r"[.!?]\s+", texto) if len(s.split()) > 3]
    if len(oraciones) > 10:
        largos = [len(s.split()) for s in oraciones]
        media = sum(largos) / len(largos)
        var = (sum((l - media) ** 2 for l in largos) / len(largos)) ** 0.5
        if media and var / media < 0.4:
            hallazgos["parrafos-uniformes"].append(
                (0, f"burstiness {var / media:.2f} (< 0.40)"))
            peso_total += 2

    densidad = peso_total * 1000 / palabras if palabras else 0
    return palabras, densidad, hallazgos


def banda(d):
    if d < 8:
        return "prosa normal"
    if d < 18:
        return "revisar a mano los tramos marcados"
    if d < 35:
        return "perfil de slop: reescribir secciones"
    return "plantilla de modelo: reescribir de cero"


def main():
    args = sys.argv[1:]
    if "--autotest" in args:
        return autotest()
    if not args:
        print(__doc__)
        return 1

    ruta = Path(args[0])
    if not ruta.is_file():
        print(f"No existe: {ruta}", file=sys.stderr)
        return 1

    palabras, densidad, hallazgos = analizar(ruta.read_text(encoding="utf-8", errors="replace"))
    print(f"\n{ruta}  —  {palabras} palabras")
    print(f"Densidad: {densidad:.1f} señales/1.000 palabras  →  {banda(densidad)}\n")

    if not hallazgos:
        print("Sin señales medibles.")
    for nombre, items in sorted(hallazgos.items(), key=lambda x: -len(x[1])):
        print(f"  {nombre}: {len(items)}")
        if "--verbose" in args:
            for n, frag in items[:8]:
                pos = f"L{n}" if n else "doc"
                print(f"      {pos}: {frag}")

    print("\nLa prueba que ningún script hace por ti: después de cada párrafo,")
    print("¿puedes repetir un hecho concreto? Si no, sobra.")
    return 0


def autotest():
    limpio = ("El PCA9685 corre 4% rápido a 25 grados. Medí 62.3 Hz con el "
              "osciloscopio contra los 60 nominales. Ajusté el prescaler a 120. "
              "Quedó en 60.1 Hz. El driver de Adafruit no documenta esa deriva.")
    sucio = ("En este artículo vamos a profundizar en el intrincado panorama de "
             "la innovación. Es importante destacar que los estudios demuestran "
             "que no se trata solo de tecnología, sino de personas. Además, la "
             "solución es rápida, escalable y segura. Asimismo, vale la pena "
             "señalar que podría potencialmente revolucionar el sector. En "
             "conclusión, ambos tienen sus fortalezas y solo el tiempo lo dirá.")

    _, d_limpio, h_limpio = analizar(limpio)
    _, d_sucio, h_sucio = analizar(sucio)

    assert d_limpio < 8, f"texto limpio marcado como slop: {d_limpio:.1f}"
    assert d_sucio > 35, f"texto sucio no detectado: {d_sucio:.1f}"
    assert "cita-fantasma" in h_sucio
    assert "paralelismo-negativo" in h_sucio
    assert "metacomentario" in h_sucio
    assert not h_limpio, f"falsos positivos: {dict(h_limpio)}"
    print(f"autotest ok — limpio {d_limpio:.1f} / sucio {d_sucio:.1f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
