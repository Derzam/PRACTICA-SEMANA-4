# 🍽️ Sistema de Gestión de Restaurante
### Programación Orientada a Objetos en Python
Nombre: Derly Zambrano
---

## Descripción

Este proyecto implementa un sistema básico de gestión para un restaurante utilizando **Programación Orientada a Objetos (POO)** en Python. El objetivo principal es demostrar cómo organizar un proyecto en módulos, separar responsabilidades entre clases y comunicar archivos mediante importaciones.

El sistema permite registrar productos del menú, gestionar clientes con sus pedidos y obtener un resumen general del estado del restaurante.

---

## Estructura del Proyecto

```
restaurante_app/
│
├── modelos/                  # Clases del dominio del problema
│   ├── __init__.py
│   ├── producto.py           # Clase Producto
│   └── cliente.py            # Clase Cliente
│
├── servicios/                # Lógica principal del sistema
│   ├── __init__.py
│   └── restaurante.py        # Clase Restaurante
│
└── main.py                   # Punto de arranque del programa
```

---

##  Clases Implementadas

### `Producto` — `modelos/producto.py`

Representa un plato, bebida o postre disponible en el menú del restaurante.

| Atributo | Tipo | Descripción |
|---|---|---|
| `nombre` | `str` | Nombre del producto |
| `categoria` | `str` | Categoría (plato principal, bebida, postre, etc.) |
| `precio` | `float` | Precio en dólares |
| `disponible` | `bool` | Indica si el producto puede pedirse |

| Método | Descripción |
|---|---|
| `mostrar_info()` | Imprime la información del producto en consola |
| `marcar_no_disponible()` | Marca el producto como agotado |
| `__str__()` | Devuelve una representación en texto del producto |

---

### `Cliente` — `modelos/cliente.py`

Representa a una persona que realiza o consume pedidos en el restaurante.

| Atributo | Tipo | Descripción |
|---|---|---|
| `nombre` | `str` | Nombre del cliente |
| `telefono` | `str` | Número de contacto |
| `mesa` | `int` | Número de mesa asignada |
| `pedidos` | `list` | Lista de productos pedidos |

| Método | Descripción |
|---|---|
| `agregar_pedido(producto)` | Agrega un producto al pedido si está disponible |
| `calcular_total()` | Calcula el monto total a pagar |
| `ver_pedidos()` | Muestra los productos pedidos y el total |
| `__str__()` | Devuelve una representación en texto del cliente |

---

###  `Restaurante` — `servicios/restaurante.py`

Clase principal que administra los productos del menú y los clientes registrados.

| Atributo | Tipo | Descripción |
|---|---|---|
| `nombre` | `str` | Nombre del restaurante |
| `direccion` | `str` | Dirección física |
| `productos` | `list` | Lista de productos registrados |
| `clientes` | `list` | Lista de clientes activos |

| Método | Descripción |
|---|---|
| `agregar_producto(producto)` | Registra un producto en el menú |
| `agregar_cliente(cliente)` | Registra un cliente en el sistema |
| `mostrar_menu()` | Muestra todos los productos del menú |
| `mostrar_clientes()` | Muestra los clientes con sus pedidos |
| `mostrar_resumen()` | Muestra un resumen general del restaurante |
| `__str__()` | Devuelve una representación en texto del restaurante |

---

## Cómo Ejecutar el Programa

### Requisitos
- Python 3.x instalado

### Pasos
1. Clonar o descargar el repositorio.
2. Abrir una terminal en la carpeta raíz del proyecto (`restaurante_app/`).
3. Ejecutar el archivo principal:

```bash
python main.py
```


## Relación entre Clases

```
Restaurante
├── lista de Producto(s)   →  modelos/producto.py
└── lista de Cliente(s)    →  modelos/cliente.py
                                  └── lista de Producto(s) pedidos
```

La clase `Restaurante` actúa como coordinadora del sistema. Contiene listas de objetos `Producto` (el menú) y objetos `Cliente`. A su vez, cada `Cliente` mantiene su propia lista de objetos `Producto` que representan sus pedidos.

---

##  Conceptos de POO Aplicados

| Concepto | Aplicación en el proyecto |
|---|---|
| **Clases y objetos** | `Producto`, `Cliente` y `Restaurante` son clases; sus instancias son los objetos del sistema |
| **Constructor `__init__()`** | Todas las clases inicializan sus atributos en el constructor |
| **Método `__str__()`** | Implementado en las 3 clases para representar objetos como texto |
| **Encapsulamiento** | Cada clase gestiona su propia información y expone métodos para operar sobre ella |
| **Composición** | `Restaurante` contiene listas de `Producto` y `Cliente`; `Cliente` contiene una lista de `Producto` |
| **Importaciones** | Los módulos se comunican mediante `from modelos.producto import Producto` |
