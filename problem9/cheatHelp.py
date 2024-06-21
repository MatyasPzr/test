sample = "bill gates is bull"
pattern = "b_ll"

patternMatchers = []
for word in sample.split():
    word_score = 0
    for i, letter in enumerate(word):
        if letter == pattern[i] or pattern == "_":
            word_score += 1

    if word_score == len(pattern):
        patternMatchers.append(word_score)
    