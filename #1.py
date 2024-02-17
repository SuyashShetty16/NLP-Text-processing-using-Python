import re

# Step 1: Read the file programmatically
file_path = r'C:\Users\Suyash\OneDrive\Documents\NLP Practicals\SamplePara.txt'

with open(file_path, 'r') as file:
    text = file.read()

# Step 2: Split the text line-by-line
lines = [line.strip() for line in re.split(r'[.!?"]', text) if line]

# Step 3: Split the entire text word-by-word
words = text.lower().split()

# Step 4: Separate the list-of-words (to find most used keywords with their respective counts)
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1

# Step 5: Separate the list-of-joining-words (to ignore them)
stop_words = {'a', 'the', 'and'}
filtered_words = [word for word in words if word not in stop_words]

# Step 6: Sentiments of the text - positive (pros), negative (cons), or neutral (bag of words for this)
positive_words = {'good', 'positive', 'pros'}
negative_words = {'bad', 'negative', 'cons'}

positive_count = sum(word_counts.get(word, 0) for word in positive_words)
negative_count = sum(word_counts.get(word, 0) for word in negative_words)

sentiment = 'positive' if positive_count > negative_count else 'negative' if negative_count > positive_count else 'neutral'

# Step 7: Create a title (suitable title for the text)
title_words = [word for word in words if word not in stop_words]
title = ' '.join(title_words[:5])  # Assuming a title is the first 5 non-stop words

# Step 8: Most Used Keywords in the form of a list
most_used_keywords = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:4]

# Step 9: Display all keywords in the text with the given format
all_keywords = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:16]

# Print the results
print("Original Text:")
print(text)

print("\nSentence Tokenization:")
print(lines)

print("\nSentence Normalization:")
normalized_text = ' '.join(words)
print(normalized_text)

print("\nWord Tokenization:")
print(words)

print("\nRemove Stop Words:")
print(filtered_words)

print("\nSentiment of the Text:")
print("Sentiment:", sentiment)

print("\nKeywords in Text:")
print(all_keywords)

print("\nTitle:")
print(title)


