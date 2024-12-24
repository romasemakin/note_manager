username = input("Введите имя: ")
fitst_title =  input("Введите первый заголовок: ")
second_title = input("Введите второй заголовок (если не нужен оставьте пустым): ")
content = input("Введите описание: ")
status = input("Введите статус заметки: ")
created_date = input("Введите Дату создания в формате день, месяц ,год (10-10-2000): ")
issue_date = input("Введите Дату истечения заметки в формате день, месяц ,год (10-10-2000): ")

note_ = {
"username": username, # indx = 0
"content": content, # indx = 1
"status": status, # indx = 2
"created_date": created_date, # indx = 3
"issue_date": issue_date, # indx = 4
"titles": [fitst_title, second_title] # вложенный список для заголовков indx = 5
}

print("Здрастуйте,", note_["username"])
print("Вот ваша заметка: ", note_["titles"][0], note_["titles"][1])
print(note_["content"])
print("Дата создания: ", note_["created_date"])
print("Дата истечения заметки: ", note_["issue_date"])
