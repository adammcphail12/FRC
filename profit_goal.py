import math


def string_check(question, valid_1, valid_2, valid_3, valid_4, error):
    while True:
        user = input('{} '.format(question)).lower()
        if user == valid_1 or user == valid_2:
            return valid_1
        elif user == valid_3 or user == valid_4:
            return valid_3
        else:
            print(error)


def int_float_check(question, error, num_type):
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


def round_up(amount, round_to):
    return int(math.ceil(amount / round_to)) * round_to


number_of_items = int_float_check('How many items do you have? ', 'That is not a positive, whole number. ', int)

cost_per_item = int_float_check('What is the cost of a single item?', 'Sorry that is not a positive number.', float)

expense = number_of_items * cost_per_item

profit_goal = [int_float_check('What is your desired profit goal? ', 'This has to be a number greater then 0',
                               float),
               string_check('Is this in dollars (enter $) or a percentage (enter %)? ', '$', 'Dollars', '%',
                            'percent', 'That is not a valid answer, Valid answers include $ or %')]

if profit_goal[1] == '%':
    print(f'Your profit goal is {profit_goal[0]}{profit_goal[1]}')
    target = ((profit_goal[0] * expense) / 100) + expense
    print(f'Your target is ${target}')
else:
    print('Ok so your profit goal is {}{}'.format(profit_goal[1], profit_goal[0]))
    target = profit_goal[0] + expense
    print(f'Your target is ${target}')

suggested_price = round_up(target / number_of_items, 5)

print(f'Sell each item for ${suggested_price}')

