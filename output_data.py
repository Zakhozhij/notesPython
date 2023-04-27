import csv
def get_notes():
    with open('notes/notes.csv','r', encoding='UTF8') as file:
        list_records = list(csv.reader(file))
        return list_records
    
def get_note_by_id(idNote):
    searchNote=''
    with open('notes/notes.csv','r', encoding='UTF8') as file:
        list_records = list(csv.reader(file))
        for i in list_records:
            if int("".join(i).split(';')[0])==idNote:
                searchNote=i
        return searchNote
    
def get_note_by_date(dateNote):
    searchNotes=[]
    with open('notes/notes.csv','r', encoding='UTF8') as file:
        list_records = list(csv.reader(file))
        for i in list_records:
            if str(("".join(i).split(';')[3]).split(' ')[0])==dateNote:
                searchNotes.append(i)
        return searchNotes
    

# def get_student_info(student_id):
#     student_name=''
#     with open('school/students.csv','r', encoding='UTF8') as file:
#         list_records = list(csv.reader(file))
#         for i in list_records:
#             if int("".join(i).split(';')[0])==student_id:
#                 student_name=" ".join(i).split(';')[1]
#     return student_name
