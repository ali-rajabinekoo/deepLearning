import re

def wordCount(filePath):
    file = open(filePath, "r", -1, "utf-8")
    text = file.read().lower()
    words = set(text.split())
    word_count = {}
    writing_symbols = [r"\.", r"\,", r"\:", r"\"", r"\?", r"\!", r"\n"]

    for symbol in writing_symbols:
        text = re.sub(symbol, " ", text)

    for word in words:
        found = re.findall(rf"\W+{word}\W+", text, flags=re.IGNORECASE)
        word_count[word] = len(found)

    return(word_count)

plaintext_dict = wordCount("plaintext.txt")
compare_text_dict = wordCount("compareText.txt")
union_words = []

for key in plaintext_dict:
    try:
        if compare_text_dict[key] > 0:
            union_words.append(key)
    except:
        pass

print(union_words)