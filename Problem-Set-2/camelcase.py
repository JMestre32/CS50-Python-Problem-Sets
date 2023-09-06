snake = input("camelCase: ")
print("snake_case: " , end="")
for i in snake:
    if i.isupper():
        i = '_' + i.lower()
    print(i, end="")