def main():
    #Delete and leading or trailing whitespace
    #Make input case insensitive
    greeting = input().strip().lower().split()

    #We only care for the first letter of the first word
    #If we can split the input into a list of strings separated 
    #by spaces and search the first word for hello then we did it?
    
    if greeting[0].startswith("hello"):
        print("$0")
    elif greeting[0][0].startswith("h") and greeting[0] != "hello":
        print("$20")
    else:
        print("$100")

main()


#This answer technically works, but doesn't account for if the greeting has hello in the string BUT starts with something else 
#(ie. vbhsjfhbyvfsuhfvbshewhello) the example greeting would return 0. 

# answer = input("Greeting: ")

# new_answer = answer.lower().strip()

# if 'hello' in new_answer:
#     print("$0")
# elif 'h' == new_answer[0]:
#     print("$20")
# else:
#     print("$0")