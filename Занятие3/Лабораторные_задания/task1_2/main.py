OUTPUT_FILE = "output.txt"


def task():
    with open(OUTPUT_FILE, "w") as f:
        for lestnica in range(1, 11):
            f.write(f"{lestnica * '*':>10}\n")


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
