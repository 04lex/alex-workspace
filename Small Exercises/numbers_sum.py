# Create a variable called previous_num and assign it to 0
previous_num = 0

# Iterate the first 10 numbers one by one using for loop and range() function
for i in range(10):
    # Next, display the current number (i), previous number, and the addition of both numbers in each iteration of the loop. Finally, change the value of the previous number to the current number ( previous_num = i).
    print('Current number:', i, 'Previous number:', previous_num, 'Sum:', i + previous_num)
    previous_num = i