# Exemple 4 : Caractères distincts
# Dans une chaîne, détecter la plus longue chaîne de caractères composée de caractères distincts.
# Par exemple : “abcdemo” est la plus longue chaîne de caractères distincts de “abcdemoderneancien”

from sys import argv

if len(argv) >= 2:
    input_string = argv[1]
else:
    input_string = input("Please input a string not containing white space: ")

# A 'distinct' string is a string that contains only distinct characters, i.e. none of the characters
# in the string repeat themselves.

if len(input_string) < 2:
    print("Longest distinct string contained in '{}' is {}".format(input_string, input_string))

# The following variables will store the coordinates of all the longest 'distinct' string
# that is found in the input_string.
# max_start will hold the start index of the distinct string
# max_length will hold the length of the distinct string.
max_start = 0
max_length = 0

# The following map will be used to store all the characters that are encountered while scanning the input
# string. We insert the scanned characters one by one, until we find a duplicate.
# Each entry in the map contains the scanned character (key) and its position in the string (value)
distinct_characters = dict()

# Start scanning
start_index = 0
scan_index = 0
while scan_index < len(input_string):
    scanned_char = input_string[scan_index]
    if scanned_char not in distinct_characters:
        # Scanned character is not yet in the 'distinct' set => add it to the map, then scan the next character
        distinct_characters[scanned_char] = scan_index
        print("Found distinct character {} in position {}.".format(scanned_char, scan_index))
        scan_index += 1
    else:
        print("Found duplicate character {} in position {}.".format(scanned_char, scan_index))
        # Scanned character is already in the 'distinct' set => found a duplicate
        # => this is the end of the current 'distinct' string.
        # The length of this distinct string is equals to the number of characters in the set
        # If this length is > max_length, then record the length and start pointer of the current distinct string
        new_length = len(distinct_characters)
        print("Found new distinct string with length={}, start_index={}: {}".format(new_length, start_index, input_string[start_index:start_index + new_length]))
        if new_length > max_length:
            max_length = new_length
            max_start = start_index
            print("Longest distinct string has been found with length={} starting at position {}.".format(max_length, max_start))
        else:
            print("Distinct string discarded because not longer than the previous ones.")
        # We have to restart scanning at the position just after the first occurence of the duplicated character
        # We get the index of the first occurence of the duplicated character from the map.
        start_index = distinct_characters[scanned_char] + 1
        scan_index = start_index
        distinct_characters.clear()
        print("Restarting scanning at position {}.".format(start_index))
# Scanned until the end of the input string
# Printing the longest distinct string
print("The longest distinct string has length={} and starts at index={}: {}".format(max_length, max_start, input_string[max_start:max_start + max_length]))

# Other example input strings:
# "Weareallinthegutter,butsomeofusarelookingatthestars."
# "We are all in the gutter, but some of us are looking at the stars."
# "I must not fear. Fear is the mind-killer. Fear is the little-death that brings total obliteration. I will face my fear. I will permit it to pass over me and through me. And when it has gone past I will turn the inner eye to see its path. Where the fear has gone there will be nothing. Only I will remain."
# "Imustnotfear.Fearisthemind-killer.Fearisthelittle-deaththatbringstotalobliteration.Iwillfacemyfear.Iwillpermitittopassovermeandthroughme.AndwhenithasgonepastIwillturntheinnereyetoseeitspath.Wherethefearhasgonetherewillbenothing.OnlyIwillremain."
# "Thequickbrownfoxjumpsoverthelazydog"
# "Howvexinglyquickdaftzebrasjump!"
# "Waltz,badnymph,forquickjigsvex."
# "iudashfpoewrzumnbvyjhgxdgflasdfkjhqwertzuiopasdfghjklyxcvbnmjasdhflkshdfhasqpwkjasdgnbxcvdfkjhasdf"