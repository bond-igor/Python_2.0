# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое
# представление. Функцию hex используйте для проверки своего результата.


HEX_FACTOR = 16
hex_data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']

enter_number = int(input('Введите целое число: '))

# метод конвертации из десятичной системы исчисления в шестнадцатиричную
def converter(number: int) -> str:
    res: str = ''
    while number > 0:
        res = str(hex_data[number % HEX_FACTOR]) + res
        number //= HEX_FACTOR
    return res

print(f"Результат конверсии в шестнадцатиричную систему: {converter(enter_number)}")

if converter(enter_number) == hex(enter_number)[2:]:
    print('Результат проверки через встроеный метод: OK')
else:
    print("Результат проверки через встроеный метод: Failed")
