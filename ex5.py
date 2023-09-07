confectionery = {'Торт': ['Медовый', 4, 100], 'Пирожное': ['Рай', 7, 92], 'Маффин': ['Янтарный', 3, 76], 'Панкейки': ['Чудо', 7, 200]}
def display_menu():
    print("Меню:")
    print("1. Просмотреть описание")
    print("2. Просмотр цены")
    print("3. Просмотр количества")
    print("4. Просмотр всей информации")
    print("5. Покупка")
    print("6. Выход")
display_menu()
while True:
    choice = input("Выберите вариант 1-6: ")
    if choice == "1":
        print("Вы выбрали 1")
        for item, values in confectionery.items():
            description = values[0]
            print(f"{item}: {description}")
    elif choice == "2":
        print("Вы выбрали 2")
        for item, values in confectionery.items():
            price = values[1]
            print(f"{item}: {price} руб.")
    elif choice == "3":
        print("Вы выбрали 3")
        for item, values in confectionery.items():
            quantity = values[2]
            print(f"{item}: {quantity} шт.")
    elif choice == "4":
        print("Вы выбрали 4")
        for item, values in confectionery.items():
            description = values[0]
            price = values[1]
            quantity = values[2]
            print(f"{item}: {description}, {price} руб., {quantity} гр.")
    elif choice == "5":
        print("Вы выбрали 5")
        item = input("Введите название: ")
        if item in confectionery:
            values = confectionery[item]
            while True:
                num = input("Введите количество изделия, которое хотите приобрести: ")
                num = int(num)
                if num <= values[2]:
                    sum = num * values[1]
                    kol = values[2] - num
                    print(f"Сумма к оплате: {sum}")
                    print(f"Оставшееся количество изделий: {kol}")
                    break
                else:
                    print("Недостаточное количество изделий.")
                    choice = input("Хотите попробовать ещё раз? (Да/Нет): ")
                    if choice.lower() == "нет":
                        print("Выход из раздела покупки.")
                        break
    elif choice == "6":
        print("До свидания!")
        break
    else:
        print("Некорректный вариант. Пожалуйста, выберите снова.")