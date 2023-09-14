months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

i = 1
months_dict={}
while i <=12:
    months_dict.update({months[i-1]: i})
    i +=1

while True:
    try:
        #Get the user's input
        date = input("Date: ")

        #Use get method, if it returns an error then we have the wrong info
        for i in months_dict:
            if date.split()[0] in i:
                month = int(months_dict.get(date.split()[0]))
                if ',' not in date:
                    continue
                first_half = (date.split(','))
                day = int(first_half[0].split()[1]) #You can also do day.replace(",", "")
                year = date.split()[2]

                if month is None:
                    continue
                elif int(day) > 31:
                    continue
                else:
                    print(year + "-" + f'{month:02}' + "-" + f'{day:02}', end="")
                    quit()


        if 1 <= int(date.split('/')[0]) <= 12 and 1 <= int(date.split('/')[1]) <= 31:
            month = int(date.split('/')[0])
            day = int(date.split('/')[1])
            year = int(date.split('/')[2])
            print(str(year) + "-" + f'{month:02}' + "-" + f'{day:02}')
            quit()

    except EOFError:
        exit()
    except (KeyError, TypeError, ValueError):
        pass

 