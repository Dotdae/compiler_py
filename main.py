import re
from LinkedList import LinkedList

palabrasReservadas = ["funct", "var", "ent", "cad", "flot", "bool", "verdadero", "falso", "const", "si", "o", "entonces", "para", "en rango", "mostrar", "escribir"]
operadores = ['+', '-', '*', '/', '=', '<', '>', ':=', ':', '==', '!=', '+=', '-=', '*=', '/=']
simbolosEspeciales = ['(', ')', '{', '}', '[', ']', ',', '"']

# Función que tokeniza el código, recibe como parámetro el archivo.

def tokenizeCode(fileName):

    # Abre el archivo.

    try:
        source = open(fileName, "r").read()

    except FileExistsError:

        print(f"El archivo {fileName} no se encontró")

        return []

    # Lista donde se guardaran los tokens

    tokens = []
    
    '''
        Variables para identificar el número de línea y columna
        comienza en 1 porque el archivo comienza en 1.
        La variable i funciona como un puntero para ver la posición en el archivo.
    '''

    line_number = 1
    column_number = 1
    i = 0

    while i < len(source):

        char = source[i]

        # Si se encuentra un salto de línea, aumentamos el número de línea y reiniciamos la columna.

        if source[i] == '\n':

            line_number += 1
            column_number = 1
            i += 1

            continue
        
        # Extraemos el token usando expresiones regulares.
        # \b es el limite para buscar una palabra que contenga caracterés alfanuméricos antes o después.
        # \w+ es para buscar caracteres de (A-Z)(a-z)(0-9)(_) y el + es para uno o más.
        # | es el operador OR.
        # \S es para buscar cada caracter que no sea un espacio en blanco ( )(\t)(\n)
        # Esta expresión regular busca palabras completas y caracteres individuales como = () ; apoyandose de \S
        # El segundo parámetro es para tomar una subcadena desde el índice i hasta el fin de la cadena. 

        # Manejar el operador := 

        if source[i:i+2] == ':=':

            tokens.append((':=', line_number, column_number))

            # Saltar los dos caracteres y aumentar la columna

            i += 2  
            column_number += 2 

            continue

        # Manejar cadenas entre comillas dobles

        if char == '"':

            # Saltar la comilla de apertura

            i += 1  

            while i < len(source) and source[i] != '"':

                i += 1

            # Solo añadir si se encuentra la comilla de cierre (TB para cadenas.)

            if i < len(source) and source[i] == '"':  

                # Añadir la cadena como un solo token, evitando tokenizar su contenido
                # tokens.append((source[start:i + 1], line_number, column_number, 'Cadena'))  # Agregar un tipo "Cadena"
                # column_number += (i - start + 1)  # Actualizar columna
                # i += 1  # Saltar la comilla de cierre
                continue

         # No tokenizar el contenido de mostrar

        if source.startswith("mostrar", i):

            # Agregar 'mostrar' como un token

            tokens.append(("mostrar", line_number, column_number))

            # Avanzar el índice después de 'mostrar'

            i += len("mostrar")  
            column_number += len("mostrar")
            
            # Verificar si hay un paréntesis abierto

            if i < len(source) and source[i] == '(':

                # Avanzar el índice después del '('

                i += 1  
                column_number += 1

                # Saltar valores dentro de las comillas

                while i < len(source):

                    if source[i] == '"':

                        # Saltar el inicio de la cadena

                        i += 1  
                        column_number += 1

                        # Avanzar hasta el final de la cadena

                        while i < len(source) and source[i] != '"':

                            i += 1
                            column_number += 1

                        if i < len(source):

                            # Saltar el cierre de la cadena

                            i += 1  
                            column_number += 1

                    elif source[i] == ')':
                        
                        # Salir del ciclo si encontramos ')'

                        i += 1  
                        column_number += 1
                        break

                    else:

                        # Si encontramos otro carácter, simplemente avanzamos

                        i += 1
                        column_number += 1
            continue

        match = re.match(r'\b\w+\b|\S', source[i:])

        # Se verífica si encontró un token.

        if match:

            '''
                match.group(0) obtiene el texto que coincide con el patrón de búsquedad.
                La segunda variable es para calcular la longitud del token encontrado.
            '''

            token = match.group(0)
            token_length = len(token)

            # Añadimos el token junto con su posición en el archivo.

            tokens.append((token, line_number, column_number))

            # Actualizamos el índice y el número de columna

            i += token_length
            column_number += token_length

        else:

            '''
                Si no se encuentra un token busca en el siguiente caracter por eso se incrementa i en 1
                y con esto también actualizamos la columna para saltar a la siguiente.
            '''

            i += 1
            column_number += 1

    return tokens

# Automatas.

