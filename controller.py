import add_notes as add_notes
import output_data as out_data
import view

def select_action():
    
    n=view.select_action()
    if n==1:
        add_note()
    elif n==2:
        get_all_notes()
    elif n==3:
        update_note()
    elif n==4:
        delete_note()
    elif n==5:
        find_note_by_id()
    elif n==6:
        find_note_by_date()
    if n!=7:
        select_action()

def add_note():
    data=view.add_note()
    add_notes.add_note(data)
    view.view_data(data)

def get_all_notes():
    data=out_data.get_notes()
    view.view_notes(data)

def update_note():
    idNote=int(input("Введите номер записи:"))
    data=view.add_note()
    dataStatus=add_notes.update_note(idNote,data)
    view.update_note_message(dataStatus)


def delete_note():
    idNote=int(input("Введите номер записи:"))
    dataStatus=add_notes.delete_note(idNote)
    view.delete_note_message(dataStatus)

def find_note_by_id():
    idNote=int(input("Введите номер записи:"))
    data=out_data.get_note_by_id(idNote)
    view.view_notes(data)

def find_note_by_date():
    dateNote=str(input("Введите дату в формате 00/00/0000 ->"))
    data=out_data.get_note_by_date(dateNote)
    view.view_notes(data)