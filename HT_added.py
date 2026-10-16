import matplotlib.pyplot as plt

# Множество названий уже добавленных задач
task_names = set()

# Множества задач по приоритетам
priority_1 = set()
priority_2 = set()
priority_3 = set()

# Словарь количества задач каждого типа
task_types = {"feature": 0, "bug": 0}

# Счетчики задач и общей сложности
task_count = 0
total_complexity = 0

while True:
    name = input('\nНазвание задачи (или "стоп", чтобы закончить): ').strip()
    if name.lower() == "стоп":
        break
    if name.lower() in task_names:
        print("Задача уже добавлена, пропускаем")
        continue

    # Ввод сложности
    while True:
        complexity = input("Сложность задачи (от 0 до 10): ")
        if complexity.isdigit() and 0 <= int(complexity) <= 10:
            complexity = int(complexity)
            break
        else:
            print("Ошибка! Введите целое число от 0 до 10")

    # Ввод приоритета
    while True:
        priority = input("Приоритет (1, 2 или 3): ")
        if priority in ["1", "2", "3"]:
            priority = int(priority)
            break
        else:
            print("Ошибка! Введите приоритет 1, 2 или 3")

    # Ввод типа задачи
    while True:
        task_type = input("Тип задачи (feature или bug): ").strip().lower()
        if task_type == "feature" or task_type == "bug":
            break
        else:
            print("Ошибка! Введите feature или bug")

    # Добавляем задачу в множество
    task_names.add(name.lower())

    # Подсчитываем количество и сложность
    task_count += 1
    total_complexity += complexity

    # Распределяем задачи по приоритетам
    if priority == 1:
        priority_1.add(name)
    elif priority == 2:
        priority_2.add(name)
    else:
        priority_3.add(name)

    # Считаем количество задач каждого типа
    task_types[task_type] += 1

    print(f"Задача «{name}» добавлена!")

# Итоги спринта
print("\nИтоги спринта")

print(f"Количество задач: {task_count}")
print(f"Общая сложность: {total_complexity}")

print("Приоритет 1:", priority_1)
print("Приоритет 2:", priority_2)
print("Приоритет 3:", priority_3)

print("Количество задач по типам:", task_types)

# Круговая диаграмма
if task_count > 0:
    plt.pie(
        task_types.values(),
        labels=task_types.keys(),
        autopct="%1.1f%%",
        colors=["skyblue", "salmon"]
    )

    plt.title("Нагрузка спринта по типам задач")
    plt.show()
else:
    print("Задач нет, диаграмма не построена")