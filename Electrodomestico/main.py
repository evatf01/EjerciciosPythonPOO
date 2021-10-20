from Electrodomestico import Electrodomestico

# precioBase=100,color="blanco",consumo='F',peso=5
from lavadora import Lavadora
from Television import Television

electros = ()
electros = list(electros)

# Electrodomesticos
electros.insert(-1, Electrodomestico(consumo="A", peso=15))
electros.insert(-1, Electrodomestico(consumo="A", peso=30))
electros.insert(-1, Electrodomestico(consumo="A", peso=60))
electros.insert(-1, Electrodomestico(consumo="A", peso=90))

# Lavadoras
electros.insert(-1, Lavadora(consumo="E", peso=50, carga=30))
electros.insert(-1, Lavadora(consumo="A", peso=50, carga=60))

# Televisiones
electros.insert(-1, Television(peso=20, resolucion=30))
electros.insert(-1, Television(peso=20, resolucion=50))

tv,lava,electro = 0,0,0
i = 0
for ele in electros:
    i+=1
    ele.precioFinal()
    # print(ele.precioBase)

    if isinstance(ele,Television):
        tv += ele.precioBase
    elif isinstance(ele,Lavadora):
        lava += ele.precioBase
    else:
        electro += ele.precioBase

print("Total Televisiones: " + repr(tv))
print("Total Lavadoras: " + repr(lava))
print("Total Electrodomesticos varios: " + repr(electro))

print("Total: " + repr(tv+lava+electro))