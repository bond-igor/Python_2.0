# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ —
# значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# reverse_kwargs(rev=True, acc="YES", stroka=4) -> {True: "rev", "YES": 'acc', 4: "stroka"}


def my_function(**kwargs):
    result = {}
    for k, v in kwargs.items():
        if isinstance(k, dict):
            result[str(v)] = k
        else:
            result[v] = k
    return result

print(my_function(rev=True, acc="YES", stroka=4))

