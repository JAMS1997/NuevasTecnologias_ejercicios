#Son inmodificables
#Son no ordenados
#No permite duplicados 
#Son iterables
#Se contruyen usando {}
#Si permiten agregar o eliminar items

usuarios = {"usaer1","user2","user3","user4"}

#no se puede intentar modificarlos usuarios usuarios[1]="usern"

#podemos agregar usuarios
usuarios.add("usuario5") #agrega un usuario a la lista de usuarios
print(usuarios)

#se puede validar si un elemento existe o no en el set
print("user2" in usuarios);
print("user6" in usuarios);

#Se puede remover elementos
usuarios.remove('user2')
print (usuarios);

for i in usuarios:
    print(i)
    
usuariosNuevos = {"user6","user7"};
#Union entre dos sets, devuelve todos los valores que estan en uno u otro conjunto sin repetir nada
usuarios.union(usuariosNuevos)
for i in usuarios:
    print(i)
    
otrosUsuarios = {"user1","user3","user9","user8","user7"}
usuarios.update(otrosUsuarios)
for i in usuarios:
    print(i)
    
#-------------------------------------------------------------------------
#Usos.
#Eliminacion de diplicados:Los conjuntos se pueden utilizar para eliminar elementos duplicados de una lista
lista = [1, 2, 3, 4, 3, 2, 1]
conjunto = set(lista)
print(conjunto) # {1, 2, 3, 4}

#Verificacion de pertenencia: los conjuntos de pueden verificar si un elemento esta presente en una coleccion
conjunto = {1, 2, 3, 4}
if 3 in conjunto:
    print("El elemento está presente")
else:
    print("El elemento no está presente")

#Operaciones matematicas:Los conjuntos se pueden utilizar para realizar operaciones matematicas como la union o la interseccion, diferencio y diferencia simetrica,

conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1.union(conjunto2)
interseccion = conjunto1.intersection(conjunto2)
diferencia = conjunto1.difference(conjunto2)
diferencia_simetrica = conjunto1.symmetric_difference(conjunto2)

print(union) # {1, 2, 3, 4, 5}
print(interseccion) # {3}
print(diferencia) # {1, 2}
print(diferencia_simetrica) # {1, 2, 4, 5}