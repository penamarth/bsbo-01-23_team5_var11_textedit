from utils import WELCOME
from files import list_files, delete_file, rename_file
from view import view_file
from edit import create_file, edit_file

def main_loop():
    print(WELCOME)
    while True:
        print('\nМеню:')
        print('  1) Список файлов')
        print('  2) Создать файл')
        print('  3) Просмотреть файл')
        print('  4) Редактировать файл')
        print('  5) Переименовать файл')
        print('  6) Удалить файл')
        print('  0) Выход')
        cmd = input('Выберите действие: ').strip()
        if cmd == '1':
            list_files()
        elif cmd == '2':
            create_file()
        elif cmd == '3':
            view_file()
        elif cmd == '4':
            edit_file()
        elif cmd == '5':
            rename_file()
        elif cmd == '6':
            delete_file()
        elif cmd == '0':
            print('Выход. До встречи!')
            break
        else:
            print('Неизвестная команда')
