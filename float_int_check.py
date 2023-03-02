# number checking function

def int_float_check(question, error , num_type):
    valid = False
    while not valid:
        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

age = int_float_check('How old are you? ','Thats not a whole number ya fool', int)

print('Damn your {}, I coulda sworn your old ass lookin mf was 99'.format(age))


