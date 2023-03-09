def truncateSentence(s,k):
    for i in range(len(s)):
        if k == 0:
            # return the sentence s from the first index up to and including the last index i-1
            return s[:i-1]
        # if the value at index i is blank subtract 1 from k
        if s[i] == " ":
            k -= 1
    #looped through s and found no spaces so returns s this would happen if there is only 1 word"
    return s

print(truncateSentence("Hello how are you Contestant", 4))