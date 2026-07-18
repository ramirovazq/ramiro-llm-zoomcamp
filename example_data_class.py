from dataclasses import dataclass
from dataclasses import asdict

@dataclass(frozen=True)
class Producto:
    id: int
    nombre: str
    precio: float
    cantidad: int

    def __post_init__(self):
        if self.precio < 0 or self.cantidad < 0:
            raise ValueError("el precio y cantidad no deben ser menores que cero")
            #print("algo mal")
        
    def valor_inventario(self):
        return self.cantidad * self.precio


p = Producto(
    id=1,
    nombre="Laptop",
    precio=15000.0,
    cantidad=5
) 

print(p)
print(p.valor_inventario())


p.precio = 20000.0  # Esto generará un error porque la clase es inmutable (frozen=True)
# Producto(
#     id=2,
#     nombre="Mouse",
#     precio=-100,
#     cantidad=3
# )
p_dict = asdict(p)
print(p_dict)