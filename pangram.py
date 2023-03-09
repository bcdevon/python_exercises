"""leetcode check if sentence is a pangram. A pangram is a sentence where every letter is used at least once"""

def checkIfPangram(sentence):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    new_sentence = set(sentence)
    if alphabet == new_sentence:
        print("True")
    else:   
        print("False")

checkIfPangram("qazwsxedcrfvtgbyhnujmiklophjgd")