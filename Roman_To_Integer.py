def intToRoman(s):
    values = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
    }   
    i=len(s)-1
    num=0
    while(i>=0):

        if i > 0 and s[i]=="V" and  s[i-1]=="I": 
            num+=4
            i -= 2
        elif i > 0 and s[i]=="X" and  s[i-1]=="I": 
            num+=9
            i -= 2
        elif i > 0 and s[i]=="L" and  s[i-1]=="X": 
            num+=40
            i -= 2        
        elif i > 0 and s[i]=="C" and  s[i-1]=="X": 
            num+=90
            i -= 2        
        elif i > 0 and s[i]=="D" and  s[i-1]=="C": 
            num+=400
            i -= 2
        elif i > 0 and s[i]=="M" and  s[i-1]=="C": 
            num+=900
            i -= 2
        else:
            num += values[s[i]]
            i= i-1
        

    return num
        

s= "MMMCDXC"
number= intToRoman(s)
print(number)





