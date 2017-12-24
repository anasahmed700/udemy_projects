# get sentence from user
original = input("Enter the sentence here to convert in pig latin: ").strip().lower()

# split sentence to words
words = original.split()

# loop through to words and convert to pig latin
new_words = []
for word in words:
    # if start with vowel, just add yay
    if word[0] in "aeiou":
        new_words.append(word+"yay")
    # otherwise, move the first consonant cluster to end, and add "ay"
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos+1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest+cons+"ay"
        new_words.append(new_word)


# stick words back togather
output = " ".join(new_words)

# output the final string
print(output)