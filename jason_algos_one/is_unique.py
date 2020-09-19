# test cases

x = [1,2,3,1,'a'] # false
y = [1,"a", "b","c"] # true 



def is_unique(my_list):
    """Return True if my_list has only one of each value, otherwise return False"""
    l = len(my_list) -1
    error = 0
    for i in range(l):
        for j in range(i+1,l+1):
            print( "i =", i, "j =", j)
            if my_list[i] == my_list[j]:
                error = error + 1
                break
            else: 
                error = error
        if error >= 1:
            return(False)
            break 

    if error >= 1:
        return(False)
    else:
        return(True)       


print(is_unique(x))