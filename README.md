# Scrapy Parser PEP

## Парсинг документов PEP
Асинхронный парсер собирающий данные о PEP с сайта `https://peps.python.org/`.
С каждой страницы PEP парсер собирает номер, название, статус и сохраняет
несколько файлов в формате `.csv` в папку `results`:
* Список PEP (номер, название и статус);
* Подсчитывает общее количество PEP для каждого статуса и количество всех PEP.

## Технологии проекта
* Python — высокоуровневый язык программирования.
* Scrapy — популярный фреймворк для парсинга веб сайтов.

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/Semavova/scrapy_parser_pep.git
```

Создать и активировать виртуальное окружение:
```bash
python -m venv env
```

```bash
source venv/Scripts/activate
```

Обновить менеджер пакетов pip и установить зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

## Запуск парсера
```bash
scrapy crawl pep
```

Автор: [Владимир Семочкин](https://github.com/Semavova)
