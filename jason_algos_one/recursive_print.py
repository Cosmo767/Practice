def recursive_print(s):
    """Print each of the characters in the string 
    s from first to last. Do it recursively 
    (call the function inside of itself); dont use a 'for
     or 'while' loop to do it."""
    # base case: length of s = 1
    # print last letter

    if len(s) == 1:
        print(s, "is the last letter")
    else:
        current_letter = s[0]
        print(current_letter)
        sub_string = s[1:len(s)]
        print(sub_string, "current sub string")
        recursive_print(sub_string)




recursive_print("Mississippi")