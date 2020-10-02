def duplicate_count(text):
    text_lower = text.lower()
    dict_count = {}
    count = 0
    for m in text_lower:
        if m in dict_count:
            dict_count[m] += 1
        else:
            dict_count[m] = 1 
    for key in dict_count:
        if dict_count[key] > 1:
            count += 1
        else:
            pass
    return count 



def test(my_input, expected_output, f):  #second order function 
    
    actual_output = f(my_input)
    successful_test = actual_output == expected_output
    success_notification = "PASS" if successful_test else "FAIL"
    output_message = ("{}: \n INPUT: {}\n OUTPUT: \n\t expected: {} \n\t actual: {}".
    format(success_notification, my_input, expected_output, actual_output))
    print(output_message) 

my_input = ''
expected_output = 0
test(my_input,expected_output,duplicate_count)

my_input = 'adafad'
expected_output = 2
test(my_input,expected_output,duplicate_count)

my_input = 'Indivisibilitiesv'
expected_output = 3
test(my_input,expected_output,duplicate_count)




