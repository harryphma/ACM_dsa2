'''
def most(sentence):
    big = 0

    for i in range(len(sentence)):
        size = len(sentence[i].split())
        if size > big:
            big = size

    return big


sentence = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(most(sentence))
'''

def is_palindrome(queue):
    original_queue = queue.copy()

    reversed_queue = []

    while original_queue:
        reversed_queue.append(original_queue.pop())

    while queue and reversed_queue:
        if queue.pop() != reversed_queue.pop():
            return False
    
    return True

q1 = [1, 2, 3, 2, 1]
print(is_palindrome(q1)) #Output = true

q2 = [1, 2, 3, 4, 5]
print(is_palindrome(q2)) #Output = false
    
