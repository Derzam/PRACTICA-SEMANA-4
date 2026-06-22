# ============================================================
# main.py
# Punto de arranque del sistema de gestión de restaurante
# Se crean objetos y se ejecutan los métodos del sistema
# ============================================================

# Importación del servicio principal y los modelos
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


# ----------------------------------------------------------
# 1. Crear el restaurante (instancia del servicio principal)
# ----------------------------------------------------------
restaurante = Restaurante(
    nombre="La Sazón Manaba",
    direccion="Av. Machala y Eloy ALfaro"
)

print(f"\n{'='*50}")
print(f"  SISTEMA INICIADO")
print(f"  {restaurante}")
print(f"{'='*50}\n")


# ----------------------------------------------------------
# 2. Crear productos del menú (instancias de Producto)
# ----------------------------------------------------------
print(">> Registrando productos en el menú...")

p1 = Producto("Seco de pollo",    categoria="Plato principal", precio=4.50)
p2 = Producto("Llapingachos",     categoria="Entrada",         precio=2.75)
p3 = Producto("Jugo de naranja",  categoria="Bebida",          precio=1.00)
p4 = Producto("Agua mineral",     categoria="Bebida",          precio=0.75)
p5 = Producto("Flan de caramelo", categoria="Postre",          precio=1.50)
p6 = Producto("Ceviche de camarón", categoria="Plato principal", precio=5.00)

# Agregar productos al restaurante
restaurante.agregar_producto(p1)
restaurante.agregar_producto(p2)
restaurante.agregar_producto(p3)
restaurante.agregar_producto(p4)
restaurante.agregar_producto(p5)
restaurante.agregar_producto(p6)


# ----------------------------------------------------------
# 3. Crear clientes (instancias de Cliente)
# ----------------------------------------------------------
print("\n>> Registrando clientes...")

c1 = Cliente("Ana Rodríguez", telefono="0991234567", mesa=3)
c2 = Cliente("Carlos Vega",   telefono="0987654321", mesa=7)
c3 = Cliente("Lucía Mora",    telefono="0976543210", mesa=1)

# Agregar clientes al restaurante
restaurante.agregar_cliente(c1)
restaurante.agregar_cliente(c2)
restaurante.agregar_cliente(c3)


# ----------------------------------------------------------
# 4. Registrar pedidos de cada cliente
# ----------------------------------------------------------
print("\n>> Registrando pedidos...")

# Pedidos de Ana
c1.agregar_pedido(p1)  # Seco de pollo
c1.agregar_pedido(p3)  # Jugo de naranja
c1.agregar_pedido(p5)  # Flan de caramelo

# Pedidos de Carlos
c2.agregar_pedido(p6)  # Ceviche de camarón
c2.agregar_pedido(p4)  # Agua mineral

# Marcar un producto como no disponible y probar el sistema
p2.marcar_no_disponible()      # Llapingachos agotados
c3.agregar_pedido(p2)          # Lucía intenta pedir — debe rechazarse
c3.agregar_pedido(p6)          # Ceviche sí disponible
c3.agregar_pedido(p3)          # Jugo de naranja


# ----------------------------------------------------------
# 5. Mostrar información organizada en consola
# ----------------------------------------------------------
restaurante.mostrar_menu()
restaurante.mostrar_clientes()
restaurante.mostrar_resumen()
