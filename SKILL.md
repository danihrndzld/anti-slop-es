---
name: anti-slop-es
description: Detecta y elimina "slop" de IA en texto, código y diseño usando umbrales de densidad medibles (Pew 2026, Wikipedia, Slopdetector) en vez de listas de palabras prohibidas. Úsala al revisar o escribir contenido, al armar presentaciones (PPTX, HTML, Beamer), al limpiar código generado por IA, o cuando pidan "deslop", "anti-slop", "quitar el slop" o "esto suena a IA".
license: MIT
---

# Anti-Slop (ES)

Fusión de tres fuentes: el toolkit `anti-slop` (texto/código/diseño), el flujo `ai-slop-cleaner` de OMC (limpieza de código sin cambiar comportamiento) y el marco de densidad de Pew 2026 / Wikipedia / Slopdetector.

## Regla base: densidad, no delatores

Un "profundizar", una raya larga o un tríptico son español normal. El perfil de slop es **varios juntos en un pasaje corto, sin un solo dato concreto**.

- **2 señales medibles en ~500 palabras** → bandera amarilla.
- **3 o 4 en el mismo tramo corto** → huella de IA.
- **Prueba final, siempre**: después de leer un párrafo, ¿puedes repetir un hecho concreto? Si no, sobra quienquiera que lo haya escrito.

Los detectores automáticos son ruidosos, sobre todo con inglés o español de no nativos. Las listas de vocabulario caducan por generación de modelo. Limpiar a máquina aplana la voz sin agregar sustancia. Usa los umbrales como filtro de candidatos, nunca como veredicto.

## Cuándo usarla

- Revisar contenido antes de entregarlo.
- Limpiar texto, código o diseño que "suena genérico".
- Auditar código que funciona pero está inflado, repetido o sobre-abstraído.
- Fijar estándares de calidad de un equipo o proyecto.
- El usuario dice `deslop`, `anti-slop`, `AI slop`, "esto parece escrito por ChatGPT".

## Cuándo NO usarla

- La tarea real es construir una función nueva o un cambio de producto.
- Piden un rediseño amplio, no una pasada incremental.
- Es un refactor genérico sin intención de simplificar.
- El comportamiento del código no está claro y no se puede proteger con pruebas.

## Flujo

### 1. Medir antes de opinar

```bash
python3 scripts/detectar_slop.py <archivo> --verbose
```

Devuelve señales por cada 1.000 palabras, no un juicio moral. Interpretación:

| Señales/1k palabras | Lectura |
|---|---|
| 0–8 | Prosa normal |
| 8–18 | Revisar a mano los tramos marcados |
| 18–35 | Perfil de slop, reescribir secciones |
| 35+ | Plantilla de modelo, reescribir de cero |

### 2. Clasificar lo encontrado

Antes de tocar nada, separa en:

- **Léxico** — vocabulario de época (ver `references/umbrales.md`), inflación latinizante, frases de relleno.
- **Sintaxis** — paralelismo negativo, regla de tres, rango falso, colas de gerundio, evasión de "ser/estar".
- **Formato** — párrafos uniformes, muros de viñetas, títulos en Title Case, residuo de chat.
- **Sustancia** — regresión a la media, trampa de abstracción, citas fantasma, relleno que se puede borrar.
- **Claude** — si el texto salió de Claude, revisa también `references/patrones-claude.md`: adulación al corregirse ("¡Tienes toda la razón!"), narración de lo que va a hacer ("Déjame revisar", "Ahora voy a"), resúmenes en pretérito perfecto calcado ("He añadido"), banderas de franqueza ("honestamente", "la respuesta honesta"), reencuadres ("la verdadera pregunta es"), superlativos ("en lugar de simplemente", "todos y cada uno") y metáforas físicas ("sostiene la carga").

La sustancia manda. El léxico es lo barato de falsificar.

### 3. Arreglar sumando, no sustituyendo sinónimos

- Sustituye abstracciones por **nombres, fechas y números**.
- Corta el teatro de contraste ("no es X, es Y") salvo que corrija un error real.
- Rompe trípticos: si el mundo tiene dos cosas, di dos.
- Convierte rayas largas sobrantes en puntos.
- Borra el metacomentario ("en este artículo veremos...").
- Toma partido. El cierre "ambos tienen sus fortalezas" no es equilibrio, es vacío.
- Reporta en pasado lo que ya pasó ("Corrí las pruebas: 14 pasan") y borra el anuncio de lo que ibas a hacer.
- No califiques tus propias frases como honestas, profundas o importantes; termina cuando se acabe el contenido.
- Conserva una frase solo si está haciendo trabajo.

