menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
while True: 
    #Get order, if it's not in menu, reprompt
    #If it's in the menu, print the total value 
    #(like a total = item + total)
    #figure out which errors to catch and catch 'em
    try: 
        food = input("Item: ").title()
    except EOFError:
        exit()
    except KeyError:
        pass
    else:
        for key in menu:
            if food in key:
                print(key)
                total = total + float(menu[key])
            else:
                continue
        print("Total: " + "$" + f"{total:.2f}")
