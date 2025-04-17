name = input("Enter a name: ")

# Check if the input contains any digits
if any(char.isdigit() for char in name):
    print("Invalid input: NO Numbers!")
else:
    # Define vowels to count
    vowels = {'a', 'e', 'i', 'o', 'u'}
    count = 0
    
    # Count each vowel (case-insensitive)
    for char in name.lower():
        if char in vowels:
            count += 1
    
    print(f"Results: Counting vowels: {count}")