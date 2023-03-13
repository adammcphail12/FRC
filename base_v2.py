import pandas


def string_check(question, valid_1, valid_2, valid_3, valid_4, error):
    while True:
        user = input('{} '.format(question)).lower()
        if user == valid_1 or user == valid_2:
            return valid_1
        elif user == valid_3 or user == valid_4:
            return valid_3
        else:
            print(error)


# checks users enter a number (float / int) more than zero, takes in
# custom question and error message
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


# This functions checks that the users input is not blank.
def not_blank(question, error):
    while True:
        name = input(question).lower()
        if name == '':
            print(error)
        else:
            return name


# this function returns the input in a dollars cents format
def currency(x):
    return '${:.2f}'.format(float(x))


# Gets the expenses, returns a list which has the data frame.
def get_expenses(var_fixed):
    # set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        'Item': item_list,
        'Quantity': quantity_list,
        'Price': price_list
    }

    # loop to get a component, quantity and price
    item_name = ''
    while item_name.lower() != 'xxx':
        print()
        # get name quantity and item
        item_name = not_blank('Item name: ', 'The component name can not be blank.')
        if item_name.lower() == 'xxx':
            break
        # Is this a item of fixed costs?
        if var_fixed is False:
            quantity = int_float_check('Quantity', 'The amount must be a positive, whole number.', int)
        else:
            quantity = 1

        price = int_float_check('How much for a single item? $', 'The amount ,must be greater then 0.', float)

        # add item, quantity and price to list
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find sub-total
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (use currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

    return [expense_frame, sub_total]


# yes no checker.
def yes_no(question):
    while True:
        response = input(question).lower()

        if response == 'yes' or response == 'y':
            return 'yes'
        elif response == 'no' or response == 'n':
            return 'no'
        else:
            print('Please Enter Yes Or No.')


# ------ Main Routine starts here ------
product_name = not_blank('Product Name: ', 'The product name can not be blank')

fixed = yes_no('do you have fixed costs? ')
if fixed == 'yes':
    fixed_expenses = get_expenses(True)
    fixed_frame = fixed_expenses[0]
    fixed_sub = fixed_expenses[1]

print('Variable Costs')

variable_expenses = get_expenses(False)
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# **** Printing Area ****


print('\n********** Variable Costs **********\n')
print(variable_frame)
print('\nTotal Variable Costs: {}'.format(variable_sub))

if fixed == 'yes':
    print('\n********** Fixed Costs **********\n')
    print(fixed_frame[['Cost']])
    print('\nTotal Fixed Costs: {}'.format(fixed_sub))
    total = fixed_sub + variable_sub
else:
    total = variable_sub

profit_goal = [int_float_check('What is your desired profit goal? ', 'This has to be a number greater then 0',
                               float),
               string_check('Is this in dollars (enter $) or a percentage (enter %)? ', '$', 'Dollars', '%',
                            'percent', 'That is not a valid answer, Valid answers include $ or %')]

print('Ok so your profit goal is {}{}'.format(profit_goal[1], profit_goal[0]))


