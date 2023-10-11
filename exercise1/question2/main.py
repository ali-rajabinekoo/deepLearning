import re

file = open("plaintext.txt", "r", -1, "utf-8")
text = file.read().lower()
words = set(text.split())
target_word = ""
max_repetition = -1
writing_symbols = [r"\.", r"\,", r"\:", r"\"", r"\?", r"\!", r"\n"]

for symbol in writing_symbols:
    text = re.sub(symbol, " ", text)

for word in words:
    found = re.findall(rf"\W+{word}\W+", text, flags=re.IGNORECASE)
    count = len(found)
    if (count > max_repetition):
        target_word = word
        max_repetition = count

print(target_word)