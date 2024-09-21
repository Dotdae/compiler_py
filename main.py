import re
from LinkedList import LinkedList

palabrasReservadas = ["funct", "var", "ent", "cad", "flot", "bool", "verdadero", "falso", "const", "si", "o", "entonces", "para", "en rango", "mostrar", "escribir"]

def tokenizeCode(fileName):

    try:

        source = open(fileName, "r")
        source = source.read()

    except FileExistsError:

        print(f"El archivo {fileName} no se encontró")
        return []
    
    # Regex to mostrar.
    # \b is to limit the word to mostrar, we use the function compile to convert
    # the regex into a object to make searches.

    regexMostrar = re.compile(r'\bmostrar\b')
    
    # Tokenizar el resto del código ignorando el contenido de 'mostrar(...)'
    
    tokens = []

    # Flag see the actual position in the line.

    i = 0

    while i < len(source):

        # Search the word starts in the position 0 and return match object.

        match = regexMostrar.search(source, i)

        if match:

            # Extract the part of the code starting in i position.
            # The regex \b\w+\b|\S can we explaneid for each element:
            # \b is the limit to search complete words.
            # \w is to search chars (A-Z)(a-z)(0-9)(_) and the + is for one or more.
            # \b again is for the end of the word.
            # | es the 'OR' in the regex
            # \S is for search each char that there is not a white space ( ), (\t) (\n)
            # This regex is for search complete words and individual chars like =, (), ; using the \S flag.


            tokens.extend(re.findall(r'\b\w+\b|\S', source[i:match.start()]))
            
            # Add 'mostrar' as an token

            tokens.append('mostrar')

            #  Skip the text inside 'mostrar(...)'

            i = source.find(')', match.end()) + 1

        else:

            # Si no hay más 'mostrar', tokenizar el resto del código

            tokens.extend(re.findall(r'\b\w+\b|\S', source[i:]))
            break

    return tokens


def isReservedWord(tokens):
    
    for token in tokens:

        if token in palabrasReservadas:

            print(f'{token} is a reserved word!')

def preProcesator():

    # Validate if the archive exist.

    try:

        file = open("example.txt", "r")
        noComment = ''

        # Delete comments.

        for line in file:

            noComment = noComment + line.split('//')[0]


        # Create the new file.

        newFileName = "out.txt"

        newFile = open(newFileName, "w")

        # Delete white spaces.

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


# Main function.

if __name__ == "__main__":

    fileName = preProcesator()

    tokens = tokenizeCode(fileName)

    print('Token list')

    for token in tokens:

        print(f"Token -> {token}")
    
    isReservedWord(tokens)


    #readFile(fileName)
    

