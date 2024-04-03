def isAnagram(s, t):
    s_list=  [char for char in s]
    t_list =  [char for char in t]
    t_list.sort()
    s_list.sort()
    if t_list == s_list:
        return True
    else:
        return False

