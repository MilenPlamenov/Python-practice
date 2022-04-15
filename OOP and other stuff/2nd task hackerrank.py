word = "ab cB GG"

for i in range(len(word)):
    if word[i] != " " and word[i - 1] != " " and i != 0:
        last_ch = word[i - 1]
        if ord(word[i].lower()) >= ord(last_ch.lower()):
            word = word.replace(word[i], word[i].upper(), 1)
        else:
            word = word.replace(word[i], word[i].lower(), 1)

print(word)