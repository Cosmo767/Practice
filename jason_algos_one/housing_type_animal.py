def housing_type_of_oldest_animal(animal_housing_dict):
    """Return the housing type which has the oldest animal of all the 
    animals in any housing type.
    sample input:
    {'apartment': {'cat': 1234, 'dog': 7}, 'house': {'mouse': 24, 'tiger': 1, 
    'groundhog': 7} }"""

    '''
    for each housing type 
        for each each animal type 
            if current age >  oldest 
                housing_type_with_oldes = current housing type 

    '''
    oldest = 0
    current_housing_type = None 
    for housing_type in animal_housing_dict:
        current_housing_dict = animal_housing_dict[housing_type]
        for animal_type in current_housing_dict:
            current_age = current_housing_dict[animal_type]
            if current_age > oldest:
                oldest = current_age
                current_housing_type = housing_type
    return current_housing_type


def test(my_input, expected_output, f):  #second order function 
    
    actual_output = f(my_input)
    successful_test = actual_output == expected_output
    success_notification = "PASS" if successful_test else "FAIL"
    output_message = ("{}: \n INPUT: {}\n OUTPUT: \n\t expected: {} \n\t actual: {}".
    format(success_notification, my_input, expected_output, actual_output))
    print(output_message) 

# Test cases

# my_input = {'apartment': {'cat': 1234, 'dog': 7}, 'house': {'mouse': 24, 'tiger': 1, 'groundhog': 7} }
# expected_output = "apartment"
# test(my_input, expected_output, housing_type_of_oldest_animal)

my_input = {'house': {'mouse': 24, 'tiger': 1, 'groundhog': 7}, 'apartment': {'cat': 2, 'dog': 89} }
expected_output = "apartment"
test(my_input, expected_output, housing_type_of_oldest_animal)


