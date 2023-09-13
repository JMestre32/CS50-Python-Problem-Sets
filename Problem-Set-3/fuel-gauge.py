while True:
    try:
        tank = (input("Fraction: ")).split('/')
        res = int(tank[0])/int(tank[1]) * 100
        if res >100:
            continue
    except (ValueError, ZeroDivisionError):
        pass
    else:
        if res <= 1:
            print("E")
            break
        elif res >= 99:
            print("F")
            break
        else:
            print(f"{res:.0f}%", sep="")
            break