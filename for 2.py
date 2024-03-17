# в итоговую строку добавлять только чётные числа
result = ""
num_a = int(input("Введите делимое число: "))
num_b = int(input("Введите делящее число: "))
for i in range(0, num_a, num_b):
    result = result + str(i) + " "
    result_2 = result.split()
    total = sum(int(x) for x in result_2)

print("Числа: ", result)
print("       ", result_2)
print("Сумма полученных чисел", total)
