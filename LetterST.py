st = input("Введите строку: ")
letter = input("Введите символ: ")
l_1 = "None"
l_2 = "None"

positions = [str(index) for index, num in enumerate(st) if num == letter]

if positions:
    l_1 = positions[0]
    l_2 = positions[-1]
else:
    l_1 = "None"
    L_2 = "None"

print("Первый индекс символа \"", letter, "\" : ", l_1)
print("Последний индекс символа \"", letter, "\" : ", l_2)
