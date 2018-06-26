# Using a for loop write a program that prints out the decimal equivalents of 1/2, 1/3, 1/4 ... 1/10. Output each one
# on a new line. (Hint: Don't forget to use floating point arithmetic.)

# 1. Use a for loop with range. What numbers do you need to count?

# 2. Print your answer inside the for loop.
for i in range(2,11):
    print("1/%05d:%07.3f"%(i,1/i))
