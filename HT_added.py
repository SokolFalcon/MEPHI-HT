# Установка библиотеки: python -m pip install matplotlib
import matplotlib.pyplot as plt


names = set()
tasks = {1: set(), 2: set(), 3: set()}
types = {"feature": 0, "bug": 0}
total = 0

while True:
    name = input('\nНазвание задачи (или "стоп", чтобы закончить): ').strip()
    name_lower = name.lower()

    if name_lower == "стоп":
        break

    if name == "":
        print("Название не должно быть пустым")
        continue

    if name_lower in names:
        print("Задача уже добавлена, пропускаем")
        continue

    while True:
        try:
            points = int(input("Сложность (от 0 до 10): "))
        except ValueError:
            print("Ошибка: введите целое число от 0 до 10")
            continue

        if 0 <= points <= 10:
            break

        print("Ошибка: сложность должна быть от 0 до 10")

    while True:
        try:
            priority = int(input("Приоритет (1, 2 или 3): "))
        except ValueError:
            print("Ошибка: введите целое число 1, 2 или 3")
            continue

        if priority in tasks:
            break

        print("Ошибка: приоритет должен быть 1, 2 или 3")

    while True:
        task_type = input("Тип (feature или bug): ").strip().lower()

        if task_type in types:
            break

        print("Ошибка: тип должен быть feature или bug")

    names.add(name_lower)
    tasks[priority].add(name)
    total += points
    types[task_type] += 1

    print("Задача добавлена")

print("\nНагрузка спринта на 2 недели")
print(f"Количество задач: {len(names)}")
print(f"Общая сложность: {total}")

for priority in tasks:
    print(f"Приоритет {priority}: {tasks[priority]}")

print("Количество задач по типам:", types)

if names:
    plt.figure(figsize=(7, 6))
    plt.pie(
        types.values(),
        labels=types.keys(),
        autopct="%1.1f%%",
        colors=["#66b3ff", "#ff9999"],
    )
    plt.title("Нагрузка спринта по типам задач")
    plt.axis("equal")
    plt.tight_layout()
    plt.show()
else:
    print("Задач нет, диаграмма не построена")
