def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    
    i = 0
    if s[0:].isalpha():
        return True
    
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1

    for letter in s:
        if letter in [' ', '.', '!', '?']:
            return False
        

    for letter in range(len(s)):
        if s[0].isalpha() and s[1].isalpha():
            if len(s) == 2:
                return True
            elif len(s) ==3:
                return True
            elif len(s) == 4:
                if s[2].isdigit() and s[3].isdigit():
                    return True
            elif len(s) == 5:
                if s[2].isdigit() and s[3].isdigit() and s[4].isdigit():
                    return True
                elif s[3].isdigit() and s[4].isdigit():
                    return True
            elif len(s) ==6:
                if s[2].isdigit() and s[3].isdigit() and s[4].isdigit() and s[5].isdigit():
                    return True
                elif s[3].isdigit() and s[4].isdigit() and s[5].isdigit():
                    return True
                elif s[4].isdigit() and s[5].isdigit():
                    return True




#Hint:
#Much like a list, a str is a “sequence” (of characters),
#which means it can be “sliced” into shorter strings with
# syntax like s[i:j]. For instance, if s is "CS50", then
#s[0:2] would be "CS".

main()




    # while i <= len(s):
    #     if s[i].isalpha() == False:
    #         if s[i] == '0':
    #             return False
    #     i += 1
