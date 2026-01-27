sentence = input("Enter a sentence: ")

# Convert to lowercase and split into words
words = sentence.lower().split()

# Count word frequencies
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
# Display results
# print("\nWord frequencies:")
# for word, count in word_count.items():
# print(f"{word}: {count}")
