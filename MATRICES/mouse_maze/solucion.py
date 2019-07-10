"""
SOLUCIÓN PROPUESTA EJERCICIO 1 GUÍA 10 TIPO PRUEBA- Tutoría de Programación 14-diciembre-2018
Autor: Rosita Hormann Lobos.
Contacto: rosita.hormannlobos@gmail.com o rhl003@alumnos.ucn.cl


"""

import numpy as np

def separacion():
    print("- - - - - - - - - - - - - - - - - - - - - - - - -")

######################################################
# LECTURA DEL ARCHIVO experimentos.txt
experimentosTxt = open("experimentos.txt","r") # Archivo que tiene lista de experimentos
listaExperimentos = []
exp = experimentosTxt.readline().strip()
cantExps = 0 # Cantidad de experimentos
while exp != "":
    listaExperimentos.append(exp)
    exp = experimentosTxt.readline().strip()
    cantExps +=1

def imprimirOpciones(listaOpciones):
    pos = 0
    for elem in listaOpciones:
        print(pos, ") ", elem)
        pos += 1

######################################################
# A partir de aquí se pregunta al usuario qué experimentos quiere consultar
# y se realizan los requerimientos principales del problema:

seguir = True # Seguir preguntando
while seguir:
    ######################################################
    # Escogiendo experimento a procesar
    imprimirOpciones(listaExperimentos)

    opcionValida = False # Todavía no se ingresan opciones
    while not opcionValida:
        pos = int(input("Que experimento quiere consultar?:" )) # "pos" representa la posicion dentro de la listaExperimentos
        if pos >= cantExps or pos < 0:
            print("Posicion inválida. Por favor escriba un numero entre 0 y ", (cantExps - 1))
        else:
            opcionValida = True
    expTxt = open(listaExperimentos[pos],"r") # Se abre el archivo del experimento seleccionado.

    ######################################################
    #Se procede a procesar el archivo del laberinto
    nombreLaberinto = expTxt.readline().strip() # Primera linea del archivo debe ser el nombre del archivo del laberinto
    mazeTxt = open(nombreLaberinto,"r") # Se abre el archivo del laberinto.
    linea = mazeTxt.readline().strip() # Se lee la primera linea, que tiene dos numeros en formato n,m
    partes = linea.split(",")

    n = int(partes[0]) # Filas de la matriz del laberinto
    m = int(partes[1]) # Columnas de la matriz del laberinto
    
    laberinto = np.zeros([n, m])
    laberintoBueno = True
    cantidadQuesos = 0
    cantidadSalidas = 0
    archivoBueno = True # Asumimos que el archivo no tiene errores
    for i in range(n):
        linea = mazeTxt.readline().strip()
        partes = linea.split(",") # Ahora "partes" es un arreglo de "m" strings.
        for j in range(m):
            if partes[j] == "P": # Pared
                laberinto[i][j] = 1
            elif partes[j] == "Q": # Queso
                laberinto[i][j] = 8
                cantidadQuesos += 1
            elif partes[j] == " ": # Espacio libre
                laberinto[i][j] = 0
            elif partes[j] == "S": # Salida
                laberinto[i][j] = 5
                cantidadSalidas += 1
            else:
                print("El archivo tiene un error!")
                archivoBueno = False
    if archivoBueno:
        if cantidadSalidas <= 0:
            print("Experimento no válido (laberinto no tiene salidas)")
            print(laberinto)
            print(cantidadSalidas)
        else:
            ######################################################
            # Ahora se posiciona al ratón en el laberinto.
            #posicionInicial = expTxt.readline().strip().split(",") # La siguiente línea a leer es la posicion inicial del ratón
            posicionInicial = expTxt.readline().strip()
            print(posicionInicial)
            posicionInicial = posicionInicial.split(",")
            filaActual = int(posicionInicial[0]) # fila en la que se encuentra el ratón.
            columnaActual = int(posicionInicial[1])  # columna en la que se encuentra el ratón.
            print("POSICION INICIAL: ", posicionInicial)
            laberinto[filaActual][columnaActual] = 6 # Se marca posicion del ratón
            
            separacion()
            print(laberinto) # Se imprime el laberinto tal cual está ahora.
            separacion()
            ######################################################

            ######################################################
            # Ahora comenzaremos a mover el ratón a través del laberinto.
            movimiento = expTxt.readline().strip()
            ratonSalio = False
            quesosCapturados = 0
            
            while movimiento != "" and not ratonSalio:
                x = input("Presione enter para continuar") # Esta línea de código nos permitirá que la lectura de los movimientos del ratón no se realicen todas de una, sino que el programa espere a que el usuario presione "enter" para pasar al siguiente movimiento.
                separacion()
                
                movFilas = 0
                movColumnas = 0

                if movimiento == "U": #up (arriba)
                    movFilas = -1 # Hay que disminuir la fila.
                    
                elif movimiento == "D": #down (abajo)
                    movFilas = 1 # Hay que aumentar la fila.
                    
                elif movimiento == "L": # left (izquierda)
                    movColumnas = -1 # Hay que disminuir la columna.
                    
                elif movimiento == "R": # right (derecha)
                    movColumnas = 1 # Hay que aumentar la columna.

                nuevaFila = filaActual + movFilas
                nuevaColumna = columnaActual + movColumnas
                
                ######################################################
                # Ahora analizaremos si el movimiento era válido o no.
                if nuevaFila < 0 or nuevaFila >= n or nuevaColumna < 0 or nuevaColumna >= m: # Aquí corroboramos que no nos estamos saliendo de la matriz "laberinto"
                    print("Movimiento inválido!")
                elif laberinto[nuevaFila][nuevaColumna] == 1: # PARED. Movimiento inválido.
                    print("Movimiento inválido! (había una pared)")
                else:
                    ######################################################
                    # Ahora analizamos los casos de movimientos válidos
                    
                    if laberinto[nuevaFila][nuevaColumna] == 8: # QUESO. Captura el queso.
                        print("Queso capturado!")
                        quesosCapturados+=1
                    elif laberinto[nuevaFila][nuevaColumna] == 5: # SALIDA.
                        ratonSalio = True # Una vez el ratón sale no hay que seguir leyendo el archivo.
                    

                    ######################################################
                    # Se procede a marcar el movimiento en el laberinto
                    laberinto[filaActual][columnaActual] = 2 #Dejar huellas

                    filaActual = nuevaFila # Actualizar fila
                    columnaActual = nuevaColumna # Actualizar columna

                    laberinto[filaActual][columnaActual] = 6 # Actualizamos posicion del ratón en el laberinto.
                    
                    print(laberinto) # Finalmente imprimimos el laberinto
                    separacion()
                    
                movimiento = expTxt.readline().strip() # Leemos siguiente movimiento
            separacion()
            print("FIN DEL EXPERIMENTO")
            separacion()
            ######################################################
            #Ahora que terminamos de mover al ratón, hay que informar quesos capturados y si el ratón salió del laberinto o no.
            print("El ratón capturó ", quesosCapturados, " de ", cantidadQuesos, " totales.")
            if ratonSalio:
                print("El ratón logró salir del laberinto!")
            else:
                print("El ratón no logró salir del laberinto...")
            separacion()

    ######################################################
    # Finalmente hay que preguntar al usuario si desea seguir consultando por experimentos
    respuesta = -1
    while respuesta == -1: 
        respuesta = int(input("Desea consultar otro experimento? [0] NO, [1] Si"))
        if respuesta != 1 and respuesta != 0:
            print("Opción inválida!")
        if respuesta == 0:
            seguir = False
            print("Adiós!")

######################################################
######################################################