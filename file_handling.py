#OPENING file
f = open('./files/reading_file_example.txt', 'r') #the second parameter is the mode, if we don't erite it, deafult = 'r'
#modes: r, w, a (append), x (create), t (text, deafult), b (binary, for images)

whole_file = f.read() #all file text
ten_chars = f.read(10) #10 characters
line = f.readline() #one line, untile the newline \n
list_of_lines = f.readlines() #all text as list of lines ending with \n
#equal to
list_of_lines = f.read().splitlines()

#CLOSING a file
f.close()

#another way to open a file
with open('./files/reading_file_example.txt') as f:
    lines = f.readlines()
#automatically closes the file at the end of the scope

with open('./files/reading_file_example.txt', 'a') as f: #append
    f.write('appended text') 

with open('./files/reading_file_example.txt', 'w') as f: #overwrite (create a file if doesn't exist)
    f.write('appended text')

#deleting files
import os
# os.remove('./files/reading_file_example.txt') #error if doesn't exist


import json

#JSON TYPE FILE, every string is a dictionary
person_json = '''{ 
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}''' #key and values must be enclosed between ", not '. For readability we put ''' and change identation

#from JSON to dictionary
person_dict = json.loads(person_json) #load take an entire file
print(person_dict)

#from dictionary to JSON
person_json = json.dumps(person_dict)

person_json = '''{ 
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''

#writing a json file
with open('./files/json_file_example.json', 'w', encoding='utf-8') as f:
    json.dump(person_json, f, ensure_ascii=False, indent=4)

#CSV FILES
import csv
with open('./files/csv_example_file.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0: #first row
            print(f'the columns names are {', '.join(row)}')
            line_count+=1
        else:
            print(f'line {line_count}: {row[0]} is a teacher, he lives in {row[1]}, {row[2]} and loves {row[3]}')
            line_count+=1

#XLSX FILES
import xlrd

excel_book = xlrd.open_workbook('./files/file_example_XLS_10.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)

#EXERCISES
with open('./files/hacker_news.csv', 'r', encoding='utf-8') as f:
    csv_reader = csv.reader(f, delimiter=',')
    count_python = 0
    count_js = 0
    count_js_low = 0
    for row in csv_reader:
        python_flag = 0
        js_flag=0
        js_low_flag =0
        for cell in row:
            if (cell.lower().count('python') > 0 and python_flag == 0):
                count_python+=1
                python_flag+=1
            if (cell.lower().count('java') > 0 and js_low_flag == 0):
                count_js_low += cell.lower().count('java') #if we call count on a string, it founds every occurrence of the given substring (not word, but also together with other characters), on lists it founds the number of times that an entire element is present
                js_low_flag +=1
                if (cell.lower().count('javascript') > 0 and js_flag == 0):
                    count_js += cell.lower().count('javascript')
                    js_flag +=1
            if (python_flag ==1 and js_flag ==1 ):
                break
    print(f'the word python or Python is present {count_python} times, javascript JavaScript or Javascript is present {count_js} times and Java or java {count_js_low} times.\nThe difference between java and javascript is {count_js_low-count_js}')



