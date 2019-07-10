# Problema: Laberinto del ratón

Se ha armado un experimento en el que se ingresan ratones en diversos laberintos. Los laberintos tienen una o más salidas, y en ellos se colocan trozos de queso que los ratones deben encontrar. Junto con esto, se ha colocado un sensor encima del laberinto que va registrando los movimientos que realiza el ratón dentro del laberinto en el que fue ingresado.

Con este experimento se desea registrar los movimientos de diversos ratones (ratones no entrenados, ratones entrenados para encontrar la salida y ratones entrenados para encontrar el queso) y determinar la capacidad de orientación espacial de los distintos grupos.

Para ello, el sensor registra tanto el laberinto usado como cada movimiento del ratón dentro del laberinto durante 10 minutos. Los archivos donde se guardan los movimientos del ratón tienen de nombre “exp**n**.txt” (n siendo un número). La estructura de los archivos exp**n**.txt es: En la primera línea está escrito el nombre del archivo que contiene el laberinto en el que se puso al ratón (más adelante se explica la estructura de los archivos de los laberintos), en la segunda línea debe haber un par de números (i,j) que representan la ubicación inicial (fila, columna) en la que el ratón fue dejado dentro del laberinto. Luego, cada línea siguiente tiene una letra que representa movimientos que va haciendo el ratón, las letras significan lo siguiente:

    U : El ratón se movió hacia arriba (up)

    D : El ratón se movió hacia abajo (down)

    L : El ratón se movió hacia la izquierda (left)

    R : El ratón se movió hacia la derecha (right)

Por otro lado, los archivos de los laberintos tienen el siguiente formato: la primera línea tiene dos números escritos como n,m  donde n es el largo del laberinto y m el ancho (como la cantidad de filas y columnas de una matriz), luego por cada línea siguiente se encuentra una lista de “m” letras separadas por comas que representan distintas cosas:

    P : Significa que esa posición del laberinto es una pared

    “ “ (espacio): Significa que esa posición del laberinto es un espacio vacío por el que el ratón puede transitar.

    Q : Significa que en esa posición hay un queso.

    S : Significa que en esa posición hay una salida del laberinto.

Usted debe escribir un programa que realice las siguientes tareas:

* Primero debe leer el archivo “experimentos.txt” que contiene los nombres de todos los archivos de los experimentos que se realizaron, dichos nombres deben ser guardados en una lista.

* Luego debe preguntar indefinidas veces (hasta que el usuario ya no quiera seguir preguntando) qué experimento desea consultar. Para ello se debe desplegar hacia abajo la lista de archivos de experimentos (digamos que de largo “ñ”), y se debe ingresar un número entre 0 y ñ-1 para escoger el archivo a leer.

* Una vez que se ha seleccionado el experimento que se debe consultar, abrir el archivo del experimento y leer la primera línea con el nombre del archivo del laberinto. El laberinto debe ser abierto como un nuevo archivo y guardado en una matriz, donde las paredes se representan con el número “1”, las salidas con el número “5”, los quesos con el número “8” y los espacios vacíos por los que se puede transitar se deben representar con el número “0”.
Debe considerar que si el laberinto no tiene salidas, el experimento no es válido. Por lo tanto si no se encontraron salidas en el laberinto, debe detener el programa, imprimir “Laberinto no válido” y saltarse al último punto de esta lista.

* Luego debe continuar con la lectura del archivo del experimento y leer la ubicación inicial del ratón, la cual debe ser marcada con el número “6” en la matriz.

* Luego debe imprimir el laberinto tal cual está en este momento (sin movimientos y con el ratón ubicado en su posición inicial). A continuación el usuario debe ir presionando enter: Por cada enter que presiona se lee un movimiento que el ratón realizó y se vuelve a imprimir la matriz con los cambios luego del movimiento. Para ello debe considerar lo siguiente:

  * Si el ratón se mueve hacia una posición que está libre, se considera un movimiento válido y el ratón debe moverse a esa posición (mover el 6 a esa posición), mientras que la posición previa en la que estaba el ratón debe marcarse con un 2.

  * A medida que el ratón se va moviendo va a dejar las posiciones por las que caminó marcadas con un 2, como si estuviese dejando huellas.

  * Si el ratón se mueve hacia una posición donde había una pared, se debe imprimir “movimiento inválido” y no realizar ningún movimiento.

  * Si el ratón se mueve hacia una posición donde había un queso, se debe imprimir “Queso capturado!”.

  * Si el ratón se mueve hasta estar encima de una salida (5), se debe imprimir “El ratón salió del laberinto”. Las salidas de los laberintos no tienen vuelta atrás, por lo tanto a partir de aquí se debe parar la lectura del archivo. Debe considerar que puede que el ratón nunca encuentre la salida al laberinto.

* Luego de mostrar todos los pasos del ratón, se debe informar: Cuántos quesos capturó el ratón comparados con la cantidad total de quesos que tenía el laberinto, y si logró salir del laberinto.

* Finalmente se debe preguntar al usuario si desea revisar otro experimento o no.

Para que su programa funcione correctamente debe ubicarse en la carpeta “mouse_maze”. ¡Suerte ratoncitos!

## Resultados que se debe obtener de cada archivo:

exp1.txt →
```
Recoge 1 de 1 quesos.
Logra salir del laberinto.
Algunos movimientos que realiza el ratón son inválidos.
```

exp2.txt →
```
Laberinto no válido (no tiene salidas).
```

exp3.txt →
```
Recoge 0 de 3 quesos.
Logra salir del laberinto.
Algunos movimientos que realiza el ratón son inválidos.
```

exp4.txt →
```
3 de 3 quesos capturados.
No logra salir del laberinto.
No existen movimientos inválidos.
```

exp5.txt →
```
2 de 3 quesos capturados.
Logra salir del laberinto.
No existen movimientos inválidos.
```
