producto = input("Nombre producto: ")
precio = float(input("Precio: "))
unidades = int(input("Cantidad: "))
# print("{producto}: {q:3d} unidades x {precio:9.2f}€ = {total:11.2f}€".format(producto = producto, q = q, precio = precio, total = q*precio))
print("{producto}: {unidades:3d} unidades x {precio:9.2f} € = {total:11.2f} €".format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))