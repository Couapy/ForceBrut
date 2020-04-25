# ForceBrut

This repository contains an algorithm that allows you to test the security of your passwords.

Please do not use it as a hacker / password breaker, to hack people.

Only hack yourself thanks =)

## How to use

### Generate password hash

To generate an hash of a password, you can run the following command.

> python3 hash.py -p YOUR_PASSWORD

### Test security password

To run the script, you can run this command :

> python3 test.py --hash YOUR_HASH_HERE

Otherwise you can specified an limit of length of password to the script.
By default it's 5.

> python3 test.py -l NEW_LIMIT --hash YOUR_HASH_HERE

Finally you can adjust the dedicated threads for the script with `-t` or `--threads`.
By default, it's 2 threads.

> python3 test.py -t NUMBER_OF_THREADS --hash YOUR_HASH_HERE

But according to my tests, 1 or 2 will be sufficient. It depends on your computer configuration.

### Generate hash and testing it in the same time

> python3 hash.py -p YOUR_PASSWORD | xargs python3 test.py --hash

OR

> python3 hash.py -p YOUR_PASSWORD | xargs python3 test.py -l LIMIT --hash

## Examples

> python3 hash.py -p test5 | xargs python3 test.py -l 5 --hash
