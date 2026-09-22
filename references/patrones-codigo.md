---
name: patrones-codigo
description: Antipatrones de código generado por IA — nombres genéricos, comentarios obvios, abstracción innecesaria, manejo de errores de relleno — y cómo limpiarlos sin cambiar comportamiento.
---

# Patrones de código

El equivalente de la prueba de borrado: **si borras la línea y nada se rompe ni se entiende peor, era slop.**

## Nombres

### Genéricos

`data`, `result`, `temp`, `value`, `item`, `thing`, `obj`, `info`, `datos`, `resultado`.

Nombra lo que la cosa **es**:

- `userData` → `currentUser`, `userProfile`, `activeSession`
- `result` → `parsedDocument`, `sortedItems`, `validationError`
- `temp` → `formattedDate`, `normalizedInput`, `previousValue`

### Verbosos de más

`getUserDataFromDatabaseByUserIdAndReturnResult()` → `getUser(userId)`
`calculateTotalSumOfAllItemPricesInCart()` → `calculateCartTotal()`

La firma y el contexto ya dicen el resto.

### Placeholders que sobrevivieron

`foo`/`bar`/`baz` en producción · `test1`, `test2` como nombres de función · prefijos `My*` · sufijos `Helper`, `Manager`, `Handler` sin especificidad.

## Comentarios

### Obvios — bórralos

```python
# mal
# Crear un usuario
user = User()

# Incrementar el contador
counter += 1

# Retornar el resultado
return result
```

Regla: si el código se documenta solo, el comentario sobra.

### TODOs genéricos

```python
# mal
# TODO: implementar esta función
# TODO: agregar manejo de errores

# bien
# TODO(dani): manejar 429 de la API con backoff
# TODO(dani): perfilar este loop, sospecha de O(n²) con n>10000
```

Quién, qué exactamente, y por qué si no es obvio.

### Bloques que anuncian secciones

```python
########################################
# INICIALIZACIÓN
########################################
```

Usa funciones o clases. Los comentarios no deberían tener que mostrar la estructura.

## Estructura

### Capas de abstracción innecesarias

```python
# mal — sobreingeniería típica de IA
class UserManagerFactory:
    def create_user_manager(self): return UserManager()

class UserManager:
    def get_user_repository(self): return UserRepository()

class UserRepository:
    def get_user(self, user_id):
        return db.query(User).filter(User.id == user_id).first()

# bien
def get_user(user_id):
    return db.query(User).filter(User.id == user_id).first()
```

No agregues capas hasta necesitarlas. Patrones de diseño cuando resuelven un problema real, no porque existan.

### Manejo de errores de relleno

```python
# mal
try:
    result = dangerous_operation()
except Exception as e:
    print(f"Ocurrió un error: {e}")
    pass

# peor
try:
    risky_operation()
except:
    pass
```

Captura excepciones específicas. Si de verdad hay que ignorar una, explica por qué en una línea.

### Implementaciones complicadas de tareas simples

```python
# mal
def is_even(n):
    """Verifica si un número es par usando propiedades matemáticas."""
    return (n / 2) == (n // 2)

# bien
def is_even(n):
    return n % 2 == 0
```

### Optimización prematura

`return n << 1` en vez de `return n * 2` "por rendimiento", sin haber perfilado nada.

### Copia y pega

Funciones casi iguales con variaciones mínimas, lógica condicional repetida, manejo de errores duplicado. Extrae lo común — pero solo cuando ya hay tres casos, no dos.

### Números mágicos sin explicación

`if retries > 3:` → constante nombrada o comentario con el porqué.

## Documentación

- **Docstrings genéricos** que repiten la firma (`"""Obtiene el usuario. Args: user_id. Returns: usuario."""`) — borra o explica el porqué.
- **README de plantilla** con secciones vacías de Instalación/Uso/Contribuir que nadie llenó.
- **APIs internas sobredocumentadas** mientras la lógica difícil no tiene una sola nota.

Documenta el **porqué**, no el qué.

## Clasificación para una pasada de limpieza

Antes de editar, ordena el trabajo en estas cinco categorías (de OMC `ai-slop-cleaner`):

1. **Duplicación** — lógica repetida, ramas copiadas, helpers redundantes.
2. **Código muerto** — sin uso, inalcanzable, flags obsoletos, restos de debug.
3. **Abstracción innecesaria** — envoltorios de paso, indirección especulativa, capas de un solo uso.
4. **Violación de fronteras** — acoplamiento oculto, responsabilidades mal puestas, imports o efectos en la capa equivocada.
5. **Pruebas faltantes** — comportamiento sin candado, regresión débil, casos borde sin cubrir.

## Señales de alta confianza

- Toda función tiene docstring, ninguna explica una decisión.
- Todo `try` captura `Exception`.
- Tres o más capas entre la llamada y la query.
- Nombres genéricos en más del 30% de las variables locales.
- Comentarios que traducen el código a español línea por línea.

## Orden de limpieza

1. Borrar código muerto (riesgo casi cero).
2. Quitar comentarios obvios.
3. Renombrar genéricos.
4. Consolidar duplicados.
5. Colapsar abstracciones (riesgo real — requiere pruebas antes).

Verifica después de cada paso. No mezcles pasos en un solo commit.

## Contexto que exime

Código de ejemplo educativo, capas de compatibilidad, wrappers de librería externa con razón documentada, y proyectos con guía de estilo que exige docstrings en todo. El estándar del proyecto le gana a esta lista.
