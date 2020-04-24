#!/bin/python3
import argparse
import hashlib
import time


# Define characters we will use to crack passwords
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
chars = lower


# Argument parser
parser = argparse.ArgumentParser(
    description="Simple password cracker."
)
parser.add_argument(
    "--hash",
    type=str,
    default="",
    help="Hash to crack."
)
parser.add_argument(
    "-l",
    "--length_max",
    type=int,
    default=5,
    help="Maximum password length. Default is 5."
)
args = parser.parse_args()


def test_password(hash, password):
    global tests
    tests += 1

    if tests % 1000000 == 0:
        percent = int(tests / possibilities)
        time_crack = int(time.time() - time_start)
        print(f">> PROCESSING | {percent:3}% | {tests:20} tests | {time_crack} seconds", end="\r")

    h = hashlib.sha256(str(password).encode('utf-8')).hexdigest().upper()
    if hash == h:
        print(f"\n[PASSWD] Password cracked : \"{password}\"")
        time_crack = time.time() - time_start
        print(f"[TIME] It took {time_crack} seconds.")
        quit()

def force_length(hash, string, currentlength, targetlength):
    test_password(hash, string)
    if currentlength is targetlength:
        return
    for char in chars:
        force_length(hash, string+char, currentlength+1, targetlength)


# Get arguments
hash = str(args.hash).encode('utf-8').decode().upper()
length_max = args.length_max
possibilities = 0
for i in range(1, length_max):
    possibilities += len(chars)**i
print(f"There is {possibilities} possibilities to test.")
tests = 0
len_disp = len(str(possibilities))

# Run script
print(f"CRACKING \"{args.hash}\" in processing...")
time_start = time.time()
force_length(hash, '', 0, length_max)
print(f"No occurences found for maximum length = {length_max}.")
