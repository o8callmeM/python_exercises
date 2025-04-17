#print(' '.join(input("Enter a phrase: ").split()[::-1]))
def reverse_words():
    user_input = input("Enter a phrase: ")    
    words = user_input.split()    
    reversed_words = words[::-1]
    # Join the reversed words back into a string
    reversed_phrase = ' '.join(reversed_words)
    # Print the result
    print("Reversed phrase:", reversed_phrase)

# Run the function
reverse_words()