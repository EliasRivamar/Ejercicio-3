from Registro import Registro
from Manejador import Manejador

if __name__ == "__main__":
    D = 2
    T = 2
    m = Manejador(D, T)
    m.test()
    m.mostrar(D,T)
    opcion = 1
    while opcion != 0:
        print("1: Mostar Menores")
        print("2: Temperatura Promedio Mensual por Hora")
        print("3: Dado un Dia Listar los valores")
        print("$: Salir")
        opcion = int(input())
        if opcion == 1:
            m.Temperatura(D,T)
            m.Humedad(D,T)
            m.Presion(D,T)
        elif opcion == 2:
            print("La temperatura promedio es:")
            print(m.temperaturaPromedio(D, T))
        elif opcion == 3:
            dia = int(input("Ingrese un dia"))
            m.mostarDia(dia, D, T)
        elif opcion == 4:
            exit()
        else:
            print("----Opcion Incorrecta----")