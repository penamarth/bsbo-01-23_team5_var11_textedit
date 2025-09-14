import os
from pathlib import Path

BASE_DIR = Path.cwd() / 'documents'
BASE_DIR.mkdir(exist_ok=True)

EOF_MARKER = '.END'

WELCOME = f"""
=== Простой консольный текстовый редактор ===
Файлы хранятся в папке: {BASE_DIR}
"""

def sanitize_filename(name: str) -> str:
    name = os.path.basename(name)
    if not name or name.strip() == '':
        raise ValueError('Некорректное имя файла')
    if name.startswith('.'):
        raise ValueError('Имя файла не должно начинаться с точки')
    return name
