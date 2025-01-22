import datetime
current_date = datetime.datetime.now().strftime("%d-%m-%Y") #текущая дата

def create_note(): #функция создания заметки
    note = {
            "username": input("Введите имя: "),
            "title": input("Введите заголовок: "),
            "content": input("Введите описание: "),
            "status": input("Введите статус заметки: "),
            "created_date": current_date,
            "issue_date": input("Введите дату истечения (дд-мм-гггг): ")
        }
    print("Имя - " + note["username"])
    print("Заголовок - " + note["title"])
    print("Описание - " + note["content"])
    print("Статус - " + note["status"])
    print("Дата создания - " + note["created_date"])
    print("Дедлайн - " + note["issue_date"])
    
create_note() #вызов функции