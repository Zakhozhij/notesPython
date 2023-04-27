from random import randint
def select_action():
    print('----------------\
        \nВыберите действие:\
        \n1.Добавить заметку\
        \n2.Вывести список всех заметок\
        \n3.Редактировать заметку\
        \n4.Удалить заметку\
        \n5.Найти заметку по номеру\
        \n6.Найти заметки по дате\
        \n7.Выйти\n----------------')
    n=int(input("Введите n:"))
    return n

def view_data(data):
    print(f'{data}')

def add_note():
    add_note=[]
    title=str(input("Введите заголовок заметки:"))
    description=str(input("Введите тело заметки:"))
    add_note.append(title+";"+description)
    return add_note

def update_note_message(data):
    if data==1:
        print("Заметка обновлена")
    else:
        print("Ошибка обновления заметки (возможно ее не существует)")

def delete_note_message(data):
    if data==1:
        print("Заметка удалена")
    else:
        print("Ошибка удаления заметки (возможно ее не существует)")

def view_notes(data):
    if len(data)>0:
        for val in data:
         print(" ".join(" ".join(val).split(';')))
    else:
        print("Данных нет")