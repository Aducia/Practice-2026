number = 1234
result = ""

while number > 0:
    digit = number % 10
    result = chr(ord('0') + digit) + result
    number //= 10

print(result)
