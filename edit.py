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
