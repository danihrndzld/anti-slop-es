---
name: patrones-texto
description: Catálogo de patrones de slop en lenguaje natural (ES/EN) — léxico, sintaxis, formato y sustancia, con la corrección concreta de cada uno.
---

# Patrones de texto

Ordenados de menos a más fiables. La sintaxis sobrevive a un cambio de sinónimos; la sustancia es el problema real.

## 1. Léxico (el más débil)

### Perífrasis con alternativa simple

| Inflado | Simple |
|---|---|
| con el fin de / con el objetivo de | para |
| debido al hecho de que | porque |
| en este momento del tiempo | ahora |
| tiene la capacidad de / es capaz de | puede |
| a pesar del hecho de que | aunque |
| tomar en consideración | considerar |
| llevar a cabo una investigación | investigar |
| realizar una implementación | implementar |
| in order to | to |
| due to the fact that | because |
| has the ability to | can |

### Inflación latinizante

*utilizar → usar* · *facilitar → ayudar* · *apalancar/leverage → usar* · *comenzar → empezar* · *demostrar → mostrar* · *implementar → hacer* (cuando aplica).

Uno no es nada. Más de uno por ~300 palabras, ganándole al verbo llano, es inflación.

### Calificadores redundantes y intensificadores vacíos

*completamente terminado* · *absolutamente esencial* · *totalmente único* · *muy único* · *historia pasada* · *planes futuros* · *resultado final*.

Sobreuso de *muy*, *realmente*, *increíblemente*, *sumamente*.

### Jerga corporativa

*sinérgico* · *enfoque holístico* · *cambio de paradigma* · *revolucionario* · *de vanguardia* · *de clase mundial* · *impulsar la innovación* · *desbloquear el potencial* · *empoderar usuarios* · *maximizar el valor*.

## 2. Sintaxis y retórica (fiable)

**Paralelismo negativo.** "No se trata de X, se trata de Y." "No solo X, sino Y." "Eso no es marketing. Es ruido." Pew: casi se triplicó en la web. Una corrección de un error real está bien; tres en un artículo es plantilla.

**Regla de tres.** "Rápido, escalable y seguro." El modelo default es el tríptico aunque el mundo tenga dos o siete elementos. Umbral: más de uno pulido por ~200 palabras.

**Rango falso.** "Desde principiantes hasta expertos", "de la creación de contenido al análisis de datos", "carnes desde res hasta pollo". Suena exhaustivo, no nombra ningún rango real.

**Colas de gerundio.** Oraciones que terminan ", destacando…", ", subrayando…", ", reflejando un cambio más amplio…". Wikipedia lo llama análisis superficial atornillado a un hecho. GPT-4o: ~5,3× la tasa humana.

**Evasión de la cópula.** "Sirve como eje", "se erige como testimonio", "representa un momento clave" en vez de "es".

**Aperturas con gerundio.** "Ofreciendo una amplia gama de herramientas, la app…" — 2–5× la tasa humana.

**Remates staccato.** "Sin historia. Sin chispa. Sin alma." / "Nada de X. Nada de Y. Solo Z." / "¿El resultado?"

**Pilas de matización y franqueza falsa.** "Podría potencialmente argumentarse que…" y los tics de 2026: "¿Honestamente?" sin nada honesto, "Aquí está lo mejor" sin nada mejor, "silenciosamente potente".

**Metacomentario.** "En este artículo veremos…" · "Como exploraremos…" · "Echemos un vistazo más de cerca" · "Ahora que cubrimos…" · "Antes de continuar…". Dilo y ya; sáltate las acotaciones escénicas.

## 3. Formato

| Patrón | Cómo se ve | Nota |
|---|---|---|
| Rayas largas | Unir cláusulas donde bastaba una coma o un punto | Humano ~3,7–10/1.000 palabras; alarma sobre ~20/1.000 |
| Párrafos uniformes | Oración tema + 3 ejemplos + cierre que repite | ChatGPT se agrupa en 3–5 oraciones |
| Un encabezado por párrafo | Esqueleto de presentación | Fusiona secciones; deja que alguna corra larga |
| Muros de viñetas / negrita inicial | Toda respuesta se vuelve lista | Sesgo del modelo de recompensa |
| Títulos En Mayúscula Inicial | Todo H2 capitalizado como título de libro | Delator de Wikipedia/bibliotecas |
| Apilamiento de conectores | *Además / Asimismo / Por otro lado* abriendo casi todo párrafo | Marca si supera la mitad de los párrafos |
| Residuo de chat | "¡Excelente pregunta!", "¡Claro!", "Con gusto", "¡Espero que te sirva!", "¿Qué opinas?" | El delator más fuerte |
| Sangrado de Markdown | `**negrita**`, `# encabezados`, `turn0search0`, ✨ | Falla al pegar |
| Cierre de "desafíos" | "A pesar de sus [virtudes], X enfrenta desafíos…" + futuro optimista vago | Fórmula de Wikipedia, no la simple mención de problemas |
| Cierre conciliador | Elogia A, elogia B, "ambos tienen sus fortalezas" | Nunca toma partido |

Los tics propios de Claude (adulación al corregirse, narración en modo agente, binario contrastivo, aforismo final, "sostiene la carga") están en `patrones-claude.md`.

Aperturas aduladoras y cierres de falso equilibrio son artefactos de RLHF: "Planteas un punto muy interesante", luego "en última instancia, la decisión es tuya". Responde la pregunta; no anuncies que era interesante.

## 4. Sustancia (lo que de verdad importa)

**Regresión a la media.** El modelo cambia lo raro y específico por elogio genérico. "Inventor del primer enganche automático de vagones" se vuelve "un titán revolucionario de la industria". El sujeto sube de volumen y pierde foco.

**Trampa de abstracción.** Humano: "La cafetería olía a espresso quemado y libros viejos." Modelo: "El lugar tenía una mezcla única de aromas."

**Prueba de la cinta (borrado).** Una sección de 500 palabras con ~100 de información nueva y 400 de repetición. Si más de un tercio de las oraciones se borran sin pérdida, es relleno.

**Citas fantasma.** "Los estudios demuestran", "los expertos coinciden", "los datos prueban", sin nombre, año ni enlace. Wikipedia también marca DOIs inventados, ISBN falsos y URLs con `utm_source=chatgpt.com`.

**Inflación de significancia.** Tono de folleto turístico, "rico tapiz", "momento clave", "legado perdurable", más frases enlatadas tipo "mantiene una presencia activa en redes sociales".

**Sin apuestas personales.** Ningún número que mediste, ningún fracaso, ninguna herramienta nombrada, ningún "perdí $4.000 en esto". Primera persona hueca sigue siendo slop.

**Sobreexplicar lo obvio** y **listas simétricas** (toda viñeta del mismo largo) completan el ritmo de máquina.

## Corrección

Arregla **sumando**, no cambiando sinónimos. Primero escribe, después edita: sustituye abstracciones por nombres, fechas y números; corta el teatro de contraste; rompe trípticos; convierte rayas sobrantes en puntos; borra metacomentario; toma partido; conserva una frase solo si hace trabajo.

## Contexto que exime

- **Público**: lo académico admite más matización que un blog.
- **Propósito**: lo legal exige precisión formularia; el marketing, energía.
- **Longitud**: un texto largo necesita más conectores que uno corto.
- **Dominio**: la escritura técnica tiene normas propias.

La clave es el **sobreuso** y la **repetición inconsciente**, no la existencia del patrón.
