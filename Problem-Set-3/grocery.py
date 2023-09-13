#Initialize an empty dictionary
grocery_list = {}

#Prompt the user for input with an empty terminal




#Use an infinite while loop
i = 0
while True:
    try:
        list_item = input().upper()
        for key in grocery_list:
            if list_item in grocery_list:
                key["num"] = i + 1
        else:
            print("grocery_list dict: " + str(grocery_list))
            grocery_list["name"] = list_item
            grocery_list["num"] = i+1
    except EOFError:
        for key in grocery_list:
            print(grocery_list["name"] + " " + str(grocery_list["num"]))
            exit()
    except KeyError:
        print("key error")