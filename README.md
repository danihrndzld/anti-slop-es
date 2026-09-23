# anti-slop-es

Skill de Claude Code, en español, para detectar y quitar **slop de IA** en texto, código y diseño.

Mide **densidad**, no palabras sueltas. Una raya larga o un tríptico aislados son español normal. Varios juntos en un pasaje corto y sin un solo dato concreto son el perfil de slop.

Junta tres fuentes:

- el toolkit `anti-slop` (patrones de texto, código y diseño),
- el flujo `ai-slop-cleaner` de oh-my-claudecode (limpieza de código sin cambiar comportamiento, con modo revisor),
- los umbrales medibles de Pew 2026, Wikipedia *Signs of AI writing*, Slopdetector y Kobak et al.

## Instalar

### Con npx (sin clonar nada)

```bash
npx github:danihrndzld/anti-slop-es            # global: ~/.claude/skills/
npx github:danihrndzld/anti-slop-es --proyecto # solo este repo: ./.claude/skills/
npx github:danihrndzld/anti-slop-es --dir ruta # destino a mano
npx github:danihrndzld/anti-slop-es --desinstalar
```

Aún no está publicada en npm; el spec `github:` es la vía soportada hoy. Al publicarla, `npx anti-slop-es` hará lo mismo.

### Con Claude Code (pega este prompt)

```
Instala la skill anti-slop-es desde https://github.com/danihrndzld/anti-slop-es

1. Corre: npx github:danihrndzld/anti-slop-es
2. Verifica que exista ~/.claude/skills/anti-slop-es/SKILL.md
3. Corre los autotests:
   python3 ~/.claude/skills/anti-slop-es/scripts/detectar_slop.py --autotest
   python3 ~/.claude/skills/anti-slop-es/scripts/limpiar_slop.py --autotest
4. Resume en dos líneas qué hace la skill y con qué frases se dispara.
```

### A mano

```bash
git clone https://github.com/danihrndzld/anti-slop-es
cp -r anti-slop-es ~/.claude/skills/anti-slop-es
```

Reinicia Claude Code después de instalar.

## Usar

Desde Claude Code, con cualquiera de estas:

> revisa este texto con anti-slop-es
> deslop este módulo: demasiados wrappers y código muerto
> ¿esto suena a ChatGPT?
> limpia el slop de README.md

Desde la terminal:

```bash
python3 scripts/detectar_slop.py documento.md --verbose
python3 scripts/limpiar_slop.py documento.md            # previsualiza
python3 scripts/limpiar_slop.py documento.md --guardar  # aplica, deja .backup
```

## Cómo lee los números

El detector cuenta señales ponderadas por cada 1.000 palabras:

| Densidad | Lectura |
|---|---|
| 0–8 | prosa normal |
| 8–18 | revisar a mano los tramos marcados |
| 18–35 | perfil de slop: reescribir secciones |
| 35+ | plantilla de modelo: reescribir de cero |

Los dos párrafos del autotest: uno que mide la deriva de un PCA9685 con osciloscopio (62.3 Hz contra 60 nominales) da **0.0**. Uno de relleno corporativo, con metacomentario, citas sin fuente y un cierre que no toma partido, da **524.6**.

Pesos: residuo de chat vale 4. Citas fantasma, paralelismo negativo, metacomentario y cierre vacío valen 3, porque casi nunca tienen otra explicación. Inflación latinizante vale 1 y léxico de época vale 2; solo pesan cuando se acumulan.

El detector falla más con autores no nativos, y el vocabulario delator cambia con cada generación de modelo. Sirve para encontrar tramos a revisar. No sirve para decidir quién escribió algo.

## Qué hay dentro

```
SKILL.md                        flujo completo: texto, código, diseño, modo revisor
references/umbrales.md          números, léxico por época de modelo, fuentes
references/patrones-texto.md    léxico, sintaxis, formato y sustancia (ES/EN)
references/patrones-codigo.md   nombres, comentarios, abstracción, fronteras
references/patrones-diseno.md   visual, layout, componentes, microcopy
scripts/detectar_slop.py        detector por densidad (--autotest incluido)
scripts/limpiar_slop.py         limpieza mecánica reversible (--autotest incluido)
bin/instalar.mjs                instalador npx, sin dependencias
```

## Pruebas

```bash
npm test
```

Corre los autotests de los dos scripts. El detector exige que el párrafo del PCA9685 quede bajo 8 y el de relleno sobre 35, con citas fantasma, paralelismo negativo y metacomentario detectados. Son dos casos fijos: no miden la tasa de falsos positivos en texto real.

## Lo que el script no mide

Después de cada párrafo, pregúntate si puedes repetir un hecho concreto. Si no puedes, el párrafo sobra, lo haya escrito una persona o un modelo.

Se arregla **sumando** nombres, fechas, números, un fracaso propio o una herramienta con nombre. Cambiar sinónimos solo aplana la voz.

## Fuentes

- [Pew Research, estudio web 2026](https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/)
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [ContentBeta: 300+ palabras sobreusadas por IA](https://www.contentbeta.com/blog/list-of-words-overused-by-ai/)
- [Slopdetector: 12 umbrales medibles](https://slopdetector.org/blog/signs-of-ai-writing)

MIT.
