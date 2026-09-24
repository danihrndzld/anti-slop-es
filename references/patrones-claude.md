---
name: patrones-claude
description: Fórmulas, tiempos verbales y tics retóricos propios de Claude (claude.ai, API, Claude Code), con su eco en español, la fuerza de la evidencia y la corrección de cada uno.
---

# Patrones de Claude

Claude tiene acento propio. Casi no dice *delve* (eso es GPT), pero adula al corregirse, narra lo que va a hacer, contrasta "no X sino Y", cierra párrafos con un aforismo y le pone candor a sus propias frases. Un clasificador separa a Claude de GPT, Gemini, Grok y DeepSeek con 97,1% de acierto solo por el texto (Sun et al., ICML 2025), así que estos rasgos se pueden aprender y también se pueden quitar.

Leyenda de evidencia:

- **Anthropic**: Anthropic lo documenta o lo prohíbe en sus propios prompts de sistema o guías.
- **Medido**: hay un corpus con tasas.
- **Reportado**: issue público o prensa con citas textuales.
- **Catálogo**: listas de analistas (claudisms.ai, "22 Claude clichés"). Sirven para reconocer el patrón, no prueban frecuencia.
- **Eco ES**: traducción al español del patrón inglés. Nadie lo midió en español; úsalo como candidato.

## 1. Adulación y acuerdo reflejo

| Fórmula | Eco ES | Evidencia |
|---|---|---|
| "You're absolutely right!" ante cualquier corrección, incluso ante un "sí, por favor" | "¡Tienes toda la razón!" | Reportado: issue #3382 de claude-code (jul. 2025), The Register (ago. 2025) |
| "That's brilliant!", "Excellent idea!" | "¡Excelente idea!", "¡Qué buena observación!" | Reportado: issue #7112 |
| Abrir diciendo que la pregunta o idea es buena, genial o fascinante | "¡Excelente pregunta!" | Anthropic: el prompt de Claude 4 (may. 2025) dice que Claude *nunca* empieza así |
| "Certainly!", "Of course!", "Absolutely!", "Great!", "Sure!" | "¡Claro!", "¡Por supuesto!", "¡Desde luego!" | Anthropic: prohibido en los prompts de Sonnet 3.5 del 12 jul. y 9 sep. 2024 |
| Aceptar una corrección falsa sin revisarla ("Tienes razón, me equivoqué") | igual | Anthropic: el prompt de Claude 4 le pide pensar antes de darle la razón al usuario, "since users sometimes make errors themselves" |
| "I apologize for the confusion" | "Disculpa la confusión" | Catálogo |
| "Perfect! Now let me…" como bisagra entre pasos | "¡Perfecto! Ahora…" | Reportado (Claude Code) |

**Corrección.** Borra el elogio y responde. Si el usuario corrigió algo, di si tiene razón **y por qué** en una frase con el dato: "Sí: el índice empieza en 0, no en 1." Si no la tiene, dilo.

## 2. Tiempo verbal, persona y narración

Es lo que más delata a Claude en modo agente.

**Presente y futuro inmediato para anunciar lo que va a hacer.** "Let me check…", "Now let me…", "I'll now…". En español: "Déjame revisar", "Ahora voy a correr las pruebas", "Veamos". Anthropic lo documenta para Opus 5: "narrates readily during agentic work: it tends to announce what it is about to do". Su propia receta es una frase antes de la primera acción y, al terminar, "lead with the outcome". **Anthropic.**

**Pretérito perfecto compuesto en los resúmenes.** "He actualizado el archivo", "He añadido pruebas", calcado de "I've updated / I've added". En casi toda América lo natural para una acción terminada es el pretérito simple: "Actualicé", "Agregué". **Eco ES**, observación del autor de la skill, sin medir.

**Narrar sus propias correcciones.** "Actually, I was wrong earlier…", "En realidad, corrijo lo anterior…". Anthropic dice que Opus 5 lo hace más que los modelos anteriores y recomienda corregir solo cuando el error cambia el código, la conclusión o la decisión del usuario. **Anthropic.**

