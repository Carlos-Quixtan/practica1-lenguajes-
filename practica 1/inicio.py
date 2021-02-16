from funciones import cargar
from funciones import desplegarListaOrdenada
from funciones import encontrar_numero 
from funciones import cargarTodo
from funciones import datosHTML



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
        encontrar_numero()
        print("-------------------------------------------------------")

    elif datoIngresado ==4:
        print("-------------------------------------------------------")
        cargarTodo()
        print("-------------------------------------------------------")

    elif datoIngresado ==5:
        print("-------------------------------------------------------")
        datosHTML()
        print("-------------------------------------------------------")
    
    else:
        print("-------------------------------------------------------")
        print("Gracias por usar nuestro programa")
        print("")
        print("")
        print("201901159 \n")
        print("Carlos Roberto Quixtán Pérez \n")
        print("carlosquixtan72@gmail.com \n")
        print("Lenguages formales  \n")
        print("-------------------------------------------------------")
        
        break
