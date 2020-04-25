#!/bin/python3

import hashlib
import argparse
import threading
import time


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


class Cracker(threading.Thread):

    def __init__(self, affected_chars):
        threading.Thread.__init__(self)
        self.affected_chars = affected_chars

        self.tests = 0
        self.possibilities = len(affected_chars)
        for i in range(2, length_max):
            self.possibilities += len(chars)**i

    def run(self):
        for c in self.affected_chars:
            if RUN:
                self.force_length(c, 1, length_max)

    def force_length(self, string, currentlength, targetlength):
        self.test_password(string)
        if currentlength is targetlength:
            return
        if RUN:
            for char in chars:
                self.force_length(string+char, currentlength+1, targetlength)

    def test_password(self, password):
        global tests, RUN
        self.tests += 1

        h = hashlib.sha256(str(password).encode('utf-8')).hexdigest().upper()
        if hash == h:
            RUN = False
            print(f"\n[PASSWD] Password cracked : \"{password}\"")
            time_crack = time.time() - time_start
            print(f"[TIME] It took {time_crack} seconds.")


# Define characters we will use to crack passwords
lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
chars = lower + number


# Get arguments
hash = str(args.hash).encode('utf-8').decode().upper()
length_max = args.length_max
only_max_length = args.only_max_length


# Vars
thread_number = 12
threads = []
RUN = True


# Run script
possibilities = 0
if only_max_length:
    possibilities = len(chars)**length_max
else:
    for i in range(1, length_max+1):
        possibilities += len(chars)**i
print(f"There is {possibilities} to test.")
print(f"TESTING \"{args.hash}\" in processing...")

time_start = time.time()
chars_array = list(chars)
chars_per_array = int(len(chars) / thread_number)

for i in range(thread_number):
    if i == thread_number-1:
        array = chars_array[chars_per_array*i:len(chars)]
    else:
        array = chars_array[chars_per_array*i:chars_per_array*(i+1)]
    new_thread = Cracker(''.join(array))
    threads.append(new_thread)
    new_thread.start()

threads_alive = True
while threads_alive:
    tests = 0
    for thread in threads:
        tests += thread.tests

    percent = (tests / possibilities) * 100
    time_diff = int(time.time() - time_start)
    print(
        f">> PROCESSING | {percent:3.2f}% | {tests:20} tests |" +
        f" {time_diff} seconds",
        end="\r"
    )

    time.sleep(1)
    threads_alive = False
    for thread in threads:
        if thread.is_alive():
            threads_alive = True
            break

for i in range(thread_number):
    threads[i].join()

if RUN:
    print(f"\nNo occurences found for maximum length = {length_max}.")

tests = 0
for thread in threads:
    tests += thread.tests
percent = (tests / possibilities) * 100
time_diff = time.time() - time_start
print(
    f"{possibilities} possibilities | {tests} tests | " +
    f"{percent} percent | {time_diff:.2f} seconds"
)
