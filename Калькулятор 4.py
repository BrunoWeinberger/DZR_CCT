a = float(input("Введите первое число: "))
if a == "выход":
    print("Программа завершена")
    exit()

while 1:
    operation = (input('Введи операцию к ответному числу (+, -, *, /): '))
    # Введи "выход", если надо завершить программу
    if operation == "выход":
        print("Программа завершена")
        break
    b = float(input("Введите второе число: "))
    if b == "выход":
        print("Программа завершена")
        exit()

    if operation == "+":
        result = a + b
    elif operation == "-":
        result = a - b
    elif operation == "*":
        result = a * b
    elif operation == "/":
        if a == 0:
            print("На 0 делить нельзя")
            exit()
        result = a / b
    else:
        print("Неизвестная операция")

    print("Ответ: ", result)
    a = result
