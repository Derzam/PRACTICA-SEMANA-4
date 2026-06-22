# ============================================================
# servicios/restaurante.py
# Clase que gestiona las operaciones principales del sistema:
# productos registrados, clientes activos y resumen general
# ============================================================

# Importación de los modelos desde la carpeta modelos/
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Clase principal que administra productos y clientes del restaurante."""

    def __init__(self, nombre, direccion):
        # Datos del restaurante
        self.nombre = nombre          # Nombre del restaurante
        self.direccion = direccion    # Dirección física
        self.productos = []           # Lista de productos en el menú
        self.clientes = []            # Lista de clientes registrados

    def agregar_producto(self, producto):
        """Registra un nuevo producto en el menú del restaurante."""
        self.productos.append(producto)
        print(f"  + Producto '{producto.nombre}' agregado al menú.")

    def agregar_cliente(self, cliente):
        """Registra un cliente en el sistema del restaurante."""
        self.clientes.append(cliente)
        print(f"  + Cliente '{cliente.nombre}' registrado.")

    def mostrar_menu(self):
        """Muestra todos los productos disponibles en el menú."""
        print(f"\n{'='*50}")
        print(f"  MENÚ DE {self.nombre.upper()}")
        print(f"{'='*50}")
        if not self.productos:
            print("  No hay productos registrados.")
        else:
            for producto in self.productos:
                producto.mostrar_info()

    def mostrar_clientes(self):
        """Muestra todos los clientes registrados con sus pedidos."""
        print(f"\n{'='*50}")
        print(f"  CLIENTES REGISTRADOS")
        print(f"{'='*50}")
        if not self.clientes:
            print("  No hay clientes registrados.")
        else:
            for cliente in self.clientes:
                print(f"\n  {cliente}")
                cliente.ver_pedidos()

    def mostrar_resumen(self):
        """Muestra un resumen general del estado del restaurante."""
        total_ingresos = sum(c.calcular_total() for c in self.clientes)
        print(f"\n{'='*50}")
        print(f"  RESUMEN — {self.nombre.upper()}")
        print(f"{'='*50}")
        print(f"  Dirección     : {self.direccion}")
        print(f"  Productos en menú : {len(self.productos)}")
        print(f"  Clientes activos  : {len(self.clientes)}")
        print(f"  Ingresos totales  : ${total_ingresos:.2f}")
        print(f"{'='*50}\n")

    def __str__(self):
        """Representación en texto del restaurante."""
        return f"Restaurante: {self.nombre} | Dirección: {self.direccion}"
