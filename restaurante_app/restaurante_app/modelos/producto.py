# ============================================================
# modelos/producto.py
# Clase que representa un producto disponible en el restaurante
# (puede ser un plato, bebida o postre)
# ============================================================


class Producto:
    """Representa un producto del menú del restaurante."""

    def __init__(self, nombre, categoria, precio, disponible=True):
        # Atributos principales del producto
        self.nombre = nombre          # Nombre del plato o bebida
        self.categoria = categoria    # Categoría: plato, bebida, postre, etc.
        self.precio = precio          # Precio en dólares
        self.disponible = disponible  # Si el producto puede pedirse o no

    def mostrar_info(self):
        """Muestra la información del producto en consola."""
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"  [{self.categoria.upper()}] {self.nombre} — ${self.precio:.2f} | {estado}")

    def marcar_no_disponible(self):
        """Marca el producto como no disponible (agotado)."""
        self.disponible = False
        print(f"  ⚠ '{self.nombre}' marcado como no disponible.")

    def __str__(self):
        """Representación en texto del producto."""
        return f"{self.nombre} (${self.precio:.2f})"
