def main():
    time = input("What time is it? ").strip().split(":")
    meal = convert(time[0], time[1])
    if meal > 7 and meal < 8:
        print("breakfast time")
    elif meal > 12 and meal < 13:
        print("lunch time")
    elif meal > 18 and meal < 19:
        print("dinner time")
    else:
        exit()


def convert(hour, minute):
    return(float(hour) + float(minute)/60)


main()