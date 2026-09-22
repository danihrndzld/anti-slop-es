# anti-slop-es

Skill de Claude Code, en español, para detectar y quitar **slop de IA** en texto, código y diseño.

No es una lista de palabras prohibidas. Es un chequeo de **densidad**: una "raya larga", un "profundizar" o un tríptico son español normal — varios apilados en un pasaje corto, sin un solo dato concreto, es el perfil de slop.

Fusiona tres fuentes:

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

Publicada en npm, el comando corto también sirve: `npx anti-slop-es`.

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

Ejemplo real de los autotests: un párrafo con mediciones concretas da **0.0**; un párrafo de relleno corporativo da **524**.

Categorías con más peso (las que casi no tienen otra explicación): residuo de chat, citas fantasma, paralelismo negativo, metacomentario, cierre vacío. Las de menos peso (léxico de época, inflación latinizante) solo cuentan acumuladas.

Los detectores son ruidosos, sobre todo con no nativos, y el vocabulario rota por generación de modelo. Usa el número para encontrar candidatos, nunca como veredicto de autoría.

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

Corre los autotests de ambos scripts: verifica que el texto con datos concretos no se marque y que el texto de plantilla sí, sin falsos positivos.

## La prueba que ningún script hace

Después de cada párrafo: ¿puedes repetir un hecho concreto? Si no, sobra — lo haya escrito una persona o un modelo.

Se arregla **sumando**: nombres, fechas, números, un fracaso propio, una herramienta nombrada. Cambiar sinónimos solo aplana la voz.

## Fuentes

- [Pew Research, estudio web 2026](https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/)
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [ContentBeta: 300+ palabras sobreusadas por IA](https://www.contentbeta.com/blog/list-of-words-overused-by-ai/)
- [Slopdetector: 12 umbrales medibles](https://slopdetector.org/blog/signs-of-ai-writing)

MIT.
