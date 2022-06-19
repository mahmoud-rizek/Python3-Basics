num1 = int(input("Enter first number: "))
opertator = input('Enter opertator: ')
num2 = int(input("Enter second number: "))


if opertator == '+':
    print(num1 + num2)

elif opertator == '-':
    print(num1 - num2)

elif opertator == '*':
    print(num1 * num2)

elif opertator == '/':
    print(num1 / num2)

elif opertator == '%':
    print(num1 % num2)

else:
    print('wrong opertator, try again')
