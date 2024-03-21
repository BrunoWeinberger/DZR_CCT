import random

random.seed()
random.randint(0, 10)

question_count = 0
action_count = 0
choice = input(print("Правда или действие?\n(введи \"Выход\",чтобы закончить) "))
while True:
    if question_count > 0:
        choice = input(print("Правда или действие? - "))
    elif action_count > 0:
        choice = input(print("Правда или действие? - "))
    if choice == "правда":
        question_count = question_count +1
        question = ("Когда ты последний раз врал и почему?",
                    "Какой сон у тебя был самым странным?",
                    "В какой ситуации ты испытывал самый сильный страх?",
                    "Если бы у вас была возможность пообщаться с любым человеком в мире, кто бы это был и о чем вы бы с ними поговорили?"
                    )
        random_question = random.choice(question)
        print(random_question)

    elif choice == "действие":
        action_count = action_count + 1
        action = ("Расскажи шутку", "Прыгни три раза на одной ноге", "Покажи обезъянку")
        random_action = random.choice(action)
        print(random_action)

    elif choice == "выход":
        if question_count == 0:
            print("Вы что-то мало сегодня играли")
        elif action_count == 0:
            print("Вы что-то мало сегодня играли")

        else:
            if question_count > action_count:
                stats = 100 / (question_count + action_count) * question_count
                print("Сегодня вы были на ", stats, "% правдивыми")
                # Вы были на н-о% правдивым

            elif question_count < action_count:
                stats = 100 / (question_count + action_count) * action_count
                print("Сегодня вы были на ", stats, "% активными")
                # Вы были на н-о% активным

        break
