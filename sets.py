def extract_unique_words(paragraph):
    # Split the paragraph into words and convert them to lowercase
    words = paragraph.lower().split()
    print('\n\nThis is the words result.')
    print(words)

    set_of_words = set(words)
    print('\n\nThis is the words set.')
    print(set_of_words)

    # Create a set to store unique words
    unique_words = set(words)
    print('\n\nThis is the unique words result.')
    print(unique_words)

    return unique_words

# Example paragraph
paragraph1 = "Python is a great and powerful programming language. Python is popular and powerful."

extract_unique_words(paragraph1)

# Extracting unique words
#unique_words1 = extract_unique_words(paragraph1)
#print("Unique words in paragraph 1:", unique_words1)