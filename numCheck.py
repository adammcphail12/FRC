# sets up a function taht takes two inputs, the desired question
#and the error messaage.
def num_check(question, error):

    #runs the loop until it gets the response from the user that
    # it is looking for - in this case a positive integer.
    valid = False
    while not valid:
        #This means it will try asking for the integer first. 
        # if it gets a value error it will move to the 'Except" 
        # method. Where it prints the predetermined error method.
         try:
            #input has to be a integer or else it will get a 
            # value error.
             response = int(input(question))
             # if the answer is greter then 0 then it will return
             # the input as there response.
             if 0 < response:
                 return response
             else: # if the answer is less then 0 it will print the error.
                 print(error)
         except ValueError:
             print(error)

# The age variable is using the num check to find the persons age.
# it takes the question and the error message. 
age = num_check('How old are you? ','Thats not a Integer!?')
# Then prints out the age using the format method.
print('So you are {} years old.'.format(age))