```bash
python3 scripts/limpiar_slop.py <archivo>            # previsualiza
python3 scripts/limpiar_slop.py <archivo> --guardar  # aplica (deja .backup)
```

El script solo toca lo mecánico (relleno, metacomentario, perífrasis). La sustancia se arregla a mano.

### 4. Verificar

Relee sin el original al lado. Si el texto quedó más corto y con más datos propios, funcionó. Si quedó más corto y más vacío, retrocede.

## Modo código

Mismo principio, otro material: aquí "slop" es código que funciona pero está inflado. **El comportamiento no cambia salvo que lo pidan explícitamente.**

1. **Proteger primero.** Identifica qué debe seguir igual. Agrega la prueba de regresión más estrecha que sirva **antes** de editar. Si no se puede, escribe el plan de verificación antes de tocar código.
2. **Plan antes que código.** Acota a los archivos pedidos. Lista los olores concretos. Ordena de borrado seguro a consolidación riesgosa.
3. **Clasificar el olor**: duplicación · código muerto · abstracción innecesaria · violación de fronteras · pruebas faltantes.
4. **Una pasada por olor**, en este orden: borrar muerto → quitar duplicados → nombres y manejo de errores → reforzar pruebas. Verifica después de cada pasada. No mezcles refactors no relacionados en el mismo diff.
5. **Compuertas de calidad**: regresión en verde, lint, typecheck, pruebas del área tocada. Si una falla, arregla o revierte la limpieza riesgosa; no la fuerces.
6. **Cerrar con evidencia**: archivos cambiados · simplificaciones · corrida de verificación · riesgos restantes.

Detalle de patrones en `references/patrones-codigo.md`.

## Modo revisor (`--review`)

Pasada de solo lectura, después de que el trabajo de limpieza ya está escrito. Existe para mantener separados escritor y revisor: **la misma pasada no escribe y se auto-aprueba**.

En modo revisor:

1. No empieces editando archivos.
2. Revisa el plan, los archivos cambiados y la cobertura de regresión.
3. Busca: código muerto restante, duplicación que debió consolidarse, envoltorios que siguen difuminando fronteras, pruebas débiles, limpieza que cambió comportamiento sin querer.
4. Emite veredicto con acciones requeridas.
5. Devuelve los cambios a una pasada de escritura separada.

## Modo diapositivas

Para PPTX, decks HTML o Beamer. Revisa contra `references/patrones-diapositivas.md`.

1. **Cada título es la conclusión de su diapositiva, con un dato.** "El caché bajó la latencia de 800 a 120 ms", no "El poder del caché".
2. **Prueba de los títulos**: leídos en orden, cuentan la historia y dicen qué se recomienda.
3. Sin viñetas de sustantivos abstractos, sin gerundios sin sujeto, sin emoji, sin diapositivas de "Agenda", "Conclusiones clave" o "¿Preguntas?" que no agregan nada.
4. Mide el archivo final: `python3 scripts/detectar_slop.py deck.pptx --verbose` (lee diapositivas y notas; también `.html`).

## Modo diseño

Revisa contra `references/patrones-diseno.md`. Prioriza lo estructural (jerarquía, espaciado con intención, contraste accesible) sobre lo estético (degradados, glassmorphism). El indicador más fuerte sigue siendo el mismo: si el diseño no se puede explicar desde el contenido, es plantilla.

## Referencias

- `references/umbrales.md` — números medibles, léxico por generación de modelo, fuentes primarias.
- `references/patrones-texto.md` — catálogo ES/EN de léxico, sintaxis, formato y sustancia.
- `references/patrones-diapositivas.md` — títulos-afirmación, títulos de plantilla, viñetas vacías y diapositivas de relleno.
- `references/patrones-claude.md` — fórmulas, tiempo verbal y tics retóricos propios de Claude, con evidencia y cambios por versión.
- `references/patrones-codigo.md` — antipatrones de nombres, comentarios, estructura e implementación.
- `references/patrones-diseno.md` — slop visual, de layout, de componentes y de microcopy.

## Contexto que exime

No todo patrón es slop:

- Lo académico admite más matización.
- Lo legal exige fórmulas fijas.
- La documentación técnica tiene convenciones propias.
- El español neutro corporativo puede ser requisito de marca.

Lo que se persigue es el **uso inconsciente y repetido**, no la existencia del patrón. Un "profundizar" no es la enfermedad. La fluidez vacía sí.
