import pandas


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
    return '${:.2f}'.format(x)


# Gets the exspenses, returns a list which has the data frame.
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

        quantity = int_float_check('Quantity', 'The amount must be a positive, whole number.', int)
        price = int_float_check('How much for a single item? $', 'The amount ,must be greater then 0.', float)

        # add item, quantity and price to list
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    expense_frame['Cost'] = expense_frame['Cost'].sum()

    # Find sub total
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (use currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency(add_dollars))

    return [expense_frame, sub_total]


# ------ Main Routine starts here ------
product_name = not_blank('Product Name: ', 'The product name can not be blank')

variable_expenses = get_expenses('variable')
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]


# **** Printing Area ****

print()
print(variable_frame)
print()