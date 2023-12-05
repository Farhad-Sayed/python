# input all my cat names and show the list

catNames = []

while True:
    print('Enter the name of cat' + str(len(catNames) + 1) + ' (or enter nothing to stop):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list caoncatation

print('My cats are:')
for name in catNames:
    print(name)
