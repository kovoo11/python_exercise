"""
A website requires a password to register. As always, there are a set of rules for an allowed password:

1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
3. At least 1 letter between [A-Z]
4. At least 1 character from [$#@]
5. Minimum length of password: 6
6. Maximum length of password: 12

A valid password must satisfy NO LESS THAN (>=) 5 of the rules above.

Write a program to check the validity of password.
Hint: use the `re` library. `re` stands for Regular Expression, with a lot of tutorials online.
"""
import re

def check_password_validity(pw):
    # TODO
    # return a boolean `True` if the password is valid, `False` otherwise
    counter = 0
    if re.search(r'[a-z]',pw):
        counter += 1
    if re.search(r'[A-Z]',pw):
        counter += 1
    if re.search(r'[/d]',pw):
        counter += 1
    if re.search(r'[$#@]',pw):
        counter += 1
    if re.search(r'^.{6,}$',pw):
        counter += 1
    if re.search(r'^.{,12}$',pw):
        counter += 1
    return(bool(counter >= 5))

good_password = "3GGEsdv2#gv1e4Ob2fbf"  # fails rule #6 only, so good
bad_password = "sgdf3298b"  # fails rule #3 and #4, so bad

print(check_password_validity(good_password))  # True
print(check_password_validity(bad_password))  # False
