def min_len_check(fn):
    def wrapper(*args, **kwargs):
        if len(*args, **kwargs) < 10:
            raise ValueError("Строка слишком короткая")
        result = fn(*args, **kwargs)
        return result

    return wrapper


@min_len_check
def some_func(str_arg: str):
    ...


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо

    some_func("Short str")  # ValueError("Строка слишком короткая")
