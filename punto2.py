estudiantes = ()
notas = []
datosEstudiante = {}

nombre = input("Nombre estudiante: ")
materia = input("Materia: ")
estudiante = (nombre, materia)

nota1= float(input("Nota 1: "))
nota2= float(input("Nota 2: "))
nota3= float(input("Nota 3: "))

calcularPromedio = lambda nota1, nota2, nota3: (nota1 + nota2 + nota3) / 3

notas.append(nota1),
notas.append(nota2),
notas.append(nota3)

def agregarEstudiante():
    datosEstudiante['nombre']=nombre
    datosEstudiante['materia']=materia
    datosEstudiante['nota1']=nota1
    datosEstudiante['nota2']=nota2
    datosEstudiante['nota3']=nota3



if __name__=="__main__":
    agregarEstudiante()
    print(f"Promedio: {calcularPromedio(notas[0],notas[1],notas[2])}")
    print(datosEstudiante)