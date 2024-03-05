# Creating an empty stack
stack = []

# Function to check if the stack is empty
def is_empty():
    return len(stack) == 0

# Function to push an element onto the stack
def push(item):
    stack.append(item)

# Function to pop an element from the stack
def pop():
    if not is_empty():
        return stack.pop()
    else:
        print("Error: Stack is empty.")
        return None

# Function to peek at the top element of the stack
def peek():
    if not is_empty():
        return stack[-1]
    else:
        print("Error: Stack is empty.")
        return None

# Function to get the size of the stack
def size():
    return len(stack)

# Test the stack operations
push(10)
push(20)
push(30)

print("Top element of the stack:", peek())

print("Popping element from the stack:", pop())
print("Popping element from the stack:", pop())

print("Is the stack empty?", is_empty())

print("Size of the stack:", size())
