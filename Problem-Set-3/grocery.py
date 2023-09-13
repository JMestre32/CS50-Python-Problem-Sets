#Initialize an empty dict
groceries = {}
while True: 
    try:
        item = input().upper()
        #Check to see if the item exists, if it does update it's item count
        if item in groceries:
            groceries.update({item: groceries[item] + 1})
        #Otherwise, add the item and initialize it's count to 1
        else:
            groceries.update({item: 1})
    except EOFError:
        #Take the keys in groceries and turn that into a list
        sorted = list(groceries.keys())
        #Sort the list of keys by alphabetical order using the list method sort()
        sorted.sort()

        #So, for each item, in the sorted list (line 16), the line below creates a key-value 
        #pair in the new sorted_dict whose keys are each item in the sorted list and whose 
        #values are the items corresponding counts from the groceries dict. 
        sorted_dict = {item: groceries[item] for item in sorted}

        #Print the sorted dict value first, then key
        for i in sorted_dict:
            print(sorted_dict[i], i)
        exit()
    except KeyError:
        pass

    #YAHOO, passed first time! We did consult help, but that's what you will have to do!
    #Don't beat yourself up for not knowing particular methods of sorting dictionaries, you're just
    #adding to your bag! :)