#Las tuplas se encierran en parentesis
#son inmutables 
#Si se requiere que tenga algun cambio se debe castear a lista
#Se puede acceder a los elementos
#Permiten duplicados 
#permiten distintos tipos de datos

colores =("amarillo","azul","rojo")

#Imprimir tipo de dato
print(type(colores));
#Imprimir Tamaño
print(len(colores));

#Imprimir posiciones
print(colores[0]);
print(colores[1]);
print(colores[2]);

#Castear a lista para que lo podamos modificar
colores_lista = list(colores);
#Agregar elemento
colores_lista.append('verde');
#Imprimir lista
print(colores_lista);
    
colores = tuple(colores_lista)
print(type(colores))

for i in range(len(colores)):
    print(colores[i])
    
#Slicing
print (colores[1:3] ) #Hasta el tercer elemento incluido