#Declara una lista llamada productos con al menos 6, artículos de una tienda escolar




productos = ["Cuadernos",  "Lapiceros", "Maleta", "Regla", "Colores", "Borradores"]
Precios = [ 3500, 1000, 40000, 5000, 13000, 500]
Cantidades = [100, 50, 20, 80, 90, 200]
cantidad_Productos = len(productos)
print("Inventario de la tiendo escolar:"
      "\nProductos:", productos,
      "\nPrecios", Precios,
      "\nCantidades", Cantidades
    )

print(f"el producto {productos[0]} tienen un precio de {Precios[0]} y una cantidad disponible de {Cantidades[0]}")
print(f"el producto {productos[1]} tienen un precio de {Precios[1]} y una cantidad disponible de {Cantidades[1]}")
print(f"el producto {productos[2]} tienen un precio de {Precios[2]} y una cantidad disponible de {Cantidades[2]}")
print(f"el producto {productos[3]} tienen un precio de {Precios[3]} y una cantidad disponible de {Cantidades[3]}")
print(f"el producto {productos[4]} tienen un precio de {Precios[4]} y una cantidad disponible de {Cantidades[4]}")
print(f"el producto {productos[5]} tienen un precio de {Precios[5]} y una cantidad disponible de {Cantidades[5]}")

print(type(productos))
print(type(Precios))

