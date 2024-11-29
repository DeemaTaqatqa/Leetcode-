def isValid(s):
    stack = []
    closeToOpen= { ")" : "(" ,  "]" :"[" , "}" :"{" }
    
    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        
        else:
            stack.append(c)
    
    return True if not stack else False

s = "[(])"
value = isValid(s)
print(value)


"""
the idea here is to check if the first element was a closing braket so for sure it will have false answer we can't get a closing for closing

if after appending we got a closing then we check if the last element equals the the opening for this close so we can pop it we keep poping until it's empty

if it's empty which is not stack , because if stack means if not empty the answer is true else is false 

time and space is O(n) , we run through the whole stack and the space is the whole stack too
"""