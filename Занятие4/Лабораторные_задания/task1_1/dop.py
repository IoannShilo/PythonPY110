import re
def task():
    text = "1 + 10 = 11, 20 - 12 = 8, 7.5 / 2.5 = 3, 3 * 0.5 = 1.5, 0.05 + 6 = 6.05"
    word_pattern = re.compile(r"(?P<First_num>\d+.*)\b\s(?P<arif_symbol>.)\s(?P<Second_Number>\d+.*\d*)\s(\=)\s(?P<Result>\d+.*\d*)")

    for date in word_pattern.finditer(text):  # итератор по совпадениям
        print(date.groupdict())  # вернуть словарь с именованными группами
        print('------')


if __name__ == "__main__":
    task()