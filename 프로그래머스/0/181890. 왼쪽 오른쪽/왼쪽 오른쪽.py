def solution(str_list):
    if "l" in str_list:
        x = str_list.index("l")
    else:
        x = len(str_list) 
    
    if "r" in str_list:
        y = str_list.index("r")
    else:
        y = len(str_list) 
    
    if x < y:
        return str_list[:x]  
    elif y < x:
        return str_list[y+1:] 
    
    return []