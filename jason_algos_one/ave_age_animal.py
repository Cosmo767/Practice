def average_animal_age(animal_dict):
    """Return the average age of all the animals in animal_dict. 
    If there are no animals, return -1"""
    # a function only returns one type of value, when possible
    '''
    count = 0
    total_age = 0 
    current_age = None
    for each animal in animal_dict 
        current_age = animal_dict[animal]
        total_age += current_age
        if there is a value count += 1 
    '''

    count = 0           # number animals in animal_dict
    total_age = 0       # sum of all the ages of animals in animal_dict
    current_age = 0     # tracks age of current animal 
    # asdfsadfas
    for animal_key in animal_dict:   #dfjsadfh
            
        current_age = animal_dict[animal_key]
        if current_age != None:
            total_age += current_age
            count += 1 
        
    average_age = (total_age / count) if (count > 0) else -1

    return average_age
    



def test(my_input, expected_output, f):  #second order function 
    
    actual_output = f(my_input)
    successful_test = actual_output == expected_output
    success_notification = "PASS" if successful_test else "FAIL"
    output_message = ("{}: \n INPUT: {}\n OUTPUT: \n\t expected: {} \n\t actual: {}".
    format(success_notification, my_input, expected_output, actual_output))
    print(output_message) 

# Test cases

# my_input = {"cat": 7, "dog": 15}
# expected_output = 11 
# test(my_input, expected_output, average_animal_age)

# my_input = {"cat": 100, "dog": 0, "bird":None}
# expected_output = 50 
# test(my_input, expected_output, average_animal_age)

# my_input = {"cat": 20}
# expected_output = 20
# test(my_input, expected_output, average_animal_age)

# my_input = {}
# expected_output = -1
# test(my_input, expected_output, average_animal_age)

my_input = {"cat": 0}
expected_output = 0
test(my_input, expected_output, average_animal_age)

