"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01(): 
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    suma = 0
    with open('data.csv', 'r') as archivo:
        # Leer líneas del archivo
        lineas = archivo.readlines()
        # Iterar sobre cada línea
        for linea in lineas:
            columns = linea.split('\t')
            suma += int(columns[1])
      
    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    with open('data.csv', 'r') as file:
        lines = file.readlines()

    # Inicializar un diccionario para contar la cantidad de registros por letra
    registro_por_letra = {}

    # Iterar sobre cada línea del archivo
    for line in lines:
        # Separar los campos por tabulaciones
        campos = line.strip().split('\t')
        # Obtener la letra en la primera columna
        letra = campos[0]
        # Incrementar el contador para esta letra
        if letra in registro_por_letra:
            registro_por_letra[letra] += 1
        else:
            registro_por_letra[letra] = 1

    # Convertir el diccionario en una lista de tuplas y ordenarla alfabéticamente
    registros_ordenados = sorted(registro_por_letra.items())
    return registros_ordenados


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    with open('data.csv', 'r') as file:
        lines = file.readlines()

    # Inicializar un diccionario para almacenar la suma de la columna 2 por letra
    suma_por_letra = {}

    # Iterar sobre cada línea del archivo
    for line in lines:
        # Separar los campos por tabulaciones
        campos = line.strip().split('\t')
        # Obtener la letra en la primera columna y el número en la segunda columna
        letra = campos[0]
        numero = int(campos[1])
        # Sumar el número a la suma correspondiente a esta letra
        if letra in suma_por_letra:
            suma_por_letra[letra] += numero
        else:
            suma_por_letra[letra] = numero

    # Convertir el diccionario en una lista de tuplas y ordenarla alfabéticamente
    suma_ordenada = sorted(suma_por_letra.items())

    return suma_ordenada



def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    with open('data.csv', 'r') as file:
        lines = file.readlines()

    # Inicializar un diccionario para almacenar la cantidad de registros por mes
    registros_por_mes = {}

    # Iterar sobre cada línea del archivo
    for line in lines:
        # Separar los campos por tabulaciones
        campos = line.strip().split('\t')
        # Obtener la fecha en la tercera columna y extraer el mes
        fecha = campos[2]
        mes = fecha.split('-')[1]
        # Incrementar el contador para este mes
        if mes in registros_por_mes:
            registros_por_mes[mes] += 1
        else:
            registros_por_mes[mes] = 1

    # Convertir el diccionario en una lista de tuplas y ordenarla por mes
    registros_ordenados = sorted(registros_por_mes.items())

    return registros_ordenados


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    with open('data.csv', 'r') as file:
        lines = file.readlines()

    # Inicializar un diccionario para almacenar el valor máximo y mínimo de la columna 2 por letra
    max_min_por_letra = {}

    # Iterar sobre cada línea del archivo
    for line in lines:
        # Separar los campos por tabulaciones
        campos = line.strip().split('\t')
        # Obtener la letra en la primera columna y el número en la segunda columna
        letra = campos[0]
        numero = int(campos[1])
        # Actualizar los valores máximo y mínimo para esta letra
        if letra in max_min_por_letra:
            max_min_por_letra[letra] = (
                max(max_min_por_letra[letra][0], numero),
                min(max_min_por_letra[letra][1], numero)
            )
        else:
            max_min_por_letra[letra] = (numero, numero)

    # Convertir el diccionario en una lista de tuplas
    max_min_lista = [(letra, max_min[0], max_min[1]) for letra, max_min in max_min_por_letra.items()]
    max_min_lista = sorted(max_min_lista)
    return max_min_lista


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    min_max_por_clave = {}

    # Abrir el archivo y leer las líneas
    with open('data.csv', 'r') as file:
        lines = file.readlines()

    # Iterar sobre cada línea del archivo
    for line in lines:
        # Separar los campos por tabulaciones
        campos = line.strip().split('\t')
        # Obtener el diccionario de la columna 5 y dividirlo en pares clave-valor
        diccionario = campos[4].split(',')
        for elemento in diccionario:
            clave, valor = elemento.split(':')
            valor = int(valor)
            # Actualizar los valores mínimos y máximos para esta clave
            if clave in min_max_por_clave:
                min_max_por_clave[clave] = (
                    min(min_max_por_clave[clave][0], valor),
                    max(min_max_por_clave[clave][1], valor)
                )
            else:
                min_max_por_clave[clave] = (valor, valor)

    # Convertir el diccionario en una lista de tuplas
    min_max_lista = [(clave, min_max[0], min_max[1]) for clave, min_max in min_max_por_clave.items()]
    min_max_lista = sorted(min_max_lista)
    return min_max_lista


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    letras_por_valor = {}
    with open('data.csv', 'r') as file:
        lines = file.readlines()

    # Iterar sobre cada línea del archivo
    for line in lines:
        # Separar los campos por tabulaciones
        campos = line.strip().split('\t')
        # Obtener el valor de la columna 2 y la letra de la columna 1
        valor_columna2 = int(campos[1])
        letra_columna1 = campos[0]
        # Agregar la letra a la lista asociada al valor de la columna 2
        if valor_columna2 in letras_por_valor:
            letras_por_valor[valor_columna2].append(letra_columna1)
        else:
            letras_por_valor[valor_columna2] = [letra_columna1]

    # Convertir el diccionario en una lista de tuplas
    asociaciones = [(valor, letras) for valor, letras in letras_por_valor.items()]
    

    return sorted(asociaciones)