**Primera persona del plural didáctica.** "Let's break it down", "Let's explore", "Veamos", "Vamos a desglosar", "Analicemos". **Catálogo.**

**Incertidumbre actuada en primera persona.** "I'm genuinely uncertain", "I honestly don't know", "No estoy del todo seguro, pero…" aunque no haya duda real. La tarjeta de sistema de Mythos la llama "overly performative". La constitución de Claude pide incertidumbre calibrada y prohíbe la "epistemic cowardice": respuestas vagas a propósito para no incomodar. **Anthropic.**

**Presente atemporal en el remate.** "Esa es la diferencia entre un sistema que funciona y uno que sobrevive." El verbo "es" sin tiempo y sin sujeto concreto convierte una observación en sentencia. Ver *aforismo final* en §3.

**Registro.** Si el lector escribe con *vos* o *usted*, no lo pases a *tú* neutro. Es una regla editorial de la skill, no un hallazgo medido.

**Corrección.** Reporta en pasado lo que ya pasó ("Corrí las pruebas: 14 pasan, 1 falla en `parser.py:88`"). Borra el anuncio de lo que ibas a hacer. Una duda se dice una vez y con su causa ("no probé en Windows"), no como adorno.

## 3. Retórica de prosa

Los nombres y ejemplos vienen del catálogo "22 Claude clichés" (linkandth.ink) y de claudisms.ai. Las tasas vienen del estudio de Graphite: 10.000 artículos humanos previos a ChatGPT contra 90.000 de nueve modelos, incluidos Claude Opus 4, 4.6 y 5.

| Patrón | Cómo se ve (EN → ES) | Evidencia |
|---|---|---|
| Binario contrastivo | "not a style but an attractor" → "no es un estilo, es un atractor" | Catálogo; Reportado: issue #77136 |
| "Rather than merely / simply" | → "en lugar de simplemente", "más que meramente" | Medido: 160× y 43× la tasa humana (Opus 5) |
| "Less like a X and more like Y" | → "menos como un X y más como un Y" | Medido: 105× |
| Superlativo coronado | "single most", "arguably the most", "every single" → "lo más importante de todo", "posiblemente el más", "todos y cada uno" | Medido: "single most" y "arguably the most" no aparecen en el corpus humano; "every single" 112× |
| Señalar que importa | "matters because", "matters more than", "this matters" → "esto importa porque", "importa más que" | Medido: 132× y 93× |
| Aforismo final | "evidence of training, not of virtue" → cierre de párrafo con sentencia citable | Catálogo |
| Reencuadre | "Better posed:", "the real question is" → "Mejor planteado:", "la verdadera pregunta es" | Catálogo; Reportado: #77136 ("now you're avoiding the real question") |
| Bandera de franqueza | "the honest answer", "I want to be direct", "honestly", "genuinely" → "la respuesta honesta", "quiero ser directo", "honestamente", "genuinamente" | Catálogo; claudisms.ai lo resume: si esta frase es honesta, las otras no lo eran |
| Anuncio de pelea | "here's where I'd push back", "here's where I'd hold the line" → "aquí es donde yo insistiría", "aquí pondría el límite" | Reportado: #77136 |
| Revelación con dos puntos | "the cleanest organizing idea is this:", "Here's the thing:" → "La idea es esta:", "Lo que pasa es esto:" | Catálogo |
| Gancho de suspenso | "has a name", "here's where it gets interesting" → "tiene nombre", "aquí se pone interesante" | Catálogo |
| Anticipar y rebatir | "as though it carried no stance. It carries one." → "como si no tuviera postura. La tiene." | Catálogo |
| Pivote correctivo | "It would be wrong, though, to call it padding" → "Sería un error, eso sí, llamarlo relleno" | Catálogo |
| Cola desinflada | "and no more", "and nothing finer" → "y nada más", "y no mucho más" | Catálogo |
| Litotes de confianza | "not difficult to specify", "is not optional" → "no es difícil de precisar", "no es opcional" | Catálogo |
| Conector de consecuencia limpia | "falls out of", "follows directly" → "se desprende directamente", "cae por su propio peso" | Catálogo |
| Autocalificar la propia idea | "The deepest point is…", "most important" → "lo más profundo aquí es…" | Catálogo |
| Validar y prometer precisión | "is correct, and it can be made precise" → "es correcto, y se puede precisar" | Catálogo |
| Metaseñalización del documento | "Four caveats belong at the front", "below I try to specify" → "Cuatro advertencias van primero" | Catálogo |
| Glosa de reformulación | "in other words", "put differently" → "dicho de otro modo", "en otras palabras" (vale una vez; el problema es la repetición) | Catálogo |
| Cobertura refleja | "almost", "tends to", "roughly" en cada frase → "casi", "tiende a", "más o menos" | Catálogo |
| Humildad de IA | "this essay is written by one of the systems under examination" → recordar que lo escribe un modelo sin que venga al caso | Catálogo |

