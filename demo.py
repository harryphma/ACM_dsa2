'''
# Example string
text = "Hello world, welcome to Python programming."

# Splitting the string on space
words = text.split()
print(words)

# Splitting the string on comma
phrases = text.split(',')
print(phrases)

# Splitting the string on 'o'
o_split = text.split('o')
print(o_split)
'''

# List of words
words = ['Python', 'is', 'awesome']

# Joining words with space
sentence = ' '.join(words)
print(sentence)

# Joining words with a comma and a space
comma_separated = ', '.join(words)
print(comma_separated)

# Joining with a newline character
new_line_separated = '\n'.join(words)
print(new_line_separated)


