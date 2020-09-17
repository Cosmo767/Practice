# Given a non-negative integer num, 
# return the number of steps to reduce it to zero. 
# If the current number is even, you have to divide it by 2, 
# otherwise, you have to subtract 1 from it.
def count_steps(n):
    ''' Counts number of steps to reduce a given number, n, to zero '''
    # While current number doesn't equal zero do this ...
    #
    # if even divide by two
    current_num = n 
    count = 0

    while current_num > 0 :
        print(current_num, "current num")
        print(count, "count")
        if current_num%2 == 0: # number is even
            current_num = current_num/2
        else:
            current_num = current_num - 1
        count += 1
    return count


print(count_steps())