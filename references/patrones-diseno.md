---
name: patrones-diseno
description: Patrones de slop visual y de UX — degradados genéricos, muros de tarjetas, tipografía por defecto, microcopy de plantilla — con la alternativa concreta.
---

# Patrones de diseño

Mismo criterio que en texto: **si la decisión no se puede explicar desde el contenido, es plantilla.**

## Visual

### Degradados genéricos

Malla morado/rosa/azul (el "degradado de startup de IA"), degradados holográficos en todo, overlay en cada imagen, el degradado como elemento principal en vez de acento.

**En su lugar:** base de color sólido; degradado como énfasis puntual; paleta desde la marca o el contenido; considera texturas, patrones o ilustración.

### Motivos sobreusados

Figuras 3D flotantes (cubos, esferas, toros) · glassmorphism en todo · neumorfismo donde no corresponde · blur excesivo · sistemas de partículas sin razón · transformaciones de perspectiva en tarjetas.

### Estética de banco de imágenes

Fotos de oficina diversa genérica · gente señalando pantallas con entusiasmo · apretones de manos en traje · plano cenital de MacBook con café.

## Color y tipografía

### Paleta

Morado #7F5AF0 + cian #2CB67D + rosa #FF6AC1 es la firma. También: paleta entera de pasteles, neón en todo, negro puro #000 y blanco puro #FFF como colores principales.

**En su lugar:** 2–3 primarios + neutros, decididos desde la marca; contraste WCAG verificado, no estimado.

### Tipos

Inter para todo · Montserrat + Open Sans · Poppins + Roboto · misma familia para títulos y cuerpo · sans "moderna" por defecto sin razón · 5+ familias distintas.

**En su lugar:** 2–3 familias máximo; jerarquía explícita (H1, H2, cuerpo, pie); tipo de display solo para display.

### Jerarquía

Todo encabezado del mismo tamaño · cuerpo bajo 16px · interlineado bajo 1,5 en cuerpo · párrafos largos centrados.

## Layout

### Estructura de landing de plantilla

Hero con degradado → tres tarjetas de beneficios → testimonios → precios en tres columnas → CTA final. Si el orden no responde a lo que el usuario necesita saber en ese orden, es esqueleto prestado.

### Espaciado

Todo separado exactamente igual · espacio en blanco sin propósito · secciones apretadas alternando con huecos enormes · nada agrupado visualmente.

**En su lugar:** el espaciado crea la jerarquía; lo relacionado va más junto; grilla de 4px u 8px.

### Tarjetas

Todo en tarjeta · tarjetas dentro de tarjetas dentro de tarjetas · sombras y bordes de más · todas del mismo tamaño sin importar el contenido.

**En su lugar:** borde simple, color de fondo o solo espaciado. La tarjeta es una decisión, no el default.

### Centrado universal

Todo el texto centrado, todo el elemento centrado, simetría forzada. Alinea a la izquierda el cuerpo; centra cuando cumple una función.

## Componentes

**Botones:** radio completamente redondeado en todo · sombras flotantes enormes · degradado en cada botón · ghost button como CTA principal · icono sin etiqueta. Jerarquía real (primario/secundario/terciario), objetivo táctil ≥44×44px, etiqueta que nombre la acción.

**Iconos:** línea genérica para todo · sin etiqueta en contexto ambiguo · decorativos sin significado · mezcla de outline y filled · de sets distintos. Un solo sistema de iconos, y que aclaren en vez de decorar.

**Formularios:** icono dentro de cada input · placeholder haciendo de etiqueta · floating labels sin valor · sin estados de error claros · validación genérica ("Campo inválido"). Etiqueta fuera del input, error que diga qué arreglar, agrupación lógica.

## Microcopy

Slop clásico: "Empodera tu negocio" · "Lleva tu X al siguiente nivel" · "Comenzar" como único CTA sin contexto · descripciones a base de palabras de moda · "Sin ruido, sin hype, solo X".

**En su lugar:** di qué hace el producto y para quién; el CTA nombra lo que va a pasar al hacer clic ("Crear cuenta gratis", "Ver demo de 2 min").

## Animación

Fade-in en cada elemento al hacer scroll · parallax sin relación con el contenido · duraciones de 800ms+ en microinteracciones · animación que retrasa una acción del usuario.

**En su lugar:** movimiento con propósito (orientación, continuidad, feedback), 150–300ms en UI, y `prefers-reduced-motion` respetado.

## Orden de revisión

1. Lo estructural (jerarquía, agrupación, contraste, accesibilidad).
2. Lo tipográfico.
3. Lo cromático.
4. Lo decorativo.

Arreglar decoración sobre estructura rota es maquillaje.
