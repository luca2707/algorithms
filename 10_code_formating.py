# Exemple 10 : Formatage
# Voici une portion de code non formatée, trouves un algorithme qui permet de respecter
# les règles de formatage :

# Lisp
# (defun fib (n) “Fibonacci” (if (< n 2) n (+ (fib (- n 1)) (fib (- n 2)))))

# Javascript
# function Fibonacci(n) { var w; if(n <= 0) return 0; if(n == 1) return 1; var u = 0; var v = 1;
# for(var i=2; i <= n; i++) { w = u+v; u = v; v = w; }; return v; }

# First Idea (for Javascript):
# In Javascript:
# - blocks are easily identified because they are enclosed in { ... }
# - simple statements end with ;
# 
# Assume input is a string that contains the source code extract.
# Define an integer that represents the number of spaces in an indent, for example:
# indent = 3
# Another integer is used to keep track of the current indentation level.
# indent_level = 0
# Create an empty list that will contain strings.
# Start scanning through the input string character by character.
# If character is 
#  - ";"" => add ";\n" to the output
#            and add indent_level * default_indent space characters to the output
#  - "{"  => add "{\n" to the output,
#            increment the current indentation level by one,
#            and add indent_level * default_indent space characters to the output
#  - "}" => add "\n" to the output
#           decrement indent_level by one
#           add indent_level * default_indent space to the output
#           add "}\n" to the ouput
# When the end of the input string is reached, just convert the list into a string (using join).

# Issue: the for loop requires special treatment, it should stay on one line.
# Implement a special rule for the simple brackets: while we are inside brackets, ignore the ; marking the end of a statement.
# Introduce the backet level to keep track.
# Issue: white spaces after the semi-column or barkets are being pushed to the next line.
# They should be ignored instead.
# => maintain a boolean that will ignore or not the whitespaces.

import unittest

class TestJavaFormat(unittest.TestCase):

    def test_java_format(self):
        input_str = """function Fibonacci(n) { var w; if(n <= 0) return 0; if(n == 1) return 1; var u = 0; var v = 1; for(var i=2; i <= n; i++) { w = u+v; u = v; v = w; } return v; }"""
        expected = """function Fibonacci (n) {
    var w;
    if (n <= 0) return 0;
    if (n == 1) return 1;
    var u = 0;
    var v = 1;
    for (var i=2; i <= n; i++) {
        w = u+v;
        u = v;
        v = w;
    }
    return v;
}
"""
        self.assertEqual(java_format(input_str, 4), expected)

class TestLispFormat(unittest.TestCase):

    # Usual Lisp formatting is like this:
    # (do-something first-argument
    #               second-argument
    #               #'(lambda (x) (frob x))
    #               fourth-argument
    #               last-argument)
    def test_lisp_format(self):
        input_str = "(defun fib (n) \"Fibonacci\" (if (< n 2) n (+ (fib (- n 1)) (fib (- n 2)))))"
        expected = """(defun fib
       (n)
       "Fibonacci"
       (if (< n
              2)
           n
           (+ (fib (- n
                      1))
              (fib (- n
                      2)))))"""
        self.assertEqual(lisp_format(input_str), expected)

def lisp_format(input_str: str) -> str:
    print("Unformated LISP:")
    print(input_str)
    print("____________________________________")
    formated = list()
    arg_count = dict()
    func_nest_level = 0
    cur_pos = 0
    indent_pos = dict()
    for i in range(len(input_str)):
        input_char =  input_str[i]
        match input_char:
            case '(':
                # Start of a new function
                func_nest_level += 1
                arg_count[func_nest_level] = 0
                indent_pos[func_nest_level] = 0
                formated.append("(")
                cur_pos += 1
            case ')':
                # End of the function
                arg_count.pop(func_nest_level)
                indent_pos.pop(func_nest_level)
                func_nest_level -= 1
                formated.append(")")
                cur_pos += 1
            case ' ':
                # a word just ended
                if func_nest_level > 0:
                    # We are inside a function
                    arg_count[func_nest_level] += 1
                    if arg_count[func_nest_level] == 1:
                        # Function name just ended => append ' '
                        formated.append(' ')
                        cur_pos += 1
                        indent_pos[func_nest_level] = cur_pos
                    if arg_count[func_nest_level] >= 2:
                        # Function argument just ended => go to the next line and indent with spaces
                        formated.append('\n')
                        formated.append(' ' * indent_pos[func_nest_level])
                        cur_pos = indent_pos[func_nest_level]
                else:
                    # We are not inside a function
                    # Should never happen
                    formated.append('_')
                    cur_pos += 1
            case _:
                # We are somewhere is a word => just append the character
                formated.append(input_char)
                cur_pos += 1
    formated_str = "".join(formated)
    print("Formated LISP:")
    print(formated_str)
    print("____________________________________")
    return formated_str

def java_format(input_str: str, indent: int = 3) -> str:
    print("Unformated java:")
    print(input_str)
    print("____________________________________")
    formated = list()
    indent_level = 0
    bracket_level = 0
    ignore_space = False
    for i in range(len(input_str)):
        input_char =  input_str[i]
        match input_char:
            case '(':
                ignore_space = False
                bracket_level += 1
                formated.append(" (")
            case ')':
                ignore_space = False
                bracket_level -= 1
                formated.append(")")
            case ';':
                formated.append(";")
                if (bracket_level <= 0):
                    ignore_space = True
                    formated.append("\n")
                    formated.append(' ' * indent * indent_level)
            case '{':
                ignore_space = True
                formated.append("{\n")
                indent_level += 1
                formated.append(' ' * indent * indent_level)
            case '}':
                ignore_space = True
                indent_level -= 1
                formated.pop()
                formated.append(' ' * indent * indent_level)
                formated.append("}\n")
                formated.append(' ' * indent * indent_level)
            case ' ':
                if not ignore_space:
                    formated.append(' ')
            case _:
                ignore_space = False
                formated.append(input_char)
    formated_str = "".join(formated)
    print("Formated java:")
    print(formated_str)
    print("____________________________________")
    return formated_str

if __name__ == "__main__":
    unittest.main()




