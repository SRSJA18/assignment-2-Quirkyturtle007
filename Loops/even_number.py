# Write a program using a while loop that asks the user to enter a number that is divisible by 2.
#
# Give the use a witty message if they enter something that is not divisible by 2 and make them enter a new number.
#
# Don't let them stop until they enter an even number! Print a congratulatory message when they *finally* get it

# This line will ask the user for an even number.
number = eval(input("Enter an even number: "))

# 1. create while a loop (What will the condition be?)
while number%2!=0:
# 2. Inside the while loop What will you need to do? Don't forget to tab in!
    print("Try again")
    number = eval(input("Enter an even number: "))
# 3. Once the user has entered an even number, congratulate them!
print("good job")