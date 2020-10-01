def cannibal_dog_count(dogs):
    """Return the number of dogs which ate another dog. 
        Sample input: {"ralph": ["rat", "dog", "chicken", "rat", "rat", "chicken", "alligator"], "big": [],
    "golden": ["rat", "dolphin"], "wolf": ["rat", "rat", "cat"]}"""
    '''
    iterate over the dictionary, dogs
        iterate over the array
            check if there is "dog" in that array
            if yes, 
                number_of_cannibals += 1
                break
    '''

    number_of_cannibals = 0

    for dog_key in dogs:
        if "dog" in dogs[dog_key]:
            number_of_cannibals += 1
    
    return number_of_cannibals





def test(my_input, expected_output, f):  #second order function 
    
    actual_output = f(my_input)
    successful_test = actual_output == expected_output
    success_notification = "PASS" if successful_test else "FAIL"
    output_message = ("{}: \n INPUT: {}\n OUTPUT: \n\t expected: {} \n\t actual: {}".
    format(success_notification, my_input, expected_output, actual_output))
    print(output_message)
    
# Test cases
# one dog ate a dog
my_input    = {"ralph": ["rat", "dog", "chicken", "rat", "rat", "chicken", "alligator"], "big": [],
                "golden": ["rat", "dolphin"], "wolf": ["rat", "rat", "cat"]}
expected_output =  1
test(my_input, expected_output, cannibal_dog_count)
# two dogs ate at least one dog
my_input    = {"ralph": ["rat", "dog", "chicken", "rat", "rat", "chicken", "alligator"], "big": [],
                "golden": ["rat", "dolphin", "dog"], "wolf": ["rat", "rat", "cat"]}
expected_output =  2
test(my_input, expected_output, cannibal_dog_count)
# no cannibals
my_input    = {"ralph": ["rat", "chicken", "rat", "rat", "chicken", "alligator"], "big": [],
                "golden": ["rat", "dolphin"], "wolf": ["rat", "rat", "cat"]}
expected_output =  0
test(my_input, expected_output, cannibal_dog_count)

# no animals
my_input    = {}
expected_output =  0
test(my_input, expected_output, cannibal_dog_count)