from text import print_menu
from writeAndRead import open_file
from functions import search_student, editing

def menu():
    while True:
        print('<<<Нажмите 9 для вызова меню>>>')
        operation = int(input())
        if operation == 0:
            break
        elif operation == 9:    
            print_menu()
        elif operation == 1:
            for i in range(len(open_file())):
                print(i+1, open_file()[i])
        elif operation == 2:
            print(search_student(open_file(), str(input('Поиск: '))))

        elif operation == 3:
            print('Какую запись будем корректировать?')
            for i in range(len(open_file())):
                print(i+1, open_file()[i])
            editing(int(input()))
        else:
            print('Некорректный ввод: ')
