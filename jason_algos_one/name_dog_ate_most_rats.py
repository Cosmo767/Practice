def name_of_dog_that_ate_the_most_rats(dogs):
    """return the name of the dog that ate the most rats. If they ate an equal 
    number of rats, return the name of the dog that comes first alphabetically. 
    If there are no ate rats, return the empty string.
    Sample input: {"ralph": ["rat", "dog", "chicken", "rat", "rat", "chicken", "alligator"], "big": [],
    "golden": ["rat", "dolphin"], "wolf": ["rat", "rat", "cat"]}"""
    '''
    notes: input is a dict with a list for the value 

    most_rats = 0
    dog_ate_most = ""
    for dog_key in dogs_dict
        current_rat_count = 0
        iterate over each list and count the number of rats
        
        if current_rat_count > most_rats 
            most_rat_count = most_rats 
            dog_ate_most = dog_key
        elif current_rat_count == most_rats
            dog_ate_most = dog_key if dog_ate_most > dog_key else dog_ate_most
        
    return dog_ate_most 
    '''
    most_rats = 0
    dog_ate_most = ""
    for dog_key in dogs:
            current_rat_count = 0
            current_dog_arr = dogs[dog_key]
            for animal in current_dog_arr:
                if animal.lower() == "rat":
                    current_rat_count += 1
            
            if current_rat_count > most_rats:
                most_rats = current_rat_count
                dog_ate_most = dog_key
            elif current_rat_count == most_rats:
                dog_ate_most = dog_key if dog_ate_most > dog_key else dog_ate_most
    return dog_ate_most

def test(my_input, expected_output, f):  #second order function 
    
    actual_output = f(my_input)
    successful_test = actual_output == expected_output
    success_notification = "PASS" if successful_test else "FAIL"
    output_message = ("{}: \n INPUT: {}\n OUTPUT: \n\t expected: {} \n\t actual: {}".
    format(success_notification, my_input, expected_output, actual_output))
    print(output_message) 
#test cases
    # one dog that has eaton the most rats  
my_input    = {"ralph": ["rat", "dog", "chicken", "rat", "rat", "chicken", "alligator"], 
                "big": [], "golden": ["rat", "dolphin"], "wolf": ["rat", "rat", "cat"]}
expected_output =  "ralph"
test(my_input, expected_output, name_of_dog_that_ate_the_most_rats)
    # variation: one dog that has eaton the most rats 
my_input    = {"ralph": ["rat", "dog", "chicken", "rat", "rat", "chicken", "alligator"], 
                "big": [], "golden": ["rat", "dolphin"], "wolf": ["rat", "rat","rat","rat", "cat"]}
expected_output =  "wolf"
test(my_input, expected_output, name_of_dog_that_ate_the_most_rats)
    # two dogs are tied for eaton most rats 
my_input    = {"ralph": ["rat", "dog", "chicken", "rat", "rat", "chicken", "alligator"], 
                "big": [], "golden": ["rat", "dolphin"], "wolf": ["rat", "rat","rat","rat", "cat"]}
expected_output =  "wolf"
test(my_input, expected_output, name_of_dog_that_ate_the_most_rats)

my_input    = {"ralph": [ "dog", "chicken", "chicken", "alligator"], 
                "big": [], "golden": ["dolphin"], "wolf": ["cat"]}
expected_output =  ""
test(my_input, expected_output, name_of_dog_that_ate_the_most_rats)

