#!/usr/bin/env python
from getpass import getpass
pswrd = ("brakesec")
password = getpass("What is your password?\n")
bad_password = ["123456","monkey123","123456789","qwerty","123455678", "111111","1234567890","1234567","password","123123","987654321","qwertyuiop","mynoob","123321","7777777","1q2w3e4r","654321","555555","google","1q2w3e4r5t","123qwe","zxcvbnm","1q2w3e"]
if password == pswrd:
    print "Correct!"
elif password in bad_password:
    print "Bad Security Person! That is an easily cracked password. Shame on you!"
else:
    print "Password not found."
