def lesser_of_tow_number(a, b):
    """
    this is a word problem where the return output is a number out of two input, if both the numbers are even then
    the smallest of them will be returned else if one of them ot both of them are odd then the bigger number will be
    returned :param a: :param b: :return:
    """
    result = 0
    if a % 2 == 0 and b % 2 == 0:
        if a > b:
            result = b
        else:
            result = a
    else:
        print('One of the number is odd')
        if a > b:
            result = a
        else:
            result = b
    return result


output = lesser_of_tow_number(2, 8)
print(f'output is :{output}')

"""
Next section
"""


