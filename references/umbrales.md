---
name: umbrales
description: Números medibles del slop de IA — frecuencias, umbrales por cada 1.000 palabras, léxico por generación de modelo y fuentes primarias. Consultar antes de afirmar que un texto es generado.
---

# Umbrales medibles

Trata esto como chequeo de **densidad**, no como prueba de autoría.

## El estudio base

El rastreo de Pew de agosto de 2026 encontró señales de autoría por IA en ~10% de las páginas en inglés de una muestra de julio de 2026, y en más de un tercio de las publicadas después del lanzamiento de ChatGPT. Contra 2023:

| Señal | Cambio |
|---|---|
| Rayas largas (em dash) | ~2× |
| Coma de Oxford | +63% |
| Vocabulario favorito de IA | >2× |
| "it's not just X, it's Y" | ~3× |

Kobak et al., sobre millones de resúmenes de PubMed, encontró picos post-ChatGPT en palabras de estilo, no en términos científicos: *delves* subió del orden de 25–28×; *underscores* y *showcasing* entre 9× y 14×.

Reinhart et al. (PNAS): GPT-4o usa cláusulas de participio presente a ~5,3× la tasa humana. La escritura académica mostró una caída >10% en *is/are* después de ChatGPT.

## Umbrales operativos

| Patrón | Umbral | Fuerza |
|---|---|---|
| Señales totales | 2 en ~500 palabras = amarillo; 3–4 = huella | alta en conjunto |
| Rayas largas | prosa humana ~3,7–10 por 1.000 palabras; los detectores se activan sobre ~20/1.000. GPT-4.1 ~10,6; Claude Opus 4.6 ~9,1; Llama a menudo ~0 | débil sola |
| Trípticos ("rápido, escalable y seguro") | más de uno pulido por ~200 palabras | media |
| *utilizar / facilitar / apalancar / demostrar* donde cabe *usar / ayudar / mostrar* | más de uno por ~300 palabras ganándole al verbo llano | media |
| Longitud de párrafo | ChatGPT se agrupa en 3–5 oraciones; varianza baja (burstiness < ~0,4) | media |
| Apertura con conector (*Además / Asimismo / Por otro lado*) | más de la mitad de los párrafos | alta |
| Autoridad sin citar ("los estudios demuestran") | sobre ~50% de las afirmaciones de autoridad | alta |
| Prueba de borrado | si >1/3 de las oraciones se pueden borrar sin pérdida, es relleno; si >1/2 de los párrafos no pasan "nombra un hecho concreto", está vacío | la más alta |
| Residuo de chat ("¡Excelente pregunta!", "¡Espero que te sirva!") | cualquier aparición | la más alta: no tiene otra explicación |

## Léxico por generación de modelo

Más útil que una lista negra congelada: el vocabulario rota por año de modelo.

| Época | Sobreusado (EN) | Equivalente/eco en ES | Evasión típica |
|---|---|---|---|
| 2023–mediados 2024 (GPT-4) | delve, tapestry, testament, intricate, landscape, pivotal, underscore, boasts, garner, vibrant | profundizar, tapiz, testimonio, intrincado, panorama, crucial, subrayar, ostenta, cosechar, vibrante | "sirve como", "se erige como" en vez de "es" |
| Mediados 2024–mediados 2025 (GPT-4o) | align with, fostering, showcasing, highlighting, enhance, enduring | alinearse con, fomentar, mostrar, destacar, potenciar, perdurable | "cuenta con / ofrece" en vez de "tiene" |
| Mediados 2025 en adelante | emphasizing, enhance, highlighting, showcasing | enfatizando, potenciar, resaltando, exhibiendo | lenguaje enlatado de "cobertura mediática / notabilidad" |
| Estilo Grok | causal, empirical, correlate, underscore | causal, empírico, correlacionar, subrayar | relleno seudocientífico |
| Claude Opus 4.6–5 (2026) | rather than merely (160×), matters because (132×), every single (112×), less like a X and more like (105×), single most, load-bearing | en lugar de simplemente, esto importa porque, todos y cada uno, menos como un X y más como, lo más X de todo, sostiene la carga | metáfora física en vez de verbo literal ("el riesgo vive en") |

Conjunto "típico de IA" de Pew: *delve, interplay, testament, additionally, align with, boasts, bolstered, crucial, emphasizing, enduring, enhance, essential, fostering, garner, highlight, intricate, key, landscape, meticulous, perfectly, pivotal, showcase, significant, tapestry, underscore, valuable, vibrant*.

Capa de marketing/B2B que los lectores ya asocian con slop: *unlock, unleash, elevate, harness, supercharge, game changer, cutting-edge, seamless, robust, paradigm shift, let's dive in, in today's fast-paced world, picture this, here's the kicker*. En español: *desbloquea, potencia tu, lleva tu X al siguiente nivel, revolucionario, de vanguardia, sin fricción, robusto, cambio de paradigma, en el mundo acelerado de hoy, imagina esto*.

## Borrar en cuanto se vean

Casi nunca aportan información:

`vale la pena señalar` · `es importante destacar` · `cabe mencionar` · `se podría argumentar` · `en conclusión` · `en definitiva` · `en última instancia` · `de cara al futuro` · `solo el tiempo lo dirá` · `los estudios demuestran` · `los expertos coinciden` · `la investigación sugiere`

## Fuentes primarias

- Pew Research, estudio web 2026: https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/
- Wikipedia, *Signs of AI writing*: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- ContentBeta, lista de 300+ palabras/patrones: https://www.contentbeta.com/blog/list-of-words-overused-by-ai/
- Slopdetector, 12 umbrales medibles: https://slopdetector.org/blog/signs-of-ai-writing
- Graphite, frases sobreusadas por modelo (tasas de Claude): https://graphite.io/five-percent/research/ai-tells
- Rewritica: https://www.rewritica.com/blog/signs-of-ai-writing
- GPTOne: https://gptone.me/blog/how-to-tell-if-something-was-written-by-chatgpt-9-signs

La guía de Wikipedia es el catálogo público más completo, pero es **descriptiva**, no una prohibición de estilo.
