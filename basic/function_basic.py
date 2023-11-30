# Parameters are variables which contain arguments.
# When a function is called with arguments, the arguments are stored in parameters.
# In general, the value that a function call evaluates to is called return value of the function.
# A return statement consists of the following:
    # The return statement.
    # The value or expression that the funtion should return.

import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain!'
    elif answerNumber == 2:
        return 'It is decidedly so!'
    elif answerNumber == 3:
        return 'Yes!'
    elif answerNumber == 4:
        return 'Reply Hazy try again!'
    elif answerNumber == 5:
        return 'Ask again later!'
    elif answerNumber == 6:
        return 'Concentrate and ask again!'
    elif answerNumber == 7:
        return 'My reply is no!'
    elif answerNumber == 8:
        return 'Outlook not so good!'
    elif answerNumber == 9:
        return 'Very doubtful!'

randomGuess = random.randint(1, 9)
answer = getAnswer(randomGuess)
print(answer)
