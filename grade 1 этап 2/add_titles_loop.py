titles = []

while True:
    titles.append(input("Введите заголовок: "))
    print(titles[-1])
    end = input("Для завершения введите stop: ")
    if end.lower() == "stop":
        break

print("Все заголовки: ", titles)