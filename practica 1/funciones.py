import re
from tkinter import *
from tkinter.filedialog import askopenfilename

# en esta viable ingreso los datos del archivo sin \n todo correcto (datos que voy a manipular)
listaSinSaltos = []

numeros = []  # ---- este es el que utilizo para trabajar) --- me contiene en una lista los numeros con los que voy ordenar o buscar
# ---- este es el que utilizo para trabajar) --- me guarda el nombre de cada lista
nombresListas = []
# ---- este es el que utilizo para trabajar) --- guarda las posiciones que tienen las palabras ordenar
nombreOrdenar = []

numeros_desordenados =[]  # contiene la lista de lista con numeros desordenados 


def cargar():
    try:
        root = Tk()
        root.withdraw()
        root.update()
        direccion_archivo = askopenfilename(
            filetypes=[("Text files", "*.txt")])

        archivo_texto = open(direccion_archivo, "r")
        # con readlines leo cada linea de mi archivo y la meto en una lista separada por comas
        separado = archivo_texto.readlines()
        archivo_texto.close()

        # con este for lo que hago es tomar la variable separado y le quito los \n (es la que uso en todo el programa )
        for i in separado:
            listaSinSaltos.append(i.strip())

        print("-------------------------------------------------------")
        print("Datos cargados correctamente")
        print("-------------------------------------------------------")

    except:
        print("No selecciono ningun archivo txt, seleccione un para continuar")


def desplegarListaOrdenada():
    pattern = r"(\d+)"     # busca los numeros de la lista

    for i in listaSinSaltos:
        # busco lo que coincide con el pattern
        valor = re.findall(pattern, i)
        
    #########################   sirve para ordenar ya la lista #################################

        for recorrido in range(1,len(valor)):
            for posicion in range(len(valor)- recorrido):
                if int(valor[posicion]) > int(valor[posicion + 1]):
                    temp = valor[posicion]
                    valor[posicion]=valor[posicion + 1]
                    valor[posicion + 1 ] = temp
        
        numeros.append(valor)  # ingreso ya ordenados los numeros a una lista de lista

    #print(numeros)   # (eliminar ) solo era para probar 


    # -----------------------------------------# busca el nombre de la lista --------------------------------------------
    pattern2 = r"(\w+\=)"    # busca el nombre de la lista
    for i in listaSinSaltos:
        # busco lo que coincide con el pattern1
        valorNames = re.findall(str(pattern2), i)
        nombresListas.append(valorNames)  # ingreso a una lista de lista
    #print(nombresListas)


    # -----------------------------------------# busca la palabra buscar -------------------------------------------------
    pattern3 = r"(ORDENAR)"   # busca la palabra buscar
    for i in listaSinSaltos:
        # busco lo que coincide con el pattern2
        listaOrdenada = re.findall(str(pattern3), i)
        if listaOrdenada:
            nombreOrdenar.append(list(listaOrdenada))
        else:
            nombreOrdenar.append(list("f"))  # agrego una f en la posicion donde no este la palabra ordenar 
                                             #(para que me sirva para saltar esa posicion y no encontrar el valor de ordenar)
    #print(nombreOrdenar)

   #------------------------------------  lista de lista con numeros sesordenados -----------------------------------------

    pattern4 = r"(\d+)"     # busca los numeros de la lista

    for i in listaSinSaltos:
        valor = re.findall(pattern4, i)   # busco lo que coincide con el pattern
        numeros_desordenados.append(valor)  # ingreso ya ordenados los numeros a una lista de lista

    #print(numeros_desordenados)   # (eliminar ) solo era para probar



    #------------------------------------  imprimo respuesta de desplegar listas ordenadas ----------------------------------

    contador = 0

    while contador < len(nombresListas):
        print(str(nombresListas[contador][0]) +str(" ") + str(numeros_desordenados[contador]) + "   Resultado de ordenar: " + str(numeros[contador]))
        print("")
        contador = contador + 1  



    #while contador < len(nombresListas):
     #   for i in numeros_desordenados:
      #      print(nombresListas[contador][0] +" " +  str(i) + "  Resultado de ordenar: " ) 
       #     contador= contador + 1

    #print(numeros)


    #while contador < len(nombresListas):
     #   for i in numeros_desordenados:
      #      for j in numeros:
       #         print(nombresListas[contador][0] +" " +  str(i) + "| Resultado de ordenar: " + str(j) )
        #        contador= contador + 1

    

    