def reverse(x):
    
    if x < (2**31 - 1) and x >= 0:
        x_str = str(x)
        revers_str = ""
        for i in range(len(x_str)):
            revers_str += x_str[-i-1]
        revers_int = int(revers_str)
        if revers_int > 2**31 - 1:
            revers_int = 0
        else: pass 
    elif x <= 0 and x > -(2**31):
        x_str = str(abs(x))
        revers_str = ""
        for i in range(len(x_str)):
            revers_str += x_str[-i-1]
        revers_int = -1*int(revers_str)
        if revers_int < -2**31:
                revers_int = 0
        else: pass 
    else: revers_int = 0 
    return revers_int 

print(reverse(1534236469))

