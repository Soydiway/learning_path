races = ['human','elf','gnome']
classes = ['warrior','wizard','thief']
stat = {
    'intelligence (интеллект)': 0,
    'strength (сила)': 0,
    'agility (ловкость)': 0
    }
race_choice = None
class_choice = None
while True:
    a = 0
    b = 0
    scores = 15
    while a < len(races):
        print(f"{a + 1}. {races[a]}")
        a += 1
    try:
        character_race = int(input("Выберите расу из списка: "))
        if character_race > 3 or character_race < 1:
            print("Выберите номер расы из списка!")
            continue
        race_choice = races[character_race - 1]
    except ValueError:
        print("Выберие расу только по его номеру из списка")
        continue
    while b < len(classes):
        print(f"{b + 1}. {classes[b]}")
        b += 1
    try:
        character_class = int(input("Выберите класс из списка: "))
        if character_class > 3 or character_class < 1:
            print("Выберите номер класса из списка!")
            continue
        class_choice = classes[character_class - 1]
    except ValueError:
        print("Выберите класс только по его номеру из списка")
        continue
    if character_race == 2:
        stat['agility (ловкость)'] += 2
    elif character_race == 3:
        stat['strength (сила)'] += 2
    if character_class == 1:
        stat['strength (сила)'] += 3
    elif character_class == 2:
        stat['intelligence (интеллект)'] += 3
    else:
        stat['agility (ловкость)'] += 3
    while scores > 0:
        k = 0
        for key in stat:
            print(f"{k + 1}.{key} : {stat[key]}")
            k += 1
        try:
            stat_choice = int(input(f"У вас {scores} очков статы. Во что их хотите вложить (введите номер характеристики из списка сверху)? "))
            if stat_choice < 1 or stat_choice > 3:
                print("Выберите характеристику только из доступного списка!")
                continue
        except ValueError:
            print("Введите только число")
            continue
        if stat_choice == 1:
            while True:
                try:
                    choice_score = int(input(f"Сколько из имеющихся {scores} очков статы,хотите вложить в интеллект: "))
                    if choice_score > scores:
                        print("Вы не можете вложить в характеристику больше очков,чем имеете!")
                        continue
                    else:
                        scores -= choice_score
                        if (choice_score + stat['intelligence (интеллект)']) > 15:
                            stat['intelligence (интеллект)'] = 15
                        else:
                            stat['intelligence (интеллект)'] += choice_score
                        break
                except ValueError:
                    print(f'Введите только число')
                    continue
        if stat_choice == 2:
            while True:
                try:
                    choice_score = int(input(f"Сколько из имеющихся {scores} очков статы,хотите вложить в силу: "))
                    if choice_score > scores:
                        print("Вы не можете вложить в характеристику больше очков,чем имеете!")
                        continue
                    else:
                        scores -= choice_score
                        if (choice_score + stat['strength (сила)']) > 15:
                            stat['strength (сила)'] = 15
                        else:
                            stat['strength (сила)'] += choice_score
                        break
                except ValueError:
                    print(f'Введите только число')
                    continue
        if stat_choice == 3:
            while True:
                try:
                    choice_score = int(input(f"Сколько из имеющихся {scores} очков статы,хотите вложить в ловкость: "))
                    if choice_score > scores:
                        print("Вы не можете вложить в характеристику больше очков,чем имеете!")
                        continue
                    else:
                        scores -= choice_score
                        if (choice_score + stat['agility (ловкость)']) > 15:
                            stat['agility (ловкость)'] = 15
                        else:
                            stat['agility (ловкость)'] += choice_score
                        break
                except ValueError:
                    print(f'Введите только число')
                    continue
    break
character = {
    'Раса': race_choice,
    'Класс': class_choice,
    'Сила': stat['strength (сила)'],
    'Интеллект': stat['intelligence (интеллект)'],
    'Ловкость': stat['agility (ловкость)']
    }
print("=== ВАШ ГЕРОЙ ===")
for key in character:
    print(f"{key}: {character[key]}")
print('================')
