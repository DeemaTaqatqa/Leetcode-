from collections import Counter
def canConstruct(ransomNote, magazine):
    counter = Counter(magazine)
    
    for c in ransomNote:
        if c not in counter:
            return False
        elif counter[c] == 1:
            del counter[c]
        else:
            counter[c] -=1
    return True
        
ransomNote = "aa"
magazine = "aab"
print(canConstruct(ransomNote,magazine))


"""
to create a dictionary to count the frequancy of each letter you have multiple ways:
manually:
counter = {}
for c in magazine:
    if c in counter:
        counter[c] += 1
    else:
        counter[c] = 1

counter = defaultdic(int)
for c in magazine:
    if c in counter:
        counter[c] += 1
        you can don't use the else if the key doesn't exist because of defaultdic it's already 0
        
"""