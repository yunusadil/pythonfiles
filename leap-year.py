"""This script works for checking a given year is a leap year or not"""


while True:
    try:
        user_input = int(input("Please enter a Year to learn it "
                               "is really leap year or not?:\n"))
        if user_input % 4 == 0 and user_input % 100 != 0 or user_input % 
400 == 0:
            print(f"{user_input} is a Leap Year")
        else:
            print(f"{user_input} is not a Leap Year")
    except ValueError:
        print("Please enter a year with digits like '2022'!")
