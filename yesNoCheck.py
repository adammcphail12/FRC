# ------- functions -----------------

# Yes / No Check
def yesNo(question):
    while True:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            return 'yes'
        elif response == 'no' or response == 'n':
            return 'no'
        else:
            print('Please Enter Yes Or No.')


# ------- main routine

instructions = yesNo('\nWould you like to read the Instructions? ')
if instructions == 'yes':
    print('Insert Instructions Here\n')
print('Ok Lets Continue.')