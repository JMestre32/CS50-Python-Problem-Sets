due = 50
while due > 0:
    coin = int(input("Insert Coin: "))
    if coin == 50:
        due = due - coin
    elif coin == 25:
        due = due - coin
    elif coin == 10:
        due = due - coin
    elif coin == 5:
        due = due - coin
    if due > 0:
        print("Amount Due: " + str(due))

print("Change Owed: " + str(abs(due)))

#if/elif could be written like so:
#if coin in [50, 25, 10, 5]:
    #due -= coin