from utils import BASE_DIR, sanitize_filename, EOF_MARKER

def create_file():
    name = input('Имя нового файла: ').strip()
    try:
        name = sanitize_filename(name)
    except ValueError as e:
        print('Ошибка:', e)
        return
    path = BASE_DIR / name
    if path.exists():
        print('Файл уже существует.')
        return
    print(f'Введите содержимое. Для окончания введите строку "{EOF_MARKER}"')
    lines = []
    while True:
        line = input()
        if line == EOF_MARKER:
            break
        lines.append(line)
    path.write_text("\n".join(lines), encoding="utf-8")
    print('Файл сохранён:', path)


def edit_file():
    name = input('Имя файла для редактирования: ').strip()
    try:
        name = sanitize_filename(name)
    except ValueError as e:
        print('Ошибка:', e)
        return
    path = BASE_DIR / name
    if not path.exists():
        print('Файл не найден')
        return
    text = path.read_text(encoding='utf-8')
    print('\nТекущее содержимое:\n---\n' + text + '\n---')
    print(f'Введите новый текст. Для окончания введите строку "{EOF_MARKER}"')
    lines = []
    while True:
        line = input()
        if line == EOF_MARKER:
            break
        lines.append(line)
    path.write_text("\n".join(lines), encoding="utf-8")
    print('Файл обновлён')


def search_in_file():
    """Поиск слова или фразы в файле"""
    name = input('Имя файла для поиска: ').strip()
    try:
        name = sanitize_filename(name)
    except ValueError as e:
        print('Ошибка:', e)
        return
    path = BASE_DIR / name
    if not path.exists():
        print('Файл не найден')
        return
    text = path.read_text(encoding="utf-8")
    query = input('Введите слово или фразу для поиска: ').strip()
    if not query:
        print('Пустой запрос')
        return

    lines = text.splitlines()
    found = False
    for i, line in enumerate(lines, 1):
        if query in line:
            print(f"Строка {i}: {line}")
            found = True
    if not found:
        print("Совпадений не найдено.")


def replace_in_file():
    """Замена текста в файле"""
    name = input('Имя файла для замены текста: ').strip()
    try:
        name = sanitize_filename(name)
    except ValueError as e:
        print('Ошибка:', e)
        return
    path = BASE_DIR / name
    if not path.exists():
        print('Файл не найден')
        return

    text = path.read_text(encoding="utf-8")
    old = input("Что заменить: ").strip()
    if not old:
        print("Пустая строка для поиска")
        return
    new = input("На что заменить: ")

    if old not in text:
        print("Совпадений не найдено.")
        return

    replaced_text = text.replace(old, new)
    path.write_text(replaced_text, encoding="utf-8")
    print(f'Все вхождения "{old}" заменены на "{new}". Файл обновлён.')
