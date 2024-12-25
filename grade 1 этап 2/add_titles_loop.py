titles = []
runorno = "Да"

while True:
    titles.append(input("Введите заголовок: "))
    print(titles[-1])

    runorno = input("желаете добавить ещё заголовок? Да/Нет: ")

    if runorno == "Да":
        continue
    else:   
        if runorno == "Нет":
            break
        
    if runorno != "Да" or "Нет":
        runorno = input("Введите Да/Нет: ")
    else:
        break

print("Все заголовки: ", titles)