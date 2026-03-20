### Hexlet tests and linter status:
[![Actions Status](https://github.com/DonDetta/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/DonDetta/python-project-50/actions)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=DonDetta_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=DonDetta_python-project-50)

## Gendiff

Утилита командной строки для сравнения двух конфигурационных файлов в форматах JSON и YAML. Показывает, что было добавлено, удалено или изменено между двумя файлами.

Поддерживаемые форматы вывода:
- **stylish** (по умолчанию) — древовидный diff с символами `+` / `-`
- **plain** — текстовое описание изменений
- **json** — структурированный JSON

### Требования

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) (менеджер пакетов)

### Установка

```bash
git clone https://github.com/DonDetta/python-project-50.git
cd python-project-50
uv sync
uv pip install -e .
```

### Запуск

```bash
gendiff file1.json file2.json
gendiff file1.yml file2.yml --format plain
gendiff file1.json file2.json --format json
```

Опции:
```
positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output (default: stylish)
```

### Демонстрация

[![asciicast](https://asciinema.org/a/cqLVfzMlNDobbRqR.svg)](https://asciinema.org/a/cqLVfzMlNDobbRqR)
[![asciicast](https://asciinema.org/a/2qRquPOI0SblK0bD.svg)](https://asciinema.org/a/2qRquPOI0SblK0bD)
[![asciicast](https://asciinema.org/a/rXu7cPhFZ2pG5W0Z.svg)](https://asciinema.org/a/rXu7cPhFZ2pG5W0Z)
[![asciicast](https://asciinema.org/a/vhTenUn2XDU5bGW1.svg)](https://asciinema.org/a/vhTenUn2XDU5bGW1)
[![asciicast](https://asciinema.org/a/ttk5MgdPhsWAUtR2.svg)](https://asciinema.org/a/ttk5MgdPhsWAUtR2)