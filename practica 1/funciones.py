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
#-------------------------------------------------------------------------------------------------------------------------------------
posicionesbuscar =[] # contiene las posiciones donde esta la palabra buscar en todo el archivo <------- OJO sirve para filtrar con "BUSCAR"
                # es una lista simple 
nombres_listas_filtro_buscar = []

nombreBuscar = [] 

nombresListas2 = []

numeros_desordenados2 = []

numero_con_el_que_voy_a_buscar = []

numeros_desordenados3 = []

numeros_desordenados_filtro_buscar = []

lista_de_encontrados =[]

lista_de_encontrados_final = []

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
        contador = contador + 1  



def encontrar_numero ():
        # -----------------------------------------# busca la palabra buscar -----------------------------------------------------------
    pattern6 = r"(BUSCAR)"   # busca la palabra buscar
    for i in listaSinSaltos:
        # busco lo que coincide con el pattern6
        listaOrdenada2 = re.findall(str(pattern6), i)
        if listaOrdenada2:
            nombreBuscar.append(list(listaOrdenada2))
        else:
            nombreBuscar.append(list("f"))  # agrego una f en la posicion donde no este la palabra buscar 
                                             #(para que me sirva para saltar esa posicion y no encontrar el valor de buscar)
    #print(nombreBuscar)

    # -----------------------------------------# lista con posiciones donde esta la palabra BUSCAR ---------------------------------
    contador0 = 0
    
    while contador0 < len(nombreBuscar):
        if nombreBuscar[contador0][0] == "BUSCAR":
            posicionesbuscar.append(int(contador0))     # variable posicionesbuscar me contiene las posiciones de la palabra BUSCAR
            contador0 = contador0 + 1
        else:
            contador0 = contador0 + 1

    #print(posicionesbuscar)
    
        # -----------------------------------------# busca el nombre de la lista --------------------------------------------------------

    pattern7 = r"(\w+\=)"    # busca el nombre de la lista
    for i in listaSinSaltos:
        # busco lo que coincide con el pattern1
        valorNamess = re.findall(str(pattern7), i) # esta variable solo me almacena el nombre de la lista para despues ingresar a la lista
        nombresListas2.append(valorNamess)  # ingreso a una lista de lista
    #print(nombresListas2)
    
    ###################################################
    # ----------------> #nombres_listas_filtro_buscar <---- contiene los nombres de las listas donde esta la palabra BUSCAR
    ###################################################

    cont1 = 0
    while cont1 < len(nombreBuscar):
        if cont1 in posicionesbuscar:
            nombres_listas_filtro_buscar.append(nombresListas2[cont1][0])
            cont1 = cont1 + 1
        else:
            cont1 = cont1 + 1

    #print(nombres_listas_filtro_buscar)
    # ['LISTA=', 'La=', 'LISTA=', 'La=', 'La=', 'LISTA=', 'holaaaaaaa=']


    #------------------------------------  lista simple con los numeros que que voy a buscar ---------------------------------------------------

    pattern8 = r"(\d+)"     # busca los numeros de la lista

    for i in listaSinSaltos:
        valor = re.findall(pattern8, i)   # busco lo que coincide con el pattern
        numeros_desordenados2.append(valor)  # ingreso desordenados los numeros a una lista de lista

    ###################################################
     # ----------> #numero_con_el_que_voy_a_buscar <---- contiene los numeros con los qu voy a ejecutar la opcion de buscar 
    ###################################################
    cont2 = 0
    while cont2 < len(nombreBuscar):
        if cont2 in posicionesbuscar:
            if "BUSCAR" in listaSinSaltos[cont2]:
                numero_buscado = numeros_desordenados2[cont2][-1]
                numero_con_el_que_voy_a_buscar.append(numero_buscado)
                cont2 = cont2 + 1
            else:
                cont2 = cont2 + 1
        else:
            cont2 = cont2 + 1

    #print("")
    #print("estos son los numeros que le pertenecen a cada comando de buscar")
    #print(numero_con_el_que_voy_a_buscar) 


   #------------------------------------  lista de lista con numeros desordenados sin el numero de BUSCAR ---------------------------------------------------

    patterN9 = r"(\d+)"     # busca los numeros de la lista

    for i in listaSinSaltos:
        valor = re.findall(patterN9, i)   # busco lo que coincide con el pattern
        numeros_desordenados3.append(valor)  # ingreso desordenados los numeros a una lista de lista

    ###################################################
     # ----------> #numeros_desordenados_filtro_buscar <---- contiene los numeros de las listas filtrado por el nombre BUSCAR
    ###################################################
    cont2 = 0
    while cont2 < len(nombreBuscar):
        if cont2 in posicionesbuscar:
            if "BUSCAR" in listaSinSaltos[cont2]:
                numeros_desordenados3[cont2].pop()  # quito el numero excedente que le pertece al opcion de buscar
                numeros_desordenados_filtro_buscar.append(numeros_desordenados3[cont2])  # agrego el que ya no tiene el numero excedente
                cont2 = cont2 + 1
            else:
                numeros_desordenados_filtro_buscar.append(numeros_desordenados3[cont2])
                cont2 = cont2 + 1
        else:
            cont2 = cont2 + 1
    #print("")
    #print(numeros_desordenados_filtro_buscar) 
    #print("")
    #print("")

    
     #------------------------------------  lista que contiene las posiciones donde esta el numero buscado ---------------------------------------------------
    
    cont3 = 0
    while cont3 < len(numero_con_el_que_voy_a_buscar):  # esto me sirve para repetir el numero de elementos que tiene la lista
