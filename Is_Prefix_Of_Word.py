def isPrefixOfWord(sentence, searchWord):
    words = sentence.split()
    for i,word in enumerate(words):
        if word.startswith(searchWord):
            return i +1
    return -1

sentence = "this problem is an easy problem"
searchWord = "pro"
print(isPrefixOfWord(sentence, searchWord))


"""
time 
O(n) (splitting the sentence) + O(m × s) (prefix), n length of the string and m is the number of words
O(n) for the words list
"""