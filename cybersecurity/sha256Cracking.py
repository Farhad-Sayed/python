from pwn import *
import sys

if len(sys.argv) != 2:
    print("Invalid Arguments ... ... ...")
    print("Please provide SHA256 hash as an argument.  ... ... ...")
    print(f"{sys.argv[0]} needs <SHA256sum>!")
    exit()

provided_hash = sys.argv[1]
password_file = "rockyou.txt"
attempts = 0

with log.progress(f"Attempting to crack {provided_hash} \n") as p:
    with open(password_file, 'r', encoding='latin-1') as pass_list:
        for password in pass_list:
            password = password.strip("\n").encode('latin-1')
            pass_hash = hashlib.sha256(password)
            p.status(f"{attempts}, {password.decode('latin-1')}, {pass_hash}")
            if pass_hash.hexdigest() == provided_hash:
                p.success(f"Password hash found after {attempts}! \"{password.decode('latin-1')}\" hashes to {pass_hash.hexdigest()}")
                exit()
            attempts += 1
        p.failure("Password hash not found!!!")
