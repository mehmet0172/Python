"""

Вы разрабатываете программу для проверки строк на палиндромы.
Палиндромом называется строка, которая читается одинаково как с начала, так и с конца.
При этом пробелы и регистр букв игнорируются. Напишите программу, которая определяет, является ли заданная строка
палиндромом. Формат ввода Одна строка, содержащая только строчные буквы русского алфавита и, в некоторых случаях,
пробелы. Длина строки от 2 до 100 символов включительно. Формат вывода Одна из двух фраз (без кавычек):
«Палиндром»‎ или «Не палиндром»‎. Пример 1 Входные данные: Тут как тут Выходные данные: Палиндром Пример 2 Входные
данные: Программист Выходные данные: Не палиндром
"""

def is_palindrome(input_string: str) -> str:
    input_string = input_string.replace(" ", "").lower()
    if input_string == input_string[::-1]:
        return "Палиндром"
    else:
        return "Не палиндром"

input_string = input()
result = is_palindrome(input_string)
print(result)


"""
The input_string.replace(" ", "").lower() line removes all spaces from the input string and converts it to lowercase, 
so that the palindrome check is case-insensitive and ignores spaces.
The input_string == input_string[::-1] line checks if the modified input string is equal to its reverse. If it is, 
then the string is a palindrome.
The if statement returns either "Палиндром" or "Не палиндром" depending on whether the string is a palindrome or not.
"""

def is_palindrome(input_string: str) -> bool:
    input_string = input_string.replace(" ", "").lower()
    return input_string == input_string[::-1]

input_string = input()
if is_palindrome(input_string):
    print('Палиндром')
else:
    print('Не палиндром')
"""
In this code, the is_palindrome function takes a string as input, removes all spaces, and converts it to lowercase. 
It then checks if the modified input string is equal to its reverse. If it is, the function returns True, 
indicating that the string is a palindrome. Otherwise, it returns False. The if statement then prints 
either "Палиндром" or "Не палиндром" depending on the result of the function call.
"""