materias = ["Matematicas", "Español", "Ciencias", "Sociales", "Fisica", "Quimica"]
print(materias)

# Para determinar el tamaño de la lista 
# print(len(materias))

# print(dir(materias))

# Acceder a elementos indicando la posicion de la lista
# print(materias[2])

# Slicing muestra las posiciones desde un rango
# print(materias[2:5])

# print(materias[3:])

# print(materias[:5])

# print(materias[-5:-1])


# Tipos de datos en listas
edades = [17, 27, 42, 31, 56, 68]

# print(type(edades))

# Actualizar un elemento de la lista
materias[2] = "Biologia"

# print(materias[0:])

materias[1:3] = "Lengua Castellana", "Ciencias Naturales"
# print(materias[0:])

################################################################

# Agregando elementos a la lista
materias.append("Religion")
# print(materias[0:])

materias.insert(0, "Etica")
# print(materias[0:])

# materias.pop()
# print(materias[0:])

# materias.remove("Etica")
# print(materias[0:])

# del materias[4]
# print(materias[0:])

# Iterar listas con ciclo for

# print("-"*80)
# for i in materias:
#     print(i)

# print("-"*80)    

# for i in range(len(materias)):
#     print(materias[i])

# print("-"*80)    


# for i, materia in enumerate(materias):
#     print(i, materia)

print("-"*80)  

# Usando un while
i = 0
while i < len(materias):
    print(materias[i])
    i += 1

print("-"*80)

# Comprension de listas
[print(i) for i in materias]