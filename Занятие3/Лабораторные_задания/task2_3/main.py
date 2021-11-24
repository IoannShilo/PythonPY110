import json


def task():
    filename = "input.json"
    with open(filename) as f:
        json_obj = json.load(f)

    return max(json_obj, key=lambda item: item["score"])


if __name__ == "__main__":
    print(task())
