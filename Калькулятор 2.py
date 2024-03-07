if input == "выход":
    print("Программа завершена.")
    break

operation = input('Введите операцию (+, -, *, /): ')
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

result = 0
if operation == "+":
    result = a + b
elif operation == "-":
    result = a - b
elif operation == "*":
    result = a * b
elif operation == "/":
    result = a / b
else:
    print("Неизвестная операция")

print("Ответ: ", result)

while 1:
    operation = input('Введите операцию к ответному числу (+, -, *, /): ')
    b = float(input("Введите второе число: "))

    a = result
    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        result = a / b
    else:
        print("Неизвестная операция")

    print("Ответ: ", result)