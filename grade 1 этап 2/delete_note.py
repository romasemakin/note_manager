notes_ = []  #список для хранения заметок

while True:
    print("Желаете добавить заметку?")
    print("1 - Добавить заметку")
    print("2 - Написать список заметок")
    print("3 - Удалить заметку")
    print("4 - Выход\n") #мнею выбора

    action = int(input("Выберите действие: ")) #выбор действия

    if action == 1: #добавление заметки
        note = {
            "Имя": input("Введите имя: "),
            "Заголовок": input("Введите заголовок: "),
            "Описание": input("Введите описание: "),
            "Статус": input("Введите статус заметки: "),
            "Дата создания": input("Введите дату создания (дд-мм-гггг): "),
            "Дедлайн": input("Введите дату истечения (дд-мм-гггг): ")
        }
        notes_.append(note)
        print("Заметка добавлена успешно!\n")

    elif action == 2: #вывод списка заметок
        if notes_: 
            print("Список заметок:")
            for i, note in enumerate(notes_, start=1):
                print(f"Заметка {i}.")
                print("Имя - " + notes_[i-1]["Имя"])
                print("Заголовок - " + notes_[i-1]["Заголовок"])
                print("Описание - " + notes_[i-1]["Описание"])
                print("Статус - " + notes_[i-1]["Статус"])
                print("Дата создания - " + notes_[i-1]["Дата создания"])
                print("Дедлайн - " + notes_[i-1]["Дедлайн"])
                print() 

        else:
            print("Список заметок пуст")

    elif action == 3: #удаление заметки
        print("Ведите номер заметки\n")
        print("Список заметок:")
        for i, note in enumerate(notes_, start=1):
            print(f"Заметка {i}.")
            print("Заголовок - " + notes_[i-1]["Заголовок"],"\n")

        delete_index = input("Введите номер заметки(для выхода нажмите Enter): ")
        delete_index =- 1

        if 0 <= delete_index < len(notes_):
            removed_note = notes_.pop(delete_index)
            print(f"Заметка с заголовком '{removed_note['Заголовок']}' удалена.\n")

        elif delete_index == None:
            continue
        
        else:
            print("Ошибка: такого номера заметки не существует. \n")

    elif action == 4: #выход из программы
        print("Выход из программы\n")
        break

    else: #если выбрано что-то не из списка
        print("Нет такого пункта меню\n")
