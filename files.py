from utils import BASE_DIR, sanitize_filename

def list_files():
    files = sorted([f.name for f in BASE_DIR.iterdir() if f.is_file()])
    if not files:
        print('\n(папка пуста)')
    else:
        print('\nСписок файлов:')
        for i, name in enumerate(files, 1):
            size = (BASE_DIR / name).stat().st_size
            print(f'  {i}. {name}  ({size} bytes)')

def delete_file():
    name = input('Имя файла для удаления: ').strip()
    try:
        name = sanitize_filename(name)
    except ValueError as e:
        print('Ошибка:', e)
        return
    path = BASE_DIR / name
    if not path.exists():
        print('Файл не найден')
        return
    confirm = input(f'Удалить "{name}"? (да/нет): ').strip().lower()
    if confirm in ('да', 'yes', 'y'):
        path.unlink()
        print('Файл удалён')

def rename_file():
    old = input('Текущее имя файла: ').strip()
    try:
        old = sanitize_filename(old)
    except ValueError as e:
        print('Ошибка:', e)
        return
    old_path = BASE_DIR / old
    if not old_path.exists():
        print('Файл не найден')
        return
    new = input('Новое имя файла: ').strip()
    try:
        new = sanitize_filename(new)
    except ValueError as e:
        print('Ошибка:', e)
        return
    new_path = BASE_DIR / new
    if new_path.exists():
        print('Файл уже существует')
        return
    old_path.rename(new_path)
    print(f'Файл переименован: {old} -> {new}')
