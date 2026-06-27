words=["apple","ant","bat","ball","car","carrot"]
grouped={}
for word in words:
    letter=word[0]
    grouped.setdefault(letter,[]).append(word)
print(grouped)