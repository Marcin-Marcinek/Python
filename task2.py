#!/usr/bin/env python3
students = {"ted" : ['2', '4', '6'], "chad": ['3', '6', '2'], "rob": ['4','3','5']}
studentName = input("Which students grades would you want to know?")
studentName = studentName.lower()

if studentName in students:
    print(studentName + ' : ' + ' ' + '\n'.join(students[studentName]))
else:
    exit()


