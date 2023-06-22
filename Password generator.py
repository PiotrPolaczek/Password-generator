import random

characters = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
              'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
              'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
              'x', 'c', 'v', 'b', 'n', 'm']

digits = []
x = int(input("Enter how many characters the password should consist of: "))

for _ in range(x):
    digit = random.choice(characters)
    digits.append(digit)

print("Generated password:", ''.join(digits))