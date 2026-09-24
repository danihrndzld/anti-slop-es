#!/usr/bin/env python3
"""Limpieza mecánica de slop (ES/EN).

Solo toca lo que se puede quitar sin pensar: relleno, metacomentario,
perífrasis, intensificadores vacíos. La sustancia (abstracciones sin dato,
citas fantasma, regresión a la media) se arregla a mano.

Uso:
    python3 limpiar_slop.py <archivo>              # previsualiza
    python3 limpiar_slop.py <archivo> --guardar    # aplica, deja .backup
    python3 limpiar_slop.py <archivo> --salida out.md
    python3 limpiar_slop.py --autotest
"""

import re
import sys
from pathlib import Path

# (patrón, reemplazo). Orden importa: lo largo antes que lo corto.
REGLAS = [
    # Metacomentario: borrar la frase inicial completa.
    (r"(?i)^\s*(es|resulta) importante (destacar|señalar|notar|mencionar) que\s*", ""),
    (r"(?i)\b(vale la pena|cabe) (señalar|mencionar|destacar) que\s*", ""),
    (r"(?i)^\s*en este (artículo|post|documento|apartado),?\s*", ""),
    (r"(?i)\bit'?s (important|worth) (to )?not(e|ing) that\s*", ""),
    (r"(?i)\bin order to\b", "to"),
    # Adulación y candor de Claude (references/patrones-claude.md)
    (r"(?i)^\s*¡?tienes (toda la )?razón[!.]\s*", ""),
    (r"(?i)^\s*¡(perfecto|excelente( idea)?)!\s*", ""),
    (r"(?i)^\s*(you'?re absolutely (right|correct)|perfect)[!.]\s*", ""),
    (r"(?i)\b(honestamente|para ser (honesto|franco|sincero)),\s*", ""),
    (r"(?i)\bgenuinamente\s+", ""),
    (r"(?i)\b(honestly|to be honest),\s*", ""),
    (r"(?i)\bgenuinely\s+", ""),
    # Perífrasis -> simple
    (r"(?i)\bcon el (fin|objetivo|propósito) de\b", "para"),
    (r"(?i)\bdebido al hecho de que\b", "porque"),
    (r"(?i)\ba pesar del hecho de que\b", "aunque"),
    (r"(?i)\ben este momento del tiempo\b", "ahora"),
    (r"(?i)\btiene la capacidad de\b", "puede"),
    (r"(?i)\bes capaz de\b", "puede"),
    (r"(?i)\btomar en consideración\b", "considerar"),
    (r"(?i)\bllevar a cabo una investigación\b", "investigar"),
    (r"(?i)\brealizar una implementación de\b", "implementar"),
    (r"(?i)\bdue to the fact that\b", "because"),
    (r"(?i)\bhas the ability to\b", "can"),
    (r"(?i)\bat this point in time\b", "now"),
    # Inflación latinizante
    (r"(?i)\butilizar\b", "usar"),
    (r"(?i)\butilizando\b", "usando"),
    (r"(?i)\butiliza\b", "usa"),
    (r"(?i)\bapalancar\b", "usar"),
    (r"(?i)\bleverage\b", "use"),
    # Matización apilada
    (r"(?i)\bpodría potencialmente\b", "podría"),
    (r"(?i)\bpodría posiblemente\b", "podría"),
    (r"(?i)\bcould potentially\b", "could"),
    (r"(?i)\bmight possibly\b", "might"),
    # Intensificadores y redundancias
    (r"(?i)\b(muy|realmente|sumamente) (único|esencial|crucial)\b", r"\2"),
    (r"(?i)\bcompletamente terminado\b", "terminado"),
    (r"(?i)\bresultado final\b", "resultado"),
    (r"(?i)\bhistoria pasada\b", "historia"),
    # Cierres vacíos
    (r"(?i)^\s*en conclusión,?\s*", ""),
    (r"(?i)^\s*en (última instancia|definitiva),?\s*", ""),
    (r"(?i)^\s*in conclusion,?\s*", ""),
]

# Agresivo: cambia el ritmo, puede tocar la voz.
AGRESIVAS = [
    (r"(?i)^\s*(además|asimismo|adicionalmente|furthermore|moreover),?\s*", ""),
    (r"(?i)\ben términos generales,?\s*", ""),
    (r"(?i)\bhasta cierto punto,?\s*", ""),
    (r"\s+—\s+", ". "),
]


def limpiar(texto, agresivo=False):
    reglas = REGLAS + (AGRESIVAS if agresivo else [])
    cambios = []
    salida = []
    for n, linea in enumerate(texto.splitlines(), 1):
        original = linea
        for patron, repl in reglas:
            linea = re.sub(patron, repl, linea)
        if linea != original:
            # Recapitaliza si borramos el arranque de la oración.
            linea = re.sub(r"^(\s*)([a-záéíóúñ])",
                           lambda m: m.group(1) + m.group(2).upper(), linea)
            cambios.append((n, original.strip(), linea.strip()))
        salida.append(linea)
    return "\n".join(salida) + ("\n" if texto.endswith("\n") else ""), cambios


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

    texto = ruta.read_text(encoding="utf-8")
    nuevo, cambios = limpiar(texto, "--agresivo" in args)

    if not cambios:
        print("Nada mecánico que quitar. Lo que quede es sustancia: revísalo a mano.")
        return 0

    print(f"{len(cambios)} línea(s) con cambios:\n")
    for n, antes, despues in cambios:
        print(f"  L{n}")
        print(f"    - {antes}")
        print(f"    + {despues}")

    if "--salida" in args:
        destino = Path(args[args.index("--salida") + 1])
        destino.write_text(nuevo, encoding="utf-8")
        print(f"\nEscrito en {destino}")
    elif "--guardar" in args:
        ruta.with_suffix(ruta.suffix + ".backup").write_text(texto, encoding="utf-8")
        ruta.write_text(nuevo, encoding="utf-8")
        print(f"\nAplicado. Respaldo en {ruta.name}.backup")
    else:
        print("\n(previsualización — usa --guardar para aplicar)")
    return 0


def autotest():
    antes = ("Es importante destacar que el servicio utiliza caché.\n"
             "Con el objetivo de reducir latencia, podría potencialmente fallar.\n"
             "El resultado final fue 42 ms.\n")
    despues, cambios = limpiar(antes)
    assert "Es importante destacar" not in despues, despues
    assert "usa caché" in despues, despues
    assert "Para reducir latencia" in despues, despues
    assert "podría fallar" in despues, despues
    assert "El resultado fue 42 ms" in despues, despues
    assert len(cambios) == 3, cambios
    claude, _ = limpiar("¡Tienes toda la razón! Honestamente, el índice empieza en 0.\n")
    assert claude == "El índice empieza en 0.\n", claude
    # No debe tocar texto ya limpio.
    limpio = "Medí 62.3 Hz con el osciloscopio. El prescaler quedó en 120.\n"
    salida, sin_cambios = limpiar(limpio)
    assert salida == limpio and not sin_cambios, sin_cambios
    print("autotest ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
