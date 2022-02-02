# Determining the Most Frequently Occuring Items in a Sequence
# 1.12.1
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
from re import A
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

# Discussion
word_counts['not']
word_counts['eyes']

# --
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
for word in morewords:
    word_counts[word] += 1

word_counts['eyes']

# --
word_counts.update(morewords)

# --
a = Counter(words)
b = Counter(morewords)
a
b

# Combine Counts
c = a + b
c

# Subtract Counts
d = a - b
d

