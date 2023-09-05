def main():    
    energy = int(input("m: "))
    e_converted = convert(energy)
    print(e_converted)

def convert(e):
    new = (e * pow(300000000, 2))
    return new


main()