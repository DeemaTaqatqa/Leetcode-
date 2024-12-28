def wordPattern(pattern, s):
    letter_to_word ={}
    word_to_letter = {}
    words = s.split()
    
    if len(words) != len(pattern):
        return False

    for p, w in zip(pattern, words): # I can iterate through both lists in zip since they are equal
        if (p in letter_to_word and letter_to_word[p] != w) or (w in word_to_letter and word_to_letter[w] != p): 
            # I need to check from 2 sides because it has to be one to one from each side that's why I made 2 hashmaps
            return False
        letter_to_word[p] = w
        word_to_letter[w] = p
        
    return True

res =wordPattern("abba","dog cat cat dog")
print(res)