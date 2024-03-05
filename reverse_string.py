def reverse_string(input_string):
    stack = []
    reversed_string = ""

    # Push each character of the input string onto the stack
    for char in input_string:
        stack.append(char)

    # Pop characters from the stack to construct the reversed string
    while stack:
        reversed_string += stack.pop()

    return reversed_string

