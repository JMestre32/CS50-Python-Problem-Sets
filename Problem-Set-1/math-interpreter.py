expr = input("Expression: ").strip().split()

x = expr[0]
y = expr[1]
z = expr[2]

if y == '+':
    print(float(x) + float(y))
elif y == '-':
    print(float(x) - float(y))
elif y == '*':
    print(float(x) * float(y))
elif y == '/':
    print(float(x) / float(y))    