def age_of_oldest_animal(animal_dict):
        """Return the age of the oldest animal in animal_dict. 
        example input: {"cat": 7, "dog": 15}.
        The keys of the dictionary are strings representing the animal.
        """
        '''
        for animal keys in animal_diction 
            check if the current value is the current largest 
            if it is set current largest to current value
        return current largest 
        '''
        current_largest = -1
        for animal_key in animal_dict:
            current_value = animal_dict[animal_key]
            if current_value > current_largest:
                current_largest = current_value

        return current_largest





def test(my_input, expected_output, f):  #second order function 
    
    actual_output = f(my_input)
    successful_test = actual_output == expected_output
    success_notification = "PASS" if successful_test else "FAIL"
    output_message = ("{}: \n INPUT: {}\n OUTPUT: \n\t expected: {} \n\t actual: {}".
    format(success_notification, my_input, expected_output, actual_output))
    print(output_message) 

# Test cases

# my_input = {"cat": 7, "dog": 15}
# expected_output = 15 
# test(my_input, expected_output, age_of_oldest_animal)

# my_input = {"cat": 7, "dog": 7}
# expected_output = 7 
# test(my_input, expected_output, age_of_oldest_animal)

my_input = {}
expected_output = -1 
test(my_input, expected_output, age_of_oldest_animal)