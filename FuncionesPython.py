##Bancolobia requiere calcular los salarios de su nueva start-up Pagui:
##Registrar id, nombre, apellido, cargo, area, salario
##requiere listar a los empleados
##requiere calcular el salario neto de cada uno, trniendo presente que si gana  < 2smlv se le paga auxilio de transporte
#imprimir colilla de pago 
#Un empleado podria insert6ar al sistema y buscar su colilla e imprimirla 
#Un analista de RH podria visualizar todos los empleados y todas las colillas de oago, ademas buscar por empleado
# (solamente RH puede registrar empleados)

salario = float(input("Ingrese el Salario"))
def pagoEps(salario):
    return salario * 0.04
def pagoPension(salario):
    return salario * 0.04
def pagoNomina(salario, eps, pension):
    salario_neto = salario - eps - pension
    print (salario_neto)
    
def pagoNomina2(salario):
    eps = pagoEps(salario)
    pension = pagoPension(salario)
    salario_neto = salario - eps - pension 
    print(salario_neto)
    
def pagoNomina3(salario,ejemploCallBack):
    eps = lambda salary: salario * 0.04
    pension = lambda salary: salario * 0.04
    salario_neto = salario - eps(salario) - pension 
    ejemploCallBack(salario_neto)
    
def ejemploCallBack(valor):
    print("El salario neto es: " + valor)
    