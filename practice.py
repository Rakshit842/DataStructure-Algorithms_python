def is_palindrome(n):
    original = n
    reverse = 0

    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n = n // 10

    return original == reverse

n = 121
if is_palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")