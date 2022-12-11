# US Date to EU Date converter

months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'
}

input_date = input('Insert the date you want to convert:  ')

if '/' in input_date:
    date = input_date.split('/')

    date[0], date[1], = date[1], date[0]
    print(f'Your converted date is: {date[0]}/{date[1]}/{date[2]}')

else:
    for i in range(1, 13):
        if months[i] in input_date:
            date = input_date.split()
            mon = date[1].split(',')
            print(date)
