
admin = input("Введите ваше имя: ").strip()
print(f"\nЗдравствуйте, {admin}! Открываем зрительское голосование")

films = ["дюна", "аватар", "матрица", "интерстеллар", "шрек"]

print("\nФильмы в программе фестиваля:", ", ".join(films))

# Создаем множество имен проголосовавших и словарь для фильма и количества голосов
voters = set()
votes = {}

for film in films:
    votes[film] = 0

# Множества для определения популярных и непопулярных фильмов
all_films = set(films)
popular_films = set(films)
selected_films = set() # хранит фильмы всех проголосовавших зрителей

while True:
    name = input('\nИмя зрителя (или "стоп", чтобы закончить): ').strip()

    if name.lower() == "стоп":
        break
    if name.lower() in voters:
        print(f"{name}, вы уже голосовали, второй голос не засчитан")
        continue

    voters.add(name.lower())

    answer = input("Какие фильмы вам понравились (через запятую): ")
    # множество понравившихся фильмов
    chosen_films = set()
    for film in answer.split(","):
        film = film.strip().lower()
        if film in films:
            chosen_films.add(film)
        elif film != "":
            print(f"Фильма «{film}» нет в программе, голос не засчитан")
    for film in chosen_films:
        votes[film] += 1
    
     # Пересечение и объединение множеств
    popular_films = popular_films & chosen_films
    selected_films = selected_films | chosen_films

    print(f"Спасибо, {name}! Засчитано голосов: {len(chosen_films)}")

print("\nИтоги голосования")

print(f"\nПроголосовало зрителей: {len(voters)}")

for film in films:
    print(f"{film} - {votes[film]}")

# Подсчет максимального количества голосов
max_votes = max(votes.values())

if max_votes > 0:
    for film in films:
        if votes[film] == max_votes:
            print(f"\nПобедитель: {film} ({max_votes})")
else:
    print("\nПобедитель не определён")

# Разность множеств, чтобы найти фильмы, за которые никто не голосовал
unpopular_films = all_films - selected_films

if len(voters) > 0 and popular_films:
    print("Понравились всем:", ", ".join(sorted(popular_films)))
else:
    print("Понравились всем: таких фильмов нет")

if unpopular_films:
    print("Не выбрал никто:", ", ".join(sorted(unpopular_films)))
else:
    print("Не выбрал никто: таких фильмов нет")

print(f"\nДо свидания, {admin}!")