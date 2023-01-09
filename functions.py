from writeAndRead import open_file,rec_file


def search_student(data,inquiry):
    result =[]
    for i in data:
        flag = False
        for k ,v in i.items():
            if flag == False:
                if inquiry.lower() in str(v.lower()):
                    result.append(i)
                    flag = True
    return result
    

def editing(id):
    data = open_file()
    print("что хотите поменять?\n-1. Фамилию\n-2. Имя\n-3. Отчество\n-4. класс\n")
    comand =int(input())
    if comand==1:
        data[id]["Фамилия"] = rec_file(id,'Фамилия', input('Введите новую фамилию: '))
    elif comand==2:
        data[id]["Имя"] =rec_file(id,'Имя', input('Введите новое имя: '))
    elif comand==3:
        data[id]["Отчество"] =  rec_file(id,'Отчество', input('Введите Новое отчество: '))
    elif comand==4:
        data[id]["класс"] = rec_file(id,"Класс", str(input('Введите новый класс: ')))
        print('Изменения внесены!')
    else:
        print('не корректный ввод')


