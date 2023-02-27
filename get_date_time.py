from datetime import date

today = date.today()

day = today.strftime('%d')
month = today.strftime('%m')
year = today.strftime('%Y')

heading = 'The current date is {}/{}/{}'.format(day,month,year)
filename = 'MMF_{}_{}_{}'.format(year,month,day)

print(heading)
print('The filename will be {}'.format(filename))