"""Преподаватель отправил студентам ведомости с оценками за экзамен.
Максимальный балл за экзамен — 100. Определите количество студентов, сдавших экзамен на отлично (50 баллов и выше),
хорошо (35–49 баллов) и неудовлетворительно (менее 35 баллов). Формат ввода Одна строка: целые числа,
разделенные запятыми, означающие баллы учеников (1 ≤ x ≤ 100). Формат вывода Количество студентов по категориям:
Отлично, Хорошо и Неудовлетворительно. Каждая группа должна начинаться с новой строки, и выдаваться в формате
«Оценка: 3» (без кавычек), где цифра — количество студентов, получивших эту оценку. Если никто не набрал баллы
в определенной категории, будет «Оценка: 0» (без кавычек). Пример 1 Входные данные: 0,40,55,34 Выходные данные:
Отлично: 1 Хорошо: 1 Неудовлетворительно: 2 Пример 2 Входные данные: 55,55,55,55,55,55 Выходные данные: Отлично: 6
Хорошо: 0 Неудовлетворительно: 0
"""

def count_grades():
    grades = list(map(int, input().split(',')))
    excellent_count = sum(1 for grade in grades if grade >= 50)
    good_count = sum(1 for grade in grades if 35 <= grade < 50)
    poor_count = sum(1 for grade in grades if grade < 35)
    print(f"Отлично: {excellent_count}")
    print(f"Хорошо: {good_count}")
    print(f"Неудовлетворительно: {poor_count}")

count_grades()

"""
The input() function reads a line of input from the user, which is a comma-separated list of grades.
The map() function converts each grade to an integer, and the list() function converts the resulting iterator to a list.
The sum() function is used to count the number of grades in each category:
excellent_count counts the number of grades 50 or higher.
good_count counts the number of grades between 35 and 49 (inclusive).
poor_count counts the number of grades less than 35.
The print() function is used to output the counts for each category, with each category on a new line.
"""
def categorize_students(scores_input: str) -> str:
    scores = list(map(int, scores_input.split(',')))
    excellent_count = sum(1 for score in scores if score >= 50)
    good_count = sum(1 for score in scores if 35 <= score < 50)
    poor_count = sum(1 for score in scores if score < 35)
    result = f"Отлично: {excellent_count}\nХорошо: {good_count}\nНеудовлетворительно: {poor_count}"
    return result

scores_input = input()
result = categorize_students(scores_input)
print(result)