def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    letras_por_valor = {}
    with open('data.csv', 'r') as file:
        lines = file.readlines()

    for line in lines:
        # Separar los campos por tabulaciones
        campos = line.strip().split('\t')
        # Obtener el valor de la columna 2 y la letra de la columna 1
        valor_columna2 = int(campos[1])
        letra_columna1 = campos[0]
        # Agregar la letra a la lista asociada al valor de la columna 2
        if valor_columna2 in letras_por_valor:
            letras_por_valor[valor_columna2].append(letra_columna1)
        else:
            letras_por_valor[valor_columna2] = [letra_columna1]

    # Ordenar y eliminar repeticiones de letras en cada lista asociada a un valor de la columna 2
    for valor in letras_por_valor:
        letras_por_valor[valor] = sorted(set(letras_por_valor[valor]))

    # Convertir el diccionario en una lista de tuplas
    lista_tuplas = [(valor, letras) for valor, letras in letras_por_valor.items()]

    return sorted(lista_tuplas)

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    conteo_por_clave = {}
    with open('data.csv', 'r') as file:
        lines = file.readlines()
    for line in lines:
        # Separar los campos por tabulaciones
        campos = line.strip().split('\t')
        # Obtener el diccionario de la columna 5 y dividirlo en pares clave-valor
        diccionario = campos[4].split(',')
        for elemento in diccionario:
            clave, _ = elemento.split(':')
            # Incrementar el contador para esta clave
            if clave in conteo_por_clave:
                conteo_por_clave[clave] += 1
            else:
                conteo_por_clave[clave] = 1

    return conteo_por_clave
#print(pregunta_09())

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista_tuplas = []
    with open('data.csv', 'r') as file:
        lines = file.readlines()
    for line in lines:
        # Separar los campos por tabulaciones
        campos = line.strip().split('\t')
        # Obtener la letra de la columna 1 y contar los elementos de las columnas 4 y 5
        letra_columna1 = campos[0]
        elementos_columna4 = len(campos[3].split(','))
        elementos_columna5 = len(campos[4].split(','))
        # Agregar la tupla a la lista
        lista_tuplas.append((letra_columna1, elementos_columna4, elementos_columna5))

    return lista_tuplas

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    suma_por_letra = {}

    # Abrir el archivo y leer las líneas
    with open('data.csv', 'r') as file:
        lines = file.readlines()

    # Iterar sobre cada línea del archivo
    for line in lines:
        # Separar los campos por tabulaciones
        campos = line.strip().split('\t')
        # Obtener la columna 2 y la columna 4
        columna2 = int(campos[1])
        columna4 = campos[3].split(',')
        # Iterar sobre cada letra en la columna 4 y sumar la columna 2 correspondiente
        for letra in columna4:
            # Incrementar la suma para esta letra
            if letra in suma_por_letra:
                suma_por_letra[letra] += columna2
            else:
                suma_por_letra[letra] = columna2

    # Ordenar el diccionario alfabéticamente por clave
    suma_por_letra_ordenada = {k: suma_por_letra[k] for k in sorted(suma_por_letra)}

    return suma_por_letra_ordenada


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    suma_por_letra = {}

    # Abrir el archivo y leer las líneas
    with open('data.csv', 'r') as file:
        lines = file.readlines()

    # Iterar sobre cada línea del archivo
    for line in lines:
        # Separar los campos por tabulaciones
        campos = line.strip().split('\t')
        # Obtener la letra de la columna 1 y la columna 5
        letra_columna1 = campos[0]
        columna5 = campos[4].split(',')
        # Iterar sobre cada elemento en la columna 5 y sumarlo para esta letra
        for elemento in columna5:
            _, valor = elemento.split(':')
            valor = int(valor)
            # Incrementar la suma para esta letra
            if letra_columna1 in suma_por_letra:
                suma_por_letra[letra_columna1] += valor
            else:
                suma_por_letra[letra_columna1] = valor

    return suma_por_letra
