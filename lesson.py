def get_multiplied_digits(number):

    str_number = str(number)
    if str_number != '':
        first = 4
        first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(40203)
print(result)
