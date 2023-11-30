import time, sys

indent = 0
# how many spaces to indent
indentIncreasing = True
# whether the indentation is increasing or not

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # pause fo 1/10 of a second

        if indentIncreasing:
            indent = indent + 1
            # increase the number of spaces
            if indent == 20:
                indentIncreasing = False
                # change direction

        else:
            indent = indent - 1
            # decrease the number of spaces
            if indent == 0:
                indentIncreasing = True

except KeyboardInterrupt:
    sys.exit()

