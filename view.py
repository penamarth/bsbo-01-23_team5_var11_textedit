from utils import BASE_DIR, sanitize_filename

def view_file():
    name = input('Имя файла для просмотра: ').strip()
    try:
        name = sanitize_filename(name)
    except ValueError as e:
        print('Ошибка:', e)
        return
    path = BASE_DIR / name
    if not path.exists():
        print('Файл не найден')
        return
    print('\n--- Содержимое файла ---')
    print(path.read_text(encoding='utf-8'))
    print('--- Конец файла ---\n')
