a = float(input("Введите первое число: "))

while 1:
    operation = (input('Введи операцию к ответному числу (+, -, *, /): '))
    # Введи "выход", если надо завершить программу
    if operation == "выход":
        print("Программа завершена")
        break
    b = float(input("Введите второе число: "))

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
    a = result
