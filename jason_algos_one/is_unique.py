# test cases

x = [1,2,3,1,'a'] # false
y = [1,"a", "b","c"] # true 


'''
def is_unique(my_list):
    """Return True if my_list has only one of each value, otherwise return False"""
    l = len(my_list) -1
    error = 0
    for i in range(l):            		#O(n^2)
        for j in range(i+1,l+1):
           
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
'''
'''
def is_unique(my_list):
    my_set = set(my_list)          		#O(n)
    return(len(my_list)==len(my_set)) 	#O(1) 
'''

def is_unique(my_list): #['a', 'a', 4 ] {'a':2, 4:1} , my_dict['a']
    '''
    Return true if the input list has all unique elements
    
    Create a dictionary where there is a key for each distinct item in my_list 
    and the value for each key is the number of occurances of item in my list
    
    '''
    my_dict = {}
    for item in my_list:  # O(n)
        # check to see if the item is in my_dict (as a key).  
        if item in my_dict: # O(1) to know whether item is a key in my_dict
            #my_dict[item] += 1
            return False    # the item was already in my_dict, so there is a duplicate 
        else: #if the item is not already in my_dict as a key
            my_dict[item] = 1
    return True # this only runs if no duplicate is found 
  
# test helper function
def test_is_unique(my_input, expected_output):
    
    actual_output = is_unique(my_input)
    successful_test = actual_output == expected_output
    success_notification = "PASS" if successful_test else "FAIL"
    output_message = "{}: \n INPUT: {}\n OUTPUT: \n\t expected: {} \n\t actual: {}".format(success_notification, my_input, expected_output, actual_output)
    print(output_message)     


# tests
test_is_unique([1,2,3,1,'a','a'], False)
test_is_unique([1,"a", "b","c"], True)
test_is_unique([], True)
test_is_unique([1], True)
test_is_unique([1, 1, 1, 1], False)


#is_unique([1,2,3,4,2])
