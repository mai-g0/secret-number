
secret_number = 50

guess = int(input("Guess the secret number: "))

while guess != secret_number:
    print("Ha ha! You're stuck in my loop!")
    guess = int(input("Guess the secret number: "))

print(secret_number)
print("""
Well done, muggle! You are free now.
""")

