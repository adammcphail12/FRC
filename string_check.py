# this is a string checker. Checks users input is what it what the program wants.
# 4 possiable valid answers.

def string_check(question, valid_1 , valid_2, valid_3, valid_4, error):
    
    while True:
        user = input('{} '.format(question)).lower()
        if user == valid_1 or user == valid_2:
            return valid_1
        elif user == valid_3 or user == valid_4:
            return valid_3
        else:
            print(error)

yes_no = string_check('Are you a criminal?', 'yes','y','no','n','Enter Yes or No')
if yes_no == 'yes' :
    print('I knew it, I saw you rob that store.')
else:
    print('R u sure?')
