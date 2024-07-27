# O(n) for time and O(1) for memory
def isPalindrome(s):
    l, r= 0, len(s)-1
    while l< r:
        while l<r and not s[l].isalnum():
            l +=1
        while l<r and not s[r].isalnum():
            r-=1
        if s[l].lower() != s[r].lower():
            return False
        l , r = l +1  , r -1
    return True

# O(n) for time and memory complexitiy 
# def isPalindrome(s):
#     clean_text = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
#     if clean_text == clean_text[::-1]:
#         return True
#     else:
#         return False


s = " "
answer=isPalindrome(s)
print(answer)

#if i can't use the isalnum() build in funtion I can built and check using the ascii number using ord funtion
# the ascii for letters from a to z is between a range and the same for numbers and captial
def alphaNum(c):
    return (ord('A') <= ord(c) <=ord('Z') or
            ord('a') <= ord(c) <=ord('z') or
            ord('0') <= ord(c) <=ord('9'))
