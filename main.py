import re


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

        print(plainText)

    except:

        print('No data')

# Print each char in the text file.


# Main function.

if __name__ == "__main__":

    preProcesator()