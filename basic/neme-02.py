# problem:
# This problem is for realizing the break statement. And I use the previous problem called name.py for this!
# If you give the correct output it will break the statement and come out from the loop. Otherwise, it jump back to the while statement

while True:
    print('Please type your name ')
    name = input().lower()
    if name == 'Sayed'.lower():
        break

print('Thank you!', name)