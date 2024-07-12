"""
Word Occurrences
Estimate: 20 minutes
Actual:   23 minutes
"""

text = input("Text: ")
words = text.split(" ")
words.sort()
count = 0
for i in words:
    if len(i) > count:
        count = len(i)
        input_words = i


counted_words = {}
for i in words:
    counted_words[i] = words.count(i)

for i in counted_words:
    print(f"{i:{len(input_words)}}: {counted_words[i]}")

print()