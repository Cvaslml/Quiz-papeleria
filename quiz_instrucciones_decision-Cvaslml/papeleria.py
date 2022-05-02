"""Papelería"""

print("--------------------------------------")
print("--------------PAPELERÍA---------------")
print("--------------------------------------")

# input
precio_costo = int(input("Ingresa el valor del producto: "))

# processing
if precio_costo < 3000:
    ganancia = 0.15 * precio_costo
    msj = "El precio de venta del artículo es: $" 

if precio_costo >= 3000 and precio_costo <= 6000:
    ganancia = 500
    msj = "El precio de venta del artículo es: $" 

if precio_costo > 6000:
    ganancia = 0.25 * precio_costo
    msj = "El precio de venta del artículo es: $" 

precio_venta = precio_costo + ganancia 

# output
print(msj + str(precio_venta) + " Y su precio de ganancia: $" + str(ganancia))