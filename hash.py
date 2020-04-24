#!/bin/python3
import hashlib
import argparse


parser = argparse.ArgumentParser(description="Hash a password.")
parser.add_argument(
    "-p",
    "--password",
    type=str,
    default="",
    help="Password to hash."
)
args = parser.parse_args()


if args.password is '':
    print("[ERROR] Please run ./hash.py -p yourpassword")
    quit()


password = str(args.password).encode('utf-8')
hash = hashlib.sha256(password).hexdigest()
print(hash)

