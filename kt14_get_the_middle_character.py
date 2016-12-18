def get_middle(s):
    if len(s) % 2 == 0:
        ind = len(s) // 2
        return s[ind-1:ind+1]
    else:
        ind = len(s) // 2 
        return s[ind]