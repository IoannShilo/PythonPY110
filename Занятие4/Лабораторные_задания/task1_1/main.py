import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = r'####\s(?P<position>\d+).+\[(?P<book>.+)\]\((?P<book_url>\w+\://\w+.\w+/\w+)\)\s+by+\s+(?P<author>.+\b)\s+\((?P<recommended>.+)\s\w+\)\s+.+\((?P<cover_url>.+)\)\s+\"(?P<description>.+\s+.+\s+.+)\".+\s+' # TODO записать ругулярное выражения для поиска книги


def task():
    book_pattern = re.compile(BOOK_REGEX)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки

    with open(BOOKS_FILE, encoding="utf-8") as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))


if __name__ == '__main__':
    task()
