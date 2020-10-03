def most_common_letter(text):
    """Returns the letter of the alphabet that occurs most frequently. If there is a tie, choose the letter that comes first in the alphabet.
    If there are no letters, return the empty string"""
    
    '''
    create a dictionary with a value for each key that counts how many time 
        the letter appears.
    keep track of the max value and the respective key as we iterate over the string.
    return the letter at the end. 
    '''
    lower_case_text = text.lower()
    my_dict = {}
    current_largest = ""
    my_dict[current_largest] = 0
    for char in lower_case_text:
        if char >= "a" and char <= "z":     #the char is a letter
            if char in my_dict:             #the letter is already in the dict
                my_dict[char] += 1
            else:                           #the letter is not in the dict
                my_dict[char] = 1

            if (my_dict.get(char) > my_dict.get(current_largest)):
                    current_largest = char 
            elif (my_dict.get(char) == my_dict.get(current_largest)):
                    current_largest = current_largest if char > current_largest else char #ternary expression
    # print(current_largest, "Current Largest")
    # print(my_dict, "my dict")
    return current_largest


'''
test cases

input expected vs output
'''


def test(my_input, expected_output):
    
    actual_output = most_common_letter(my_input)
    successful_test = actual_output == expected_output
    success_notification = "PASS" if successful_test else "FAIL"
    output_message = ("{}: \n INPUT: {}\n OUTPUT: \n\t expected: {} \n\t actual: {}".
    format(success_notification, my_input, expected_output, actual_output))
    print(output_message)   
# test("aab", "a")

# test("beta", "a" )
# test("", "")
#test("5,2,3,3,3","") #21
# test("2,2,2z", "z") #21
# test("TaeaTt","t")
test("ABCabc","a")

