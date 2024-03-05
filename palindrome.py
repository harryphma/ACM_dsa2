def is_palindrome(num):
    
    digits = []
    for digit in str(num):
        digits.append(int(digit))
    
    
    left, right = 0, len(digits) - 1
    while left < right:
        if digits[left] != digits[right]:
            return False
        left += 1
        right -= 1
    return True


num = int(input("Enter a number to check if it's a palindrome: "))
if is_palindrome(num):
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")


