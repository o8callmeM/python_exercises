# Get input from user
user_input = input("Enter a number: ")

try:
    # Convert input to integer
    a = int(user_input)

    # Check User inputed number is odd or even
    if a >= 3:
        # Check if number is odd or even
        if a % 2 == 1:  # Odd number
            for num in range(1, a + 1, 2):
                print(num, end=" ")
        else:  # Even number

            for num in range(0, a + 1, 2):
                print(num, end=" ")
    else:
        print("You must enter a number greater than or equal to 3")

except ValueError:
    print("Error: Please enter a valid number")