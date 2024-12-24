note_ = {
    "username": input("Введите имя: "), # indx = 0
    "titles": [input("Введите первый заголовок: "), input("Введите второй заголовок (если не нужен оставьте пустым): ")], # вложенный список для заголовков indx = 1
    "content": input("Введите описание: "), # indx = 2
    "status": input("Cтатус заметки: "), # indx = 3
    "created_date": input("Введите Дату создания в формате день, месяц ,год (10-10-2000): "), # indx = 4
    "issue_date": input("Введите Дату истечения заметки в формате день, месяц ,год (10-10-2000): "), # indx = 5
}

print("Здрастуйте,", note_["username"])
print("Вот ваша заметка: ", note_["titles"][0], note_["titles"][1])
print("Описание: ", note_["content"])
print("Дата создания: ", note_["created_date"])
print("Дата истечения заметки: ", note_["issue_date"])
