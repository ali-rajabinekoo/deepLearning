import re

file = open("plaintext.txt", "r", -1, "utf-8")
text = file.read().lower()
words = set(text.split())
word_count = {}
writing_symbols = [r"\.", r"\,", r"\:", r"\"", r"\?", r"\!", r"\n"]

for symbol in writing_symbols:
    text = re.sub(symbol, " ", text)

for word in words:
    found = re.findall(rf"\W+{word}\W+", text, flags=re.IGNORECASE)
    word_count[word] = len(found)

print(word_count)