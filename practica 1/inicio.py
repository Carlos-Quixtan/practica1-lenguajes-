from funciones import cargar
from funciones import desplegarListaOrdenada

print("-------------------------------------------------------")
print("PRACTICA 1")
print("-------------------------------------------------------")


while True:
    
    print("1. Cargar archivo de entrada")
    print("2. Desplegar listas ordenadas")
    print("3. Desplegar busquedas")
    print("4. Desplegar todas")
    print("5. Desplegar todas a archivo")
    print("6. salir")

    datoIngresado = int(input("Ingresa el numero que desea utiizar: "))

    if datoIngresado ==1:
        print("-------------------------------------------------------")
        cargar()
        print("-------------------------------------------------------")

    elif datoIngresado ==2:
        print("-------------------------------------------------------")
        desplegarListaOrdenada()
        print("-------------------------------------------------------")

    elif datoIngresado ==3:
        print("-------------------------------------------------------")

        print("-------------------------------------------------------")

    elif datoIngresado ==4:
        print("-------------------------------------------------------")

        print("-------------------------------------------------------")

    elif datoIngresado ==5:
        print("-------------------------------------------------------")

        print("-------------------------------------------------------")
    
    else:
        print("-------------------------------------------------------")
        print("Gracias por usar nuestro programa")
        print("-------------------------------------------------------")
        
        break
