username = input("Введите имя: ")
fitst_title =  input("Введите первый заголовок: ")
second_title = input("Введите второй заголовок (если не нужен оставьте пустым): ")
content = input("Введите описание: ")
status = input("Введите статус заметки: ")
created_date = input("Введите Дату создания в формате день, месяц ,год (10-10-2000): ")
issue_date = input("Введите Дату истечения заметки в формате день, месяц ,год (10-10-2000): ")

note_ = [
username, # indx = 0
content, # indx = 1
status, # indx = 2
created_date, # indx = 3
issue_date, # indx = 4
[fitst_title, second_title] # вложенный список для заголовков indx = 5
]

print("Здрастуйте,", note_[0])
print("Вот ваша заметка: ", note_[5][0], note_[5][1])
print(note_[1])
print("Дата создания: ", note_[3])
print("Дата изменения: ", note_[4])
