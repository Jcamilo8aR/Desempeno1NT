#LISTA 
salario = {}
datosEmpleado = []
empleado = ()

def empleado():
    identificacion = int(input("Identificacion: "))
    nombre = input("Nombre Empleado: ")
    edad = int(input("Edad: "))
    empleado = [identificacion, nombre, edad]
    return empleado
    

def salario():
    empleado()
    base = int(input("Salario mensual: "))
    comision = int(input("Comision por venta: "))
    cantVentas = int(input("Cantidad ventas en el mes: "))
    impuesto = int(input("Porcentaje de impuestos (ej:5): "))
    
    x = comision * cantVentas
    c = base + x
    deduccion = (comision * impuesto)/100
    salFinal = c - deduccion
    
    salario = {"base": base, "cantVentas":cantVentas, "comision":comision,"impuesto":impuesto,"salFinal":salFinal}
    print (f"Salario: ${salFinal}")
    print (salario)
    
    datosEmpleado = (empleado, salario)
    return datosEmpleado
    

def actualizar():
    identificacion = int(input("Identificacion: "))
    nombre = input("Nombre Empleado: ")
    edad = int(input("Edad: "))
    empleado = (identificacion, nombre, edad)
    
    base = int(input("Salario mensual: "))
    comision = int(input("Comision por venta: "))
    cantVentas = int(input("Cantidad ventas en el mes: "))
    impuesto = int(input("Porcentaje de impuestos (ej:5): "))
    x = comision * cantVentas
    c = base + x
    deduccion = (comision * impuesto)/100
    salFinal= c - deduccion
    
    salario = {"base": base, "cantVentas":cantVentas, "comision":comision,"impuesto":impuesto,"salFinal":salFinal}
    datosEmpleado = [empleado, salario]
    
    print (f"Salario: ${salFinal}")
    print (salario)
    print(datosEmpleado)
    
    

def opcion():
    opcion = 1
    while opcion ==1 or opcion == 2:
        opcion = int(input(("Escoga una opción para continuar: \n1.Agregar \n2.Actualizar \n3.Salir \n")))
        if opcion == 1:
            salario()
        elif opcion == 2:
            actualizar()
        elif opcion == 3:
            break
    while opcion !=1 and opcion !=2 and opcion !=3 and opcion !=4 and opcion !=5:
        print("Opcion Invalida")
        opcion = int(input(("Escoga una opción para continuar: \n1.Agregar \n2.Actualizar \n")))
        if opcion == 3:
            break
    
    

if __name__=="__main__":
    opcion()
    