import json


def task(input_filename: str, output_filename: str) -> None:
    with open(input_filename) as f:
        python_object = json.load(f)

    with open(output_filename, 'w') as f:
        json.dump(python_object, f, indent=4)



if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
