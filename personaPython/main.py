from Persona import Persona

nombre = input("Introduce el nombre: ")
edad = input("Introduce la edad: ")
sexo = input("Introduce el sexo: ")
peso = input("Introduce el peso: ")
altura = input("Introduce la altura: ")

persona1 = Persona(nombre,"",edad,sexo,peso,altura)
persona2 = Persona(nombre,"",edad,sexo)
persona3 = Persona()

print(persona1)
print(persona2)
print(persona3)