#!/usr/bin/env python
while True:
    try:
        num1 = float(raw_input("First number: "))
        break
    except:
        print ("Only numbers, please!")
        
while True:
    try:
        num2 = float(raw_input("Second number: "))
        break
    except:
        print ("Only numbers, please!")
operation = raw_input("+, -, *, or /: ")
if operation == ("+"):
    print num1 + num2
elif operation == ("-"):
    print num1 - num2
elif operation == ("*"):
    print num1 * num2
elif operation == ("/"):
    try:
        print num1 / num2
    except:
        print ("You can't divide by 0, silly!")
else:
    print "Error"
