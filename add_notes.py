from datetime import datetime
import csv
def add_note(data):
    with open('notes/notes.csv','a+', encoding='UTF8') as file:
        count_rows=len(open("notes/notes.csv", encoding='UTF8').readlines())
        for val in data:
            count_rows+=1
            file.write('{};{};{};\n'
                        .format(count_rows,val,datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

def update_note(idNote,data):
    noteStatus=0
    with open('notes/notes.csv','r', encoding='UTF8') as file:
        list_records = list(csv.reader(file))
        for i in list_records:
            if int("".join(i).split(';')[0])==idNote:
                list_records[idNote-1]="".join(i).split(';')[0]+";"+data[0]+";"+"".join(i).split(';')[3]
                noteStatus=1



    with open('notes/notes.csv','w', encoding='UTF8') as file:
        for val in list_records:
            file.write('{}\n'
                        .format("".join(val)))
    return noteStatus



def delete_note(idNote):
    noteStatus=0
    with open('notes/notes.csv','r', encoding='UTF8') as file:
        list_records = list(csv.reader(file))
        for i in list_records:
            if int("".join(i).split(';')[0])==idNote:
                list_records.remove(i)
                noteStatus=1
    with open('notes/notes.csv','w', encoding='UTF8') as file:
        count_rows=0
        for val in list_records:
            count_rows+=1
            new_val="".join(val)["".join(val).find(";") + 1 : ]

            file.write('{};{}\n'
                        .format(count_rows,new_val))
    return noteStatus