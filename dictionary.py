#Los diccionarios estan compuestos por clave valor
#Son mutables
#No admiten claves repetidas
#Desde python 3.7 son ordenados 

#estan compuestos por clave y valor 
# no admiten claves repetidas 
#desde python 3.7 los diccionarios son ordenados

users = {"name":"Victor",
         "last_name":"Garcia",
         "email":"vag"}

print(len(users))
print(type(users))

#Adicionar 

users ["password"] = "1234"

#ver keys

print(users.keys())

#ver valores 

print(users.values())

#obtener valores 
print(users.get("name"))

#Un ejercicio usando diccionarios y funciones en el que creemos un producto con las siguientes claves
#id, nombre , costo , cantidad, margen de ganancio
# se deben almacenar los productos con dos campos adicionales que son calculados 
# pv =costo/(1-mg) y valor de inventarios = cantidad * costo

#la aplicacion debe permitir iniciar, mostrar un menu 
#1 agregar producto
#2. listar los productos
#3. vender productos 