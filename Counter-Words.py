# sentence : count words

def count_words(sentance):
    word_count = len(sentance.split())
    return word_count



sentance = input("Enter The sentace: ")

print(count_words(sentance))


