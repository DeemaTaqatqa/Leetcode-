def isIsomorphic(s, t):
    map_s_to_t = {}
    map_t_to_s = {}

    for char_s, char_t in zip(s,t):
        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t:
                return False
        if char_t in map_t_to_s:
            if map_t_to_s[char_t] != char_s:
                return False
            
        map_s_to_t[char_s] = char_t
        map_t_to_s[char_t] = char_s
        
    return True


s = "badc"
t = "baba"
print(isIsomorphic(s,t))
        