import re
from LinkedList import LinkedList

palabrasReservadas = ["funct", "var", "ent", "cad", "flot", "bool", "verdadero", "falso", "const", "si", "o", "entonces", "para", "en rango", "mostrar", "escribir"]


# Clean code.

def removeExtras(file):

    # Delete end of line.

    splitText = file.split("\n\n")

    cleanText = []

    # Delete spaces.

    for line in splitText:

        cleanText.append(line.strip())

    # Delete comments.

    for line in cleanText:

        # Search and select the comment and remove it.

        if(re.search("^//", line)):

            cleanText.remove(line)

    return cleanText

def preProcesator():

    # Validate if the archive exist.

    try:

        file = open("example.txt", "r")

        file = str(file.read())

        # Delete comments.

        plainText = removeExtras(file)

        # Create the new file.

        newFileName = "out.txt"

        newFile = open(newFileName, "w")

        for line in plainText:

            newFile.write(line)

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

    #fileName = preProcesator()

    #readFile(fileName)
    
    lista = LinkedList()

    lista.add(1)
    lista.add(2)
    lista.add(3)

    lista.print()
