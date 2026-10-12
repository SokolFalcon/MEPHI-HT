admin = input("Введите ваше имя: ").strip()
print(f"Здравствуйте, {admin}! Открываем зрительское голосование")

films = ["дюна", "аватар", "матрица", "интерстеллар", "шрек"]
print("Фильмы в программе фестиваля:", ", ".join(films))

votes = {}
for film in films:
    votes[film] = 0

names = set()
common = set(films)
chosen = set()

while True:
    name = input('\nИмя зрителя (или "стоп", чтобы закончить): ').strip()
    name_lower = name.lower()

    if name_lower == "стоп":
        break

    if name == "":
        print("Имя не должно быть пустым")
        continue

    if name_lower in names:
        print(f"{name}, вы уже голосовали, второй голос не засчитан")
        continue

    text = input("Какие фильмы вам понравились (через запятую): ")

    liked = set()

    for film in text.split(","):
        film = film.strip().lower()

        if film == "":
            continue

        if film in votes:
            liked.add(film)
        else:
            print(f"Фильма «{film}» нет в программе, голос не засчитан")

    for film in liked:
        votes[film] += 1

    names.add(name_lower)

    # Оставляем фильмы, которые выбрал каждый зритель.
    common = common & liked

    # Собираем фильмы, которые выбрал хотя бы один зритель.
    chosen = chosen | liked

    print(f"Спасибо, {name}! Засчитано голосов: {len(liked)}")

print("\nИтоги голосования")
print(f"Проголосовало зрителей: {len(names)}")

for film in films:
    print(f"{film} - {votes[film]}")

if chosen:
    winner = films[0]

    for film in films:
        if votes[film] > votes[winner]:
            winner = film

    print(f"Победитель: {winner} ({votes[winner]})")
else:
    print("Победителя нет: ни одного голоса за фильмы не засчитано")

# Если зрителей не было, общих любимых фильмов тоже нет.
if not names:
    common = set()

not_chosen = set(films) - chosen

# Сохраняем порядок программы при выводе.
common_list = []
not_chosen_list = []

for film in films:
    if film in common:
        common_list.append(film)

    if film in not_chosen:
        not_chosen_list.append(film)

if common_list:
    print("Понравились всем:", ", ".join(common_list))
else:
    print("Понравились всем: таких фильмов нет")

if not_chosen_list:
    print("Не выбрал никто:", ", ".join(not_chosen_list))
else:
    print("Не выбрал никто: таких фильмов нет")

print(f"\nДо свидания, {admin}!")
