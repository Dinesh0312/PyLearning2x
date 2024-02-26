#Task #1 - Take a user input (name, age, roll_number, phone_number) and print the user details
user_data = (input("Enter your name: "),
             int(input("Enter your age: ")),
             int(input("Enter Your roll_number: ")),
             int(input("Enter your phone_number: ")))

print("Find the user details ", user_data)

# Task #2 - Print the Table of 2 by using the command print()
# 2 x 1 = 2
# 2 x 2 = 4
# ...
# 2 x 10 = 20

num = int(input("Enter the table number which you want: "))
for count in range(1, 11):
    print(num, 'X', count, '=', num*count)