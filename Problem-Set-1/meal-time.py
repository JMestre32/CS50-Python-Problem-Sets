def main():
    time = input("What time is it? ").strip()
    meal = convert(time)
    if meal >= 7 and meal <= 8:
        print("breakfast time")
    elif meal >= 12 and meal <= 13:
        print("lunch time")
    elif meal >= 18 and meal <= 19:
        print("dinner time")
    else:
        exit()


def convert(time):
    new_time = (time.split(":"))
    return(float(new_time[0]) + float(new_time[1])/60)


if __name__ == "__main__":
    main()