import datetime

while True:
    user_input = input("Введите дату дедлайна (в формате день-месяц-год, например, 10-10-2000): ")

    if len(user_input.split("-")) == 3:
        day, month, year = user_input.split("-") #разделяем дату с помощью -
        
        if day.isdigit() and month.isdigit() and year.isdigit():
            try:
                issue_date = datetime.datetime(int(year), int(month), int(day)) #преоброзавание даты в формат datetime
                current_date = datetime.datetime.now() #текущая дата
                date = (issue_date - current_date).days  #проверяем дедлайн
                
                if date < 0:
                    print(f"Внимание! Дедлайн истёк {-date} дней назад!")
                elif date > 0:
                    print(f"До дедлайна осталось {date} дней")
                else:
                    print("Дедлайн сегодня!") #вывод сколько осталось до дедлайна
                
                print("Для выхода нажмите Enter") #выход
                input()
                break
            except ValueError:
                print("Ошибка: Неверная дата. Проверьте корректность дня, месяца и года") #это было очень сложно делать, долго гуглил но теперь если ввести неверный формат 2024-11-25 будет ошибка и код не сломается
        else:
            print("Ошибка: Дата должна содержать только цифры!")
    else:
        print("Ошибка: Неверный формат даты. Попробуйте снова")