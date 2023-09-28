# #LISTA
posicionClasificacion = []
posicionCarrera = []

#TUPLA
posicionCarrera = ("Barein","Arabia Saudi","Australia","Azerbaiyán")

# DICCIONARIO
pilotos = {
    1: "Verstappen", 3:"Ricciardo", 10:"Gasly", 11:"Perez"
}

equipos = {1:"Red Bull", 2:"Ferrari", 3:"Mercedes", 4:"Alpine", 5:"Mclaren", 6:"Alfa Romeo", 7:"Aston Martin", 8:"Haas", 9:"Alpha Tauri", 10:"Willimans"}

puntos = []
posicion = 0
punto=0
def calcularPuntos(posicion):
    posicion=int(input("Posicion Carrera: "))
    punto=0
    puntos = []
    if posicion == 1:
        punto=25
        puntos.append(punto)
    elif posicion == 2:
        punto=18
        puntos.append(punto)
    elif posicion == 3:
        punto=15
        puntos.append(punto)
    elif posicion == 4:
        punto=12
        puntos.append(punto)
    elif posicion == 5:
        punto=10
        puntos.append(punto)
    elif posicion == 6:
        punto=8
        puntos.append(punto)
    elif posicion == 7:
        punto=6
        puntos.append(punto)
    elif posicion == 8:
        punto=4
        puntos.append(punto)
    elif posicion == 9:
        punto=punto
        puntos.append(punto)
    elif posicion == 10:
        punto=1
        puntos.append(punto)
    else: 
        puntos = 0
    print(punto)
        
    return puntos

opcion = 1
while opcion ==1 or opcion == 2:
    opcion = int(input(("Escoga una opción para continuar: \n1.Agregar \n")))
    if opcion == 1:
        print(calcularPuntos(posicion))
    elif opcion == 2:
        print(calcularPuntos(posicion))

if __name__=="__main__":
    print(f"asd: ${calcularPuntos(posicion)}")
    print(f"Puntos: {puntos}")