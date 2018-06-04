#flow of the program
#1get a sentence from user
#2split the sentence into words
#3conver the words into pig latin form
#4jointhe words together into sentence (use join() method)
#5output



#1
original = input("Enter a sentence to convert into pig latin: ").strip().lower()

#2
words = original.split() #splits the sentence into words and stores it into list

#3
new_words = []
for w in words:
    if w[0] in "aeiou":
        nw = w + "yay"
        new_words.append(nw)
    else:
        pos = 0
        for letter in w:
            if letter not in "aeiou":
                pos += 1
            else:
                break
        conso = w[:pos]
        rest = w[pos:]
        nw = rest + conso + "ay"
        new_words.append(nw)

#4
output = " ".join(new_words)

#5
print(output.capitalize())