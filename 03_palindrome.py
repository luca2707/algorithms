# Exemple 3 : Tableau de palindromes
# Étant donné un tableau de chaînes de caractères, créer un algorithme qui retourne un tableau
# de ces mêmes chaînes, de telle sorte que les lettres des chaînes de caractères soient un palindrome.
# Traiter le cas, où une chaîne n’a pas de palindrome.
#
# palindrome: adjectif et nom masculin.
# Se dit d'un mot, d'un vers, d'une phrase que l'on peut lire indifféremment de gauche à droite
# ou de droite à gauche. (Exemple : le mot ressasser ou la phrase Ésope reste ici et se repose.)

from sys import argv

def computePalindrome(input_string: str) -> str:
    # Scan the input string, character by character.
    # Throw away all non alphabetical characters like white space, punctuations and special characters.
    # Convert all characters to lower case.
    # Each non-white-space character is stored in into a map, the key being the character,
    # the value being the numbre of occurences encountered so far.
    map = dict()
    for i in range(len(input_string)):
        newchar = input_string[i]
        # Ignore non-alphabetic characters
        if not newchar.isalpha():
            continue
        # Convert character to lower case
        newchar = newchar.lower()
        counter = 1
        if newchar in map:
            # This character is already present => increment the value by the occurences found previously
            counter += map[newchar]
        map[newchar] = counter

    # iterate through the map and start assembling the palindrome
    uneven_character_counter = 0
    left_list = list()
    right_list = list()
    for (char, counter) in map.items():
        if counter%2 == 0:
            # Even number of occurences => append to both lists
            repetitions = counter // 2
            left_list.insert(0, repetitions * char)
            right_list.append(repetitions * char)
        else:
            # Uneven number of occurences => check if it is the first one
            if uneven_character_counter == 0:
                # First character with uneven number of occurences => append to the end of the left_list
                # (where it will become the center of the palindrome)
                uneven_character_counter += 1
                left_list.append(counter * char)
            else:
                # This is already the second character that occurs an uneven number of times
                # => this character string is NOT a palindrome => stop processing.
                return "NO PALINDROME FOUND";
    # The palindrome is obtained by concatenating all elements in the left list and all those in the right list
    return "".join(left_list + right_list)

if len(argv) >= 2:
    input_string = argv[1]
else:
    input_string = input("Please input the string that you want to transform into a palindrome: ")

print("Computing a palindrome for the string: {} ...".format(input_string))
print("Result: {}".format(computePalindrome(input_string)))

# Table of palindromes
palindrome_list = list()
palindrome_list.append("A nut for a jar of tuna.")
palindrome_list.append("Al lets Della call Ed \“Stella.\”")
palindrome_list.append("Amore, Roma.")
palindrome_list.append("Are we not pure? \"No, sir!\" Panama's moody Noriega brags. \"It is garbage!\" Irony dooms a man—a prisoner up to new era.")
palindrome_list.append("Borrow or rob?")
palindrome_list.append("King, are you glad you are king?")
palindrome_list.append("Taco cat")
palindrome_list.append("Was it a car or a cat I saw?")
palindrome_list.append("Dennis, Nell, Edna, Leon, Nedra, Anita, Rolf, Nora, Alice, Carol, Leo, Jane, Reed, Dena, Dale, Basil, Rae, Penny, Lana, Dave, Denny, Lena, Ida, Bernadette, Ben, Ray, Lila, Nina, Jo, Ira, Mara, Sara, Mario, Jan, Ina, Lily, Arne, Bette, Dan, Reba, Diane, Lynn, Ed, Eva, Dana, Lynne, Pearl, Isabel, Ada, Ned, Dee, Rena, Joel, Lora, Cecil, Aaron, Flora, Tina, Arden, Noel, and Ellen sinned.")
palindrome_list.append("Ed, I saw Harpo Marx ram Oprah W. aside.")
palindrome_list.append("The quick brown fox jumps over the lazy dog")
palindrome_list.append("How vexingly quick daft zebras jump!")
palindrome_list.append("Waltz, bad nymph, for quick jigs vex.")
palindrome_list.append("saippuakivikauppias")
palindrome_list.append("detartrated")
palindrome_list.append("ressasser")
palindrome_list.append("Esope reste ici et se repose.")
palindrome_list.append("Doc, note: I dissent. A fast never prevents a fatness. I diet on cod")


result_list = list()
for s in palindrome_list:
    result_list.append(computePalindrome(s))
    print("______________________________________________________________________")
    print("Computing palindrome for {} ...".format(s))
    print("Result: {}.".format(computePalindrome(s)))