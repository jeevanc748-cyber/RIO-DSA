try:
    num = int(input("Enter a number: "))
    print("Double is:", num * 2)
except ValueError:
    print("Please enter a valid number!")