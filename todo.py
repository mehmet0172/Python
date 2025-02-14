# todo.py

def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
    else:
        print("Список задач:")
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task['name']} {'(выполнено)' if task['completed'] else ''}")


def add_task(tasks, task_name):
    tasks.append({"name": task_name, "completed": False})


def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        print("Задача удалена.")
    else:
        print("Неверный индекс задачи.")


def complete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print("Задача помечена как выполненная.")
    else:
        print("Неверный индекс задачи.")


def main():
    tasks = []

    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Просмотреть все задачи")
        print("3. Удалить задачу")
        print("4. Пометить задачу как выполненную")
        print("5. Выход")

        choice = input("Выберите опцию (1-5): ")

        if choice == '1':
            task_name = input("Введите название задачи: ")
            add_task(tasks, task_name)
        elif choice == '2':
            show_tasks(tasks)
        elif choice == '3':
            task_index = int(input("Введите индекс задачи для удаления: ")) - 1
            remove_task(tasks, task_index)
        elif choice == '4':
            task_index = int(input("Введите индекс задачи для пометки как выполненной: ")) - 1
            complete_task(tasks, task_index)
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")


if __name__ == "__main__":
    main()