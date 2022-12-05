# Exemple 1 : Tail
# Tail est une commande UNIX qui permet d’afficher les x dernières lignes de texte d’un fichier.
# Trouve un algorithme qui permet de coder cette fonctionnalité.
# 
# This program implements a simple 'tail' command as in linux.
# The program takes 2 arguments:
# First argument is 'filename', the name of a text file.
# Second argument is nblines, the number of lines that you want the program to output.
# The program will output the last 'nblines' of the file.

from sys import argv

# Define a FIFO buffer class
class FifoBuffer():
    
    max_size: int
    lines = list()

    def __init__(self, max_size = 10) -> None:
        self.max_size = max_size

    def add(self, newline: str):
        if len(self.lines) >= self.max_size:
            # Fifo buffer is full => remove the first element before adding the new one
            self.lines.pop(0)
        self.lines.append(newline)

    def get(self, index: int) -> str:
        return self.lines[index]

    def get_size(self) -> int:
        return len(self.lines)

# 1. Get the filename:
if len(argv) >= 2:
    filename = argv[1]
else:
    filename = input("Please enter the name of the file: ")
print("Will tail file '{}'.".format(filename))

# 2. Get the number of lines to tail
nblines = 10
if len(argv) >= 3:
    strInput = argv[2]
else:
    strInput = input("How many lines do you want to tail? (default is 10): ")
if len(strInput) > 0:
    nblines = int(strInput)
print("Will print the last {} lines of file '{}'.".format(nblines, filename))

# Create a FIFO buffer of strings to hold the lines read from the file.
# The list will contain maximum 'nblines' elements
buffer = FifoBuffer(nblines)

# Open the file (by default readonly in text more)
with open(filename, encoding="utf-8") as f:
    line_counter = 0
    newline = f.readline()
    while newline != "":
        line_counter += 1
        buffer.add(newline)
        newline = f.readline()
    else:
        print("Reached end of file after reading {} lines.".format(line_counter))

# The end of file has been reached => the FIFO buffer contains the 'nblines' last lines of the file
# We just need to print them.
for i in range(buffer.get_size()):
    print("{}: {}".format(i + 1, buffer.get(i)), end="")
