status = 0

while True:
    if status == 0:
        print("Ваша заметка отложена")
    elif status == 1:
        print("Ваша заметка в процессе")
    elif status == 2:
        print("Ваша заметка выполнена")

    print("Выберите статус заметки: ")
    print("0 - Отложена")
    print("1 - В процессе")
    print("2 - Выполнена")
    print("3 - Выход")

    status = int(input())

    if status == 3:
        break
