import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_obgect = json.load(f)

    gen_exr = (item["contains_improvement_appeals"] for item in json_obgect)  # TODO записать выражение-генератор возвращающее значение по ключу contains_improvement_appeals
    return sum(gen_exr)


if __name__ == "__main__":
    print(task())
