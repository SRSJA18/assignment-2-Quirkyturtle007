# Write a program using a while loop that asks the user for a number, and prints a countdown from that number
# to zero.
#
# What should your program do if the user inputs a negative number?
#
# As a programmer, you should always consider "edge conditions" like these when you program!
# (Another way to put it, always assume the users of your program will be trying to find a way to break it!
# If you don't include a condition that catches negative numbers, what will your program do?)

# This line asks the user to input a number and stores it in the variable count.
count = eval(input("Countdown from?"))
# 1. Create while loop that counts down to zero (What will the condition be? What occurs inside the loop?)
for i in range(count,-1,-1):
    print(i)