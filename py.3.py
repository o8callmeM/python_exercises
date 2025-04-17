def count_words():
    # Get input phrase from user
    phrase = input("Enter a phrase: ")
    
    words = phrase.lower().split()
    
    # Count word occurrences
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Print the result in the specified format
    print("{", end="")
    for i, (word, count) in enumerate(word_counts.items()):
        if i != 0:
            print(", ", end="")
        print(f'"{word}": {count}', end="")
    print("}")

count_words()