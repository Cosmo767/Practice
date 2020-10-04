# def digital_root(n):
#     if n <= 9: # base case 
#         return n
#     else:      # function that adds digits together and creates a new number 
#         m = 0
#         for i in str(n):
#             m += int(i)
#         return(digital_root(m)) #calls digital root on new number 

# #### from codewars #####

# def digital_root(n):
#     return n if n < 10 else digital_root(sum(map(int,str(n))))
#     # map(int, str(n)) creates a list of the integers in n 
#     # sum() creates the new number and passes it back up to digital_root

#     # also from codewars #

def digital_root(n):
    return n%9 or n and 9
n=18
print(n%9 or n and 9)
print(n%9)
print(n and 9)

