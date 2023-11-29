import random, sys

print('R0CK, PAPER, SCiSS0R')

# These variables keep track of wins, losses and ties\
wins = 0
losses = 0
ties = 0

# The main game loop
while True:
    print('%s wins, %s losses, %s ties' % (wins, losses, ties))
    # The player input loop
    while True:
        print('Enter your move: (r)ock (p)@per (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # quit the game
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type any of r, p, s or q')

    # Display What player choose
    if playerMove == 'r':
        print('R0CK Versus ... ...')
    elif playerMove == 'p':
        print('PAPER Versus ... ...')
    elif playerMove == 's':
        print('SCISSORS Versus ... ...')

    # Display what computer choose
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('R0CK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    # Game Logic: display wins, losses and ties
    if playerMove == computerMove:
        print('It is a tie')
        ties = ties + 1
    # win conditions
    elif playerMove == 'r' and computerMove == 's':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You win!')
        wins = wins + 1
    # lose conditions
    elif playerMove == 'r' and computerMove == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You lose!')
        losses = losses + 1

