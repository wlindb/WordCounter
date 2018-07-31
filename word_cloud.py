from collections import Counter

# Wordcounter to see how many times each words occur in the textfile 98-0.txt, then prints out the 10 most common ones.
with open('98-0.txt', 'r') as file:
    wordcount = {}
    for word in file.read().split():

        # Clean out unnecessary characters
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace("‘", "")
        word = word.replace("“", "")
        word = word.lower()

        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1


    # Print out 10 most common word
    x = Counter(wordcount)
    mostCommon = x.most_common(10)
    for i in mostCommon:
        print(i)

