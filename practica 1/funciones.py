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
numeros_desordenados_2 =[]  # contiene la lista de lista con numeros desordenados 

posiciones =[] # contiene las posiciones donde esta la palabra ordenar en todo el archivo <------- OJO sirve para filtrar con "ORDENAR"
                # es una lista simple 

nombres_listas_filtro_ordenar = [] # contiene los nombres de las listas donde esta la palabra ORDENAR         <------ SI resultado
                                    # es una lista simple

numeros_desordenados_filtro_ordenar = [] # contiene los numeros desordenados donde esta la palabra ORDENAR    <------ SI resultado


numeros_ordenados_filtro_ordenar = [] # contiene los numeros ordenados donde esta la palabra ORDENAR    <------ SI resultado

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
        #print(listaSinSaltos)   #<-------------------<------<------<--------<-----<-<-----<<<- quitar

        print("-------------------------------------------------------")
        print("Datos cargados correctamente")
        print("-------------------------------------------------------")

    except:
        print("No selecciono ningun archivo txt, seleccione un para continuar")

def desplegarListaOrdenada():

    # -----------------------------------------# busca la palabra buscar -----------------------------------------------------------
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

    # -----------------------------------------# lista con posiciones donde esta la palabra ordenar ---------------------------------
    contador2 = 0
    
    while contador2 < len(nombreOrdenar):
        if nombreOrdenar[contador2][0] == "ORDENAR":
            posiciones.append(int(contador2))          # variable posiciones me contiene las posiciones de la palabra ordenar
            contador2 = contador2 + 1
        else:
            contador2 = contador2 + 1

    
    #print(posiciones)

    # -----------------------------------------# busca el nombre de la lista --------------------------------------------------------

    pattern2 = r"(\w+\=)"    # busca el nombre de la lista
    for i in listaSinSaltos:
        # busco lo que coincide con el pattern1
        valorNames = re.findall(str(pattern2), i)
        nombresListas.append(valorNames)  # ingreso a una lista de lista
    #print(nombresListas)
    
    ###################################################
    # ----------------> #nombres_listas_filtro_ordenar <---- contiene los nombres de las listas donde esta la palabra ORDENAR
    ###################################################

    cont1 = 0
    while cont1 < len(nombreOrdenar):
        if cont1 in posiciones:
            nombres_listas_filtro_ordenar.append(nombresListas[cont1][0])
            cont1 = cont1 + 1
        else:
            cont1 = cont1 + 1

    #print(nombres_listas_filtro_ordenar)
    # ['DATOS=', 'LISTA=', 'DATOS=', 'LISTA=', 'DATOS=', 'LISTA=']

   #------------------------------------  lista de lista con numeros desordenados ---------------------------------------------------

    pattern4 = r"(\d+)"     # busca los numeros de la lista

    for i in listaSinSaltos:
        valor = re.findall(pattern4, i)   # busco lo que coincide con el pattern
        numeros_desordenados.append(valor)  # ingreso desordenados los numeros a una lista de lista

    ###################################################
     # ----------> #numeros_desordenados_filtro_ordenar <---- contiene los numeros de las listas filtrado por el nombre BUSCAR
    ###################################################
    cont2 = 0
    while cont2 < len(nombreOrdenar):
        if cont2 in posiciones:
            if "BUSCAR" in listaSinSaltos[cont2]:
                numeros_desordenados[cont2].pop()
                numeros_desordenados_filtro_ordenar.append(numeros_desordenados[cont2])
                cont2 = cont2 + 1
            else:
                numeros_desordenados_filtro_ordenar.append(numeros_desordenados[cont2])
                cont2 = cont2 + 1
        else:
            cont2 = cont2 + 1

    #print(numeros_desordenados_filtro_ordenar) 


    #-------------------------------------------------------------ordeno la lista de numeros--------------------------------------------

    pattern = r"(\d+)"     # busca los numeros de la lista

    for i in listaSinSaltos:
        # busco lo que coincide con el pattern
        valor1 = re.findall(pattern, i)
    
    #########################   sirve para ordenar ya la lista #################################

        for recorrido in range(1,len(valor1)):
            for posicion in range(len(valor1)- recorrido):
                if int(valor1[posicion]) > int(valor1[posicion + 1]):
                    temp = valor1[posicion]
                    valor1[posicion]=valor1[posicion + 1]
                    valor1[posicion + 1 ] = temp
        
        numeros.append(valor1)  # ingreso ya ordenados los numeros a una lista de lista (pero aun tienen el valor del comando BUSCAR)
                                # y aun no estan filtrados por la palabra ORDENAR

    ##################### filtro los odenados y quito el valor de buscar######################    

    pattern5 = r"(\d+)"     # busca los numeros de la lista

    for i in listaSinSaltos:
        valor2 = re.findall(pattern5, i)   # busco lo que coincide con el pattern
        numeros_desordenados_2.append(valor2)  # ingreso desordenados los numeros a una lista de lista
    
    ###################################################
     # ----------> #numeros_ordenados_filtro_ordenar <---- contiene los numeros ordenados de las listas filtrado (ya es la respuesta)
    ###################################################
   
    cont3 = 0
    while cont3 < len(nombreOrdenar):   # esto solo es un ciclo
        if cont3 in posiciones:       # si posicion cont 3 esta en la lista de posiciones que tienen la palabra ordenar
            if "BUSCAR" in listaSinSaltos[cont3]:  # si la palabra buscar esta en la fila entonces quito su valor
                numero_de_buscar = numeros_desordenados_2[cont3][-1] # adquiero el ultimo valor de la lista para despues usar en remove
                numeros[cont3].remove(numero_de_buscar)  # retiro de la lista numeros el valor de la variable numero_de_buscar
                numeros_ordenados_filtro_ordenar.append(numeros[cont3]) # agrego a la lista ya filtrado y sin numero de buscar
                cont3 = cont3 + 1
            else:
                numeros_ordenados_filtro_ordenar.append(numeros[cont3])
                cont3 = cont3 + 1
        else:
            cont3 = cont3 + 1

    #print(numeros_ordenados_filtro_ordenar)

    #------------------------------------  imprimo respuesta de desplegar listas ordenadas --------------------------------------------

    contador = 0

    while contador < len(nombres_listas_filtro_ordenar):
        print(str(nombres_listas_filtro_ordenar[contador]) +str(" ") + str(numeros_desordenados_filtro_ordenar[contador]) + "   Resultado de ordenar: " + str(numeros_ordenados_filtro_ordenar[contador]))
        print("")
        contador = contador + 1  

    