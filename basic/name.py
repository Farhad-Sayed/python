# problem:
# This program is a simple program which will not end until you input the correct name!


name = ''

while name != 'Sayed'.lower():
    print('Please type your name: ')
    name = input().lower()
print('Thank you!', name)