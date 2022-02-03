import os

def file_directory():
    os.chdir('files')
    list_file = []
    for file in os.listdir(os.getcwd()):
        if file.endswith(".txt"):
            list_file.append(os.path.join(os.getcwd(), file))
    return list_file


def sort_files():
    string_qnt = {}
    for file in file_directory():
        name = os.path.basename(file)
        with open(file, 'r') as rf:
            string_qnt.update({name : len(rf.readlines())})
    list_files = list(string_qnt.items())
    list_files.sort(key=lambda i: i[1])
    return list_files


def write_file():
    out = ''
    for file in sort_files():
        with open(file[0]) as rf:
            out = out + f'''{file[0]}\n{file[1]}\n{rf.read()}\n'''
    os.chdir('..')
    with open('result.txt', 'w') as wf:
        wf.write(out)


write_file()


'''
Исходные файлы закидываются в директорию files
Итоговый файл сохраняется в корневую директорию программы с названием result.txt
'''