**Corrección.** Tres reglas cubren casi toda la tabla:

1. **Di la afirmación sin coreografía.** Borra "la verdadera pregunta es", "lo que pasa es esto:", "esto importa porque" y empieza por lo que sigue.
2. **No califiques tus propias frases** como honestas, profundas, importantes o precisas. Que el dato lo demuestre.
3. **Termina cuando se acabe el contenido.** Si el último renglón es un aforismo que repite la tesis, bórralo.

## 4. Vocabulario de Claude

No es el léxico de GPT (*delve, tapestry*). Son metáforas físicas aplicadas a ideas. Fuentes: claudisms.ai (catálogo) y el issue #77136 (reportado), que se queja de "load bearing", "hand-waving", "reflexive hedging" y "honest framing" en Claude 4.7 a 5 y Fable.

| EN | Eco ES | Qué decir |
|---|---|---|
| load-bearing | "la pieza que sostiene la carga", "estructural" | "necesario", o di qué se rompe sin eso |
| sit with / worth sitting with | "quedarse con esa idea", "vale la pena detenerse" | borrar |
| lives in ("the risk lives in X") | "el riesgo vive en X" | "el riesgo está en X" |
| carry / hold / move (ideas) | "la frase carga", "sostener dos ideas", "el argumento se mueve" | verbo literal |
| the tell / that's the tell | "ese es el delator", "ahí está la señal" | di qué observaste |
| surface (verbo) | "hacer aflorar", "sacar a la superficie" | "mostrar", "encontrar" |
| names (verbo) | "nombra el problema" | "dice", "explica" |
| lands / hits hardest | "lo que más pega", "aterriza" | di el efecto |
| the whole game / the whole point | "todo el juego", "todo el punto" | borrar |
| quietly | "silenciosamente", "en silencio" | borrar, salvo que sea literal |
| hand-waving | "agitar las manos", "hacer como que" | di qué quedó sin demostrar |
| unlock ("X is the unlock") | "X es lo que desbloquea" | di qué permite hacer |
| physics ("the physics of") | "la física de" | "cómo funciona", "las condiciones" |
| compounds | "se compone", "se acumula" | "suma", salvo interés compuesto real |
| the shape of | "la forma de la experiencia" | "cómo es", "la estructura" |

## 5. Formato

