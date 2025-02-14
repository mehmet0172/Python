"""
Вы разрабатываете систему фильтрации текстовых данных. Необходимо реализовать функцию, которая заменяет все гласные
буквы в тексте на символ . Текст написан на русском языке. Гласных букв в русском языке десять: «а», «у», «о», «и»,
 «э», «ы», «я», «ю», «е», «ё». Алгоритм должен игнорировать разницу между заглавной и строчной буквами, то есть «‎А»
  и «‎а» — один и тот же символ.‎ Формат ввода Одна строка текста. Длина строки от 1 до 100 символов.
  Строка может содержать буквы русского языка в разных регистрах, а также пробелы и специальные символы.
  Формат вывода Строка, в которой все гласные заменены на . В остальном — сохранено исходное написание,
  включая регистр, пробелы и специальные символы. Пример 1 Входные данные: Привет, мир!
  Выходные данные: Првт, м*р! Пример 2 Входные данные: ааааааа Выходные данные:

"""

def replace_vowels(input_string: str) -> str:
    vowels = 'ауоиэыяюеёАУОИЭЫЯЮЕЁ'
    result = ''
    for char in input_string:
        if char in vowels:
            result += '*'
        else:
            result += char
    return result

input_string = input()
result = replace_vowels(input_string)
print(result)

"""
The vowels variable contains all the vowel characters in Russian, both lowercase and uppercase.
The result variable is initialized as an empty string, which will store the modified input string.
The for loop iterates over each character in the input string.
For each character, the code checks if it is a vowel by checking if it is in the vowels string. 
If it is, the code appends a * to the result string. Otherwise, it appends the original character to the result string.
Finally, the modified result string is returned and printed to the console
"""

def filter_vowels(text: str) -> str:
    vowels = 'ауоиэыяюеёАУОИЭЫЯЮЕЁ'
    return ''.join('*' if char in vowels else char for char in text)

text = input()
result = filter_vowels(text)
print(result)

"""
In this code, the filter_vowels function takes a string as input and returns a new string where all vowels are 
replaced with *. The vowels variable contains all the vowel characters in Russian, both lowercase and uppercase. 
The return statement uses a generator expression to iterate over each character in the input string, replacing 
vowels with * and leaving other characters unchanged. The resulting string is then printed to the console.
"""
