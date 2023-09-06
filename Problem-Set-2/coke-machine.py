due = 50
while due > 0:
    while True:
        coin = int(input("Insert coin: "))
        if coin == 50:
            break
        elif coin == 25:
            break
        elif coin == 10:
            break
        elif coin == 5:
            break
        elif coin == 67899928212:
            print("ayyy")
    due = due - coin
    if due > 0:
        print("Amount due: " + str(due))

print("Change due: " + str(abs(due)))