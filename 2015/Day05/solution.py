def hasAtLeastThreeVowels(text):
    vowel_count = 0
    for c in text:
        if c == 'a':
            vowel_count += 1
        elif c == 'e':
            vowel_count += 1
        elif c == 'i':
            vowel_count += 1
        elif c == 'o':
            vowel_count += 1
        elif c == 'u':
            vowel_count += 1

        if vowel_count >= 3:
            return True

    return False


def hasDoubleLetter(text):
    for i in range(len(text) - 1):
        if text[i] == text[i + 1]:
            return True
    return False


def hasForbiddenString(string):
    if "ab" in string:
        return True
    if "cd" in string:
        return True
    elif "pq" in string:
        return True
    elif "xy" in string:
        return True
    else:
        return False


file = open("input.txt")
lines = file.readlines()
nice_string_count = 0

for line in lines:
    if hasAtLeastThreeVowels(line) and hasDoubleLetter(line) and not hasForbiddenString(line):
        nice_string_count += 1

print(nice_string_count, 'strings are nice')
