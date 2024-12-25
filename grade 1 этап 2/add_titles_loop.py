titles = []
runorno = "Да"

while True:
    titles.append(input("Введите заголовок: "))
    print(titles[-1])
    runorno = input("желаете добавить ещё заголовок? Да/Нет: ")
    if runorno == "Нет":
        break

print("Все заголовки: ", titles)