# problem
# This problem is for realizing the continue statement.
# when a program execution reaches to a 'continue' statement, the programe execution jumps back to the start of the loop.

while True:
    print('Who are you? ')
    user = input().lower()
    if user != 'Sayed'.lower():
        continue
    print('Hello! Sayed! What is your password?')
    password = input()

    if password == 'swordfish':
        break

print('Access granted!\n')