# cont3 = me sirve para recorrer cada elemento que contiene mi lista de numeros a buscar y con estos comparar si se encuentra en las listas
        lista_de_encontrados =[]
        contt2 = 0
        while contt2 < len(numeros_desordenados_filtro_buscar[cont3]): # se va repetir el numero de elementos que tenga esa posicion
                                                            # con esto aseguro que se van a valuar todos los numeros de dicha posicion 
            if numeros_desordenados_filtro_buscar[cont3][contt2] == numero_con_el_que_voy_a_buscar[cont3]: # valuo si el valor .....->
                    # es igual al elemento que tiene mi lista de numeros buscados en ese momento 
                lista_de_encontrados.append(contt2) 
                contt2 = contt2 + 1   # con esto lo que hago es pasar al otro numero de mi elemnto 
            else:
                
                contt2 = contt2 + 1 

        #print(lista_de_encontrados)
        #print("se agrego el valor a la lista")
        lista_de_encontrados_final.append("encontrado en: " + str(lista_de_encontrados))
            
        #lista_de_encontrados_final.append(lista_de_encontrados)
        cont3 = cont3 + 1 
   


    #print("se finalizo la busqueda")
    
    contadorrr = 0

    while contadorrr < len(lista_de_encontrados_final):
        if lista_de_encontrados_final[contadorrr] == "encontrado en: []":
            lista_de_encontrados_final[contadorrr] = "No encontrado"
            contadorrr +=1
        else:
            contadorrr += 1
    #print(lista_de_encontrados_final)

    #------------------------------------  imprimo respuesta de desplegar busqueda -------------------------------------------------------

    contador = 0

    while contador < len(numeros_desordenados_filtro_buscar):
        print(str(nombres_listas_filtro_buscar[contador]) +str(" ") + str(numeros_desordenados_filtro_buscar[contador]) + "   valor buscado: " + str(numero_con_el_que_voy_a_buscar[contador]) + "  " + str(lista_de_encontrados_final[contador]))
        contador = contador + 1 




def cargarTodo():

    contador1 = 0

    while contador1 < len(nombres_listas_filtro_ordenar):
        print(str(nombres_listas_filtro_ordenar[contador1]) +str(" ") + str(numeros_desordenados_filtro_ordenar[contador1]) + "   Resultado de ordenar: " + str(numeros_ordenados_filtro_ordenar[contador1]))
        contador1 = contador1 + 1  

    print()

    contador = 0

    while contador < len(numeros_desordenados_filtro_buscar):
        print(str(nombres_listas_filtro_buscar[contador]) +str(" ") + str(numeros_desordenados_filtro_buscar[contador]) + "   valor buscado: " + str(numero_con_el_que_voy_a_buscar[contador]) + "  " + str(lista_de_encontrados_final[contador]))
        contador = contador + 1 


#-----------------------------------------------------  FUNCION PARA DATOSHTML -----------------------------------------------------------  
def tabla():
    texto=""
    contador1 = 0

    while contador1 < len(nombres_listas_filtro_ordenar):
        texto+="<tr>"
        texto+="<td>"+ str(str(nombres_listas_filtro_ordenar[contador1]) +str(" ") + str(numeros_desordenados_filtro_ordenar[contador1]) + "   Resultado de ordenar: " + str(numeros_ordenados_filtro_ordenar[contador1]))+"</td>"
        texto+="</tr>"
        contador1 = contador1 + 1  

    contador = 0

    while contador < len(numeros_desordenados_filtro_buscar):
        texto+="<tr>"
        texto+="<td>"+ str(str(nombres_listas_filtro_buscar[contador]) +str(" ") + str(numeros_desordenados_filtro_buscar[contador]) + "   valor buscado: " + str(numero_con_el_que_voy_a_buscar[contador]) + "  " + str(lista_de_encontrados_final[contador]))+"</td>"
        texto+="</tr>"
        contador = contador + 1 

    return(texto)


def datosHTML():
    import webbrowser
    funcion= open("tarea.html", "wb")
    abrir = """<html>
    <head>
    <meta charset="utf8" />
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
    <title>Registros</title>



    </head>

    <body>
        <h1>Los datos son:</h1>
        <div class="container">
            <table class="table">"""
    abrir+= tabla()

    abrir+="""
            
            </table>
    </div>
    </body>
    </html>"""
    
    funcion.write(bytes(abrir, "ascii"))
    funcion.close()
    webbrowser.open_new_tab("tarea.html") 

