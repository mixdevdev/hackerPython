def reverse_words_order_and_swap_cases(sentence):
    thestr = ''
    for i in sentence:
        if i.isspace():
            thestr+= " "
        else:
            if i.isupper():
                thestr+= i.lower()
            if i.islower():
                thestr+= i.upper()
    words = list(reversed(thestr.split()))
    word = " ".join(words)
    return word
print(reverse_words_order_and_swap_cases("Dog are Fun"))