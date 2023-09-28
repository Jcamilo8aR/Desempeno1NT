#LISTA 
asd = []
pilotos = []

salario = ()
empleado = {}
# ventas = 0
# comision = 0
# impuesto = 0

def salario():
    base = int(input("Salario mensual: "))
    comision = int(input("Comision por venta: "))
    cantVentas = int(input("Cantidad ventas en el mes: "))
    impuesto = int(input("Impuestos (ej:5): "))
    
    x = comision * cantVentas
    c = base + x
    deduccion = (comision * impuesto)/100
    salFinal = c - deduccion
    
    # salario = (base,cantVentas,comision,impuesto, salFinal)
    salario = {"base": base, "cantVentas":cantVentas, "comision":comision,"impuesto":impuesto,"salFinal":salFinal}
    print (f"asd: ${salFinal}")
    print (salario)
    

def calcularSalario():
    salario()
    
    




    
if __name__=="__main__":
    salario()
    