def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    #Find the dollar sign, drop it
    #Convert to float
   dolla = float(d.replace("$", ""))
   return dolla


def percent_to_float(p):
    #Similarly, find the percentage, drop it
    #Convert to float
    #Multiply by 0.01 to make it into a percentage
    percent = (float(p.replace("%", "")) * 0.01) 
    return percent


main()