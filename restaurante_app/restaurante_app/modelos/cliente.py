# ============================================================
# modelos/cliente.py
# Clase que representa a un cliente del restaurante
# ============================================================


class Cliente:
    """Representa a un cliente que realiza pedidos en el restaurante."""

    def __init__(self, nombre, telefono, mesa=None):
        # Datos de identificación del cliente
        self.nombre = nombre        # Nombre del cliente
        self.telefono = telefono    # Teléfono de contacto
        self.mesa = mesa            # Número de mesa asignada (puede ser None)
        self.pedidos = []           # Lista de productos pedidos (inicia vacía)

    def agregar_pedido(self, producto):
        """Agrega un producto al pedido del cliente si está disponible."""
        if producto.disponible:
            self.pedidos.append(producto)
            print(f"  ✔ '{producto.nombre}' agregado al pedido de {self.nombre}.")
        else:
            print(f"  ✘ '{producto.nombre}' no está disponible en este momento.")

    def calcular_total(self):
        """Calcula y devuelve el total a pagar por el cliente."""
        return sum(p.precio for p in self.pedidos)

    def ver_pedidos(self):
        """Muestra todos los productos pedidos por el cliente."""
        if not self.pedidos:
            print(f"  {self.nombre} no tiene pedidos registrados.")
        else:
            print(f"  Pedidos de {self.nombre}:")
            for producto in self.pedidos:
                print(f"    - {producto}")
            print(f"  Total: ${self.calcular_total():.2f}")

    def __str__(self):
        """Representación en texto del cliente."""
        mesa_info = f"Mesa {self.mesa}" if self.mesa else "Sin mesa"
        return f"{self.nombre} | Tel: {self.telefono} | {mesa_info} | Pedidos: {len(self.pedidos)}"
