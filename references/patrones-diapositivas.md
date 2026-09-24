---
name: patrones-diapositivas
description: Slop en presentaciones (PPTX, HTML, Beamer) — títulos de plantilla, viñetas vacías, diapositivas de relleno — y cómo escribir títulos-afirmación con datos.
---

# Patrones de diapositivas

En una diapositiva cada palabra ocupa espacio en pantalla, así que el relleno se nota más que en prosa. El público lee el título, mira el gráfico y deja de leer. Si el título no dice nada, la diapositiva no dice nada.

Las reglas de esta página son editoriales: vienen de la práctica de consultoría (títulos-afirmación, pirámide de Minto) y de los patrones de `patrones-claude.md`. No hay un corpus que mida su frecuencia en decks.

## La regla que arregla casi todo: título-afirmación

El título es **la conclusión de la diapositiva en una oración, con un dato**. El cuerpo la demuestra.

| Título de plantilla | Título-afirmación |
|---|---|
| El poder del caché | El caché bajó la latencia de 800 a 120 ms |
| Desbloqueando el potencial de los datos | 3 de 5 reportes se pueden armar solos con el data lake actual |
| Más allá de la automatización | Automatizar la conciliación libera 12 horas por semana al equipo de Tesorería |
| Por qué la seguridad importa | En 2025 tuvimos 4 incidentes, todos por credenciales en repositorios |
| Conclusiones clave | Recomendamos migrar el JOB IVDV1JBA en Q1: cuesta Q45.000 y ahorra Q12.000 al mes |
| ¿Y ahora qué? | Próximo paso: aprobar el piloto con 2 agencias antes del 15 de octubre |

**Prueba de los títulos.** Lee solo los títulos, en orden. Deben contar la historia completa sin abrir el cuerpo. Si al leerlos no sabes qué se recomienda ni por qué, el deck está vacío aunque tenga gráficos.

## Títulos de plantilla

Delatan que el título se eligió por cómo suena, no por lo que dice:

- *El poder de X* · *The power of X*
- *Desbloqueando / Liberando / Potenciando X* · *Unlocking X*
- *Más allá de X* · *Beyond X*
- *Transformando X en Y* · *Navegando X* · *El viaje hacia X*
- *X: el futuro de Y* · *Un nuevo paradigma*
- *Por qué X importa* · *Why X matters*
- *Conclusiones clave* · *Key takeaways* · *Reflexiones finales*
- Pregunta retórica como título: *¿Por qué fallan los proyectos?*
- Una sola palabra abstracta: *Innovación*, *Sinergia*, *Visión*

## Viñetas vacías

| Patrón | Ejemplo | Arreglo |
|---|---|---|
| Tríptico de sustantivos abstractos | Eficiencia · Escalabilidad · Innovación | Nombra lo que cambia: "Cierre contable de 5 a 2 días" |
| Gerundio sin sujeto | Optimizando procesos / Impulsando la innovación | Verbo conjugado con sujeto y dato: "Tesorería concilia en 1 hora, no en 6" |
| Verbo inflado | potenciar, impulsar, habilitar, apalancar, maximizar | usar, bajar, subir, permitir, con el número |
| **Término en negrita:** explicación | **Agilidad:** respondemos más rápido al mercado | Quita la etiqueta; deja la frase con dato |
| Viñetas simétricas | Cuatro viñetas del mismo largo y la misma forma | Si una idea es más importante, dale más espacio o su propia diapositiva |
| Emoji como viñeta | 🚀 Crecimiento ✨ Calidad 💡 Ideas | Sin emoji, salvo que la marca los use |
| Cifra sin fuente | ↑ 300% productividad | Fuente, periodo y base: "+18% transacciones por cajero, ene–jun 2026, agencia Zona 10" |

## Diapositivas de relleno

- **Agenda** en un deck de menos de 8 diapositivas.
- **Contexto** o **Antecedentes** que repite lo que el público ya sabe.
- **Misión / Visión / Valores** en un deck técnico.
- **Conclusión** que repite las viñetas anteriores. Cierra con la decisión que pides o con el próximo paso, con fecha y responsable.
- **Gracias / ¿Preguntas?** como diapositiva final. Si hace falta, que la última diapositiva sea la recomendación y quede en pantalla durante las preguntas.

## Frases de cierre y taglines

- Aforismo final: "No se trata de tecnología, se trata de personas."
- Falso equilibrio: "Cada opción tiene sus fortalezas."
- Futuro vago: "El futuro es ahora", "Juntos llegaremos más lejos."

Bórralas. Si la diapositiva necesita cierre, cierra con la cifra o la decisión.

## Notas del orador

Mismo slop que en prosa: "En esta diapositiva veremos…", "Es importante destacar que…". Las notas son para quien presenta: el dato que tiene que recordar, la pregunta difícil que puede venir y su respuesta.

## Densidad en pantalla

- Una idea por diapositiva. Si el título necesita "y", son dos diapositivas.
- Si una viñeta ocupa más de una línea, pásala a las notas o conviértela en título.
- Un gráfico con el título-afirmación encima vale más que cinco viñetas.

## Revisar un deck

```bash
python3 scripts/detectar_slop.py deck.pptx --verbose   # lee diapositivas y notas
python3 scripts/detectar_slop.py deck.html --verbose   # decks HTML (htmlppt, reveal)
```

Para Beamer, pasa el `.tex` directo. Después del número, haz la prueba de los títulos a mano.
