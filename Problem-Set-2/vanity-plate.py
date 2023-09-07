def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #Ensure the plate's least 2 characters long and 6 characters max
    if len(s) < 2 or len(s) > 6:
        return False
    
    #Ensure the first two characters on the plate are letters
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    #Return false if a digit is in the middle of the plate
    i = 0
    while i < len(s):
        if s[i].isdigit() == True and s[i:].isdigit() == False:
            return False
        i += 1
    
    #Return false if the first digit on the plate is '0'
    i = 0

    #Iterate through s
    #If first instance of s[i] where s[i].isdigit is true
    #is == '0' return False
    #Otherwise, break out
    while i < len(s):
        print(s[i])
        if s[i].isdigit() == True:
            if s[i] == '0':
                return False
            else:
                break
        i +=1
        
        

    #Return false if there are punctuation marks in the plate
    for letter in s:
        if letter in [',', '.', '!', ' ', '?']:
            return False
        
    return True



main()

#Hint:
#Much like a list, a str is a “sequence” (of characters),
#which means it can be “sliced” into shorter strings with
# syntax like s[i:j]. For instance, if s is "CS50", then
#s[0:2] would be "CS".

