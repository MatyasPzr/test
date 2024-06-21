with open("randomText.txt", "r") as file:
    content = file.read().lower()


while True:
    patternMatchers = []
    word_len = int(input("Input word length: "))
    for word in content.split():
        if len(word) == word_len:
            patternMatchers.append(word)

    print(patternMatchers)
