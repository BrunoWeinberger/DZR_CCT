# Строки. Методы строк.
# Попробовать использовать методы, перечисленные ниже, по аналогии с работой на занятии.
# В результате должен получиться файл, в котором выполняются перечисленные ниже команды
# с комментариями по ходу выполнения.

text_example = input("Введите какой-нибудь текст на проверку: \n")

# S.islower()  # Состоит ли строка из символов в нижнем регистре
count_lowercase = 0
count_uppercase = 0
for s in text_example:
    if s.islower():
        count_lowercase += 1

    # - s.isupper()  # Состоит ли строка из символов в верхнем регистре
    elif s.isupper():
        count_uppercase = count_uppercase + 1


# S.upper()  # Преобразование строки к верхнему регистру
uppercase_text = text_example.upper()

# S.lower()  # Преобразование строки к нижнему регистру
lowercase_text = text_example.lower()

# S.title()  # Первую букву каждого слова переводит в верх. регистр, остальные в нижний
titled_text = text_example.title()

# S.capitalize()  # Переводит первый символ строки в верхний регистр, остальные в нижний
capitalized_text = text_example.capitalize()

if count_lowercase == 0:
    print("\nПрописных букв не наблюдается \n")
else:
    print("\nЕсть прописные буквы")
    print("в количестве ", count_lowercase, " штук \n")

if count_uppercase == 0:
    print("Заглавных букв не наблюдается \n")
else:
    print("Есть заглавные буквы")
    print("В количестве ", count_uppercase, " штук \n")

if text_example[0].istitle():
    print("Предложение начинается с заглавной буквы \n")
else:
    print("Предложение не начинается с заглавной буквы \n")

print("Данный текст заглавными буквами:")
print('\"', uppercase_text, '\" \n')

print("Данный текст строчными буквами:")
print('\"', lowercase_text, '\" \n')

print("Текст с заглавными первыми буквами в каждом слове:")
print('\"', titled_text, '\" \n')

print("Текст с одной заглавной буквой в начале предложения:")
print('\"', capitalized_text, '\" \n')