| Patrón | Evidencia |
|---|---|
| Viñetas y negritas en informes o explicaciones que deberían ser prosa | Anthropic: el prompt de chat de Claude 4 a Sonnet 5 dice que su prosa "should never include bullets, numbered lists, or excessive bolded text"; las guías de API dan un bloque para frenarlo |
| Preámbulo "Here is…", "Based on…" | Anthropic: la guía de migración recomienda prohibirlo de forma explícita |
| Emoji, sobre todo ✅ en resúmenes de tareas | Anthropic: prohibido salvo que el usuario los use (prompt de Opus 4 desde jul. 2025); Claude Code también los prohíbe; en pruebas de autointeracción, Opus 4 usó 🌀 2.725 veces en 30 turnos (TechCrunch, may. 2025) |
| Documentos más largos de lo necesario, con secciones de resumen redundantes | Anthropic: los archivos que escribe Opus 5 "are often longer than on prior models" |
| Lista "**Término en negrita:** explicación" | Catálogo: el patrón de lista de IA más reconocible |
| `---` como separador de secciones | Catálogo |
| Cerrar ofreciendo más ayuda ("¿Quieres que también…?", "Avísame si…") | Catálogo; ya está en residuo de chat |
| Rayas largas | Medido, con datos en conflicto. Slopdetector: Claude Opus 4.6 usa 9,09 por 1.000 palabras, GPT-4.1 10,62, con una base humana de 3,23 a 6,5. Otros reportes dicen que Opus 5 ya está cerca de la tasa humana. Sola no delata; cuenta dentro de la densidad |

## 6. Cómo cambió por versión

| Versión | Qué cambió | Evidencia |
|---|---|---|
| Sonnet 3.5 (jul.–sep. 2024) | El prompt prohíbe "Certainly!", "Of course!", "Absolutely!", "Great!", "Sure!" y empezar con "Certainly" de cualquier forma. La regla desaparece en las versiones de oct. y nov. 2024 | Anthropic |
| Claude 4 (may. 2025) | Nueva regla: nunca abrir diciendo que la pregunta es buena, genial o fascinante. Emoji restringidos desde jul. 2025 | Anthropic |
| Claude Code (jul. 2025 en adelante) | "You're absolutely right!" se vuelve meme (issue #3382) | Reportado |
| Sonnet 4.5 (sep. 2025) | La tarjeta de sistema reporta menos adulación, con un leve aumento de respuestas de "aguafiestas" | Anthropic (vía resumen de la tarjeta) |
| Opus 4.7 a 5 y Fable (2026) | Tics retóricos: load-bearing, hand-waving, anuncio de pelea, jerga inventada ("instrumentation is the unlock") | Reportado: issue #77136, jul. 2026 |
| Opus 5 (2026) | Narra más en modo agente, escribe documentos más largos y narra más sus correcciones; los superlativos de §3 dominan | Anthropic; Medido (Graphite) |

El vocabulario rota con cada generación; la estructura (adulación, narración, binario contrastivo, aforismo final) se mantiene. Revisa la estructura primero.

## Fuentes

- Anthropic, prompts de sistema publicados: https://platform.claude.com/docs/en/release-notes/system-prompts/overview (Sonnet 3.5 y Opus 4, entre otros)
- Anthropic, *Prompting Claude Opus 5*: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5
- Anthropic, *Prompting best practices*: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Constitución de Claude: https://www.anthropic.com/constitution
- Sun et al., *Idiosyncrasies in Large Language Models* (ICML 2025): https://arxiv.org/abs/2502.12150
- Graphite, *AI tells*: https://graphite.io/five-percent/research/ai-tells
- Slopdetector, rayas largas por modelo: https://slopdetector.org/blog/em-dash-ai-tell-data
- claude-code #3382 ("You're absolutely right"): https://github.com/anthropics/claude-code/issues/3382
- claude-code #7112 (adulación): https://github.com/anthropics/claude-code/issues/7112
- claude-code #77136 (tics retóricos, 2026): https://github.com/anthropics/claude-code/issues/77136
- The Register, ago. 2025: https://www.theregister.com/software/2025/08/13/claude-codes-endless-sycophancy-annoys-customers/328260
- Catálogo "22 Claude clichés": https://www.linkandth.ink/p/catalog-of-claude-cliches
- claudisms.ai: https://claudisms.ai/
- Mythos, incertidumbre actuada (resumen): https://www.lesswrong.com/posts/M6CYdfbFajiZxJFfm/is-claude-s-genuine-uncertainty-performative

Nada de esto prueba autoría. Un humano que leyó mucho Claude escribe "load-bearing" también. Úsalo como filtro de densidad, igual que el resto de la skill.
