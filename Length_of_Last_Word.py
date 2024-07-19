def lengthOfLastWord(s):
        words=s.split()
        return(len(words[-1]))



s = "  World  "
length=lengthOfLastWord(s)
print(length)

#if the the string was empty or has sapce to return 0 but in this case no need to use it
#        return 0 if not s or s.isspace() else len(s.split()[-1])