def isReservedWord(token):

    # Estado inicial.

    automata_state = 0

    for reserved in palabrasReservadas:

        # Verifica si el token es igual a uno en la lista global de palabras reservadas.

        if token == reserved: 

            # Pasa al siguiente estado que sería el de aceptación.

            automata_state = 1 

            break

    # Si se llega al estado de aceptación (1) retornará true, sino, será false.

    return automata_state == 1 

def isIdentifier(token):

    '''
        Verifica que el identificador sea como se especifica:
        * Debe iniciar con un carácter [A-Z][a-z].
        * Debe estar seguido de uno o más caracteres [A-Z][a-z].
        * No puede contener dígitos.
        * No puede contener símbolos especiales.
    '''

    # Estado inicial.

    automata_state = 0

    # Verifica si el token es una cadena entre comillas o un número.

    if (token.startswith('"') and token.endswith('"')) or (token.startswith("'") and token.endswith("'")):

        return False
    
    if token.isdigit():

        return False

    # Recorrer cada carácter el token.

    for char in token:

        if automata_state == 0:

            '''
                El primer carácter debe ser una letra, si lo es, pasa al siguiente estado.
                Si no comienza con una letra regresa false.
            '''


            if char.isalpha():

                automata_state = 1
            
            else:

                return False

           
            '''
                Continua en el siguiente estado comprobando el resto de la cadena.
                Si derecta un carácter inválido regresa false.
            '''

        elif automata_state == 1:
    
            # Sigue comprobando si cada caracter son solo letras.

            if char.isalpha():

                # Permanece en el estado 1.

                continue

            else: 

                return False
            
    # Si se llega al estado de aceptación (1) retornará true, sino, será false.

    return automata_state == 1

def isOperator(token):

    # Estado inicial.

    automata_state = 0

    # Verifica si el token es de longitud 1 o 2 (Para poder incluir :=)

    if len(token) > 2:

        return False
    for char in token:
        if automata_state == 0:  
            # Se comprueba en el estado inicial si es un operador
            if token in operadores:  # Comprobar si el token completo está en la lista de operadores
                automata_state = 1
            else:
                return False
            
        elif automata_state == 1: 
            # Si encuentra un carácter que no es operador regresa false.
            if token not in operadores:  
                return False


    # Regresa true si llega al estado de aceptación.

    return automata_state == 1  

def isSymbol(token):

    # Estado inicial.

    automata_state = 0

    for char in token:

        if automata_state == 0:  

            '''
                Si el carácter está en la lista global de símbolos especiales pasa al estado de aceptación
                si no, regresa false.
            '''

            if char in simbolosEspeciales:

                automata_state = 1

            else:

                return False
            
        elif automata_state == 1:  

            # Verífica que en el estado de aceptación sean solo símbolos.

            return False 
        
    # Regresa true si llega al estado de aceptación.
    
    return automata_state == 1  # Acepta si es un símbolo válido

def identifyToken(token):

    # Se guarda cada token, el token se recibe como una tupla compuesto por (lexema, línea, columna)

    lexema = token[0]  

    # Se comprueba cada token con su respectivo autómata y se le asigna el tipode token.
    
    if isReservedWord(lexema):
        return 'Palabra Reservada'
    elif isIdentifier(lexema):
        return 'Identificador'
    elif isOperator(lexema):
        return 'Operador'
    elif isSymbol(lexema):
        return 'Símbolo Especial'
    else:
        return 'Desconocido'

def preProcesator():
    try:
        file = open("example.txt", "r")
        noComment = ''

        # Eliminar comentarios
        for line in file:
            noComment += line.split('//')[0]

        # Crear el nuevo archivo sin comentarios
        newFileName = "out.txt"
        with open(newFileName, "w") as newFile:
            newFile.write(noComment.rstrip() + '\n')

        return newFileName
    except:
        print('No data')

# Print each char in the text file.

def readFile(fileName):

    try:

        file = open(fileName, "r")

        print("Print each character.")

        for line in file:

            for char in line:

                print(char)

    except:

        print("Unexisted data!")

# Función principal

if __name__ == "__main__":
    
    # Se preprocesa el archivo inicial y se retorna el nombre del nuevo archivo.

    fileName = preProcesator()

    # Se almacenan los tokens.

    tokens = tokenizeCode(fileName)

   # Identificar el tipo de cada token

    tokensTipo = [(token, identifyToken(token), line, column) for token, line, column in tokens]

    # Insertar tokens en la lista enlazada

    linkedList = LinkedList()

    for token in tokens:
        tipo_token = identifyToken(token)

        # Almacena lexema, valor, columna, renglón, tipo de token

        linkedList.add(token[0], token[0], token[2], token[1], tipo_token)

    # Imprime la tabla de tokens.

    linkedList.print()
