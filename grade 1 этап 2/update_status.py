status = 0 #статус заметки, от 0 до 2, 0 - отложено 1 - в процессе 2 - выполнено 

while True:
    if status == 0:
        print("Ваша заметка отложена")
    elif status == 1:
        print("Ваша заметка в процессе")
    elif status == 2:
        print("Ваша заметка выполнена") #вывод статуса

    print("Выберите статус заметки: ")
    print("0 - Отложена")
    print("1 - В процессе")
    print("2 - Выполнена")
    print("3 - Выход") #вывод меню

    status = int(input()) #выбор статуса

    if status == 3: #выход из программы
        break

    if status > 3: #если выбран несуществующий статус
        print("Выберете число от 0 до 3")
        status == 0
