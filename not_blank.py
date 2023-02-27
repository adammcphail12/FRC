# A not blank checker checks that the users input is not blank.
# takes in a question and error
def not_blank (question,error ):
    while  True:
        name = input(question).lower()
        if name == '':
            print(error)
        else:
            return name

name = not_blank('What is your name? ', 'Bruh homes you gotta enter something g. ')
print('whatup g docs sole {} '.format(name))