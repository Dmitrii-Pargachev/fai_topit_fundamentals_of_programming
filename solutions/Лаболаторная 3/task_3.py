"""Задание 3. Коллекции и выбор структуры данных."""

submissions = [
    ("anna", "lab_01", 5),
    ("boris", "lab_01", 4),
    ("anna", "lab_02", 5),
    ("daria", "lab_01", 3),
    ("boris", "lab_02", 5),
    ("anna", "lab_01", 4),
]


def new_data():
    return {
        "students": set(),        # множество студентов
        "labs": set(),            # множество лабораторных
        "attempts": {},           # студент -> список результатов попыток
        "best": {},               # (студент, лаба) -> лучший результат
        "count": {},              # (студент, лаба) -> число попыток
    }


def add_submission(data, record):
    """Добавляет одну запись и обновляет все структуры без перестроения."""
    student, lab, score = record
    key = (student, lab)
    data["students"].add(student)
    data["labs"].add(lab)
    data["attempts"].setdefault(student, []).append(score)
    if key not in data["best"] or score > data["best"][key]:
        data["best"][key] = score
    data["count"][key] = data["count"].get(key, 0) + 1


def build_data(records):
    data = new_data()
    for record in records:
        add_submission(data, record)
    return data


def students_with_both(data, lab_a, lab_b):
    """Студенты, сдавшие обе работы (пересечение множеств)."""
    done_a = {s for (s, lab) in data["best"] if lab == lab_a}
    done_b = {s for (s, lab) in data["best"] if lab == lab_b}
    return done_a & done_b


def run_query(data, line):
    """Разбирает текстовую команду и выполняет запрос. Не падает на ошибках."""
    parts = line.split()
    if not parts:
        return "Пустая команда"
    command, args = parts[0], parts[1:]

    match command:
        case "student" if len(args) == 1:
            name = args[0]
            if name not in data["attempts"]:
                return f"Студент {name} не найден"
            return f"{name}: попытки {data['attempts'][name]}"
        case "best" if len(args) == 2:
            key = (args[0], args[1])
            if key not in data["best"]:
                return f"Нет данных для {key}"
            return f"Лучший результат {args[0]} по {args[1]}: {data['best'][key]}"
        case "attempts" if len(args) == 2:
            key = (args[0], args[1])
            if key not in data["count"]:
                return f"Нет данных для {key}"
            return f"Попыток у {args[0]} по {args[1]}: {data['count'][key]}"
        case "completed" if len(args) == 1:
            done = {s for (s, lab) in data["best"] if lab == args[0]}
            if not done:
                return f"Работу {args[0]} никто не сдавал"
            return f"{args[0]} сдали: {sorted(done)}"
        case "student" | "best" | "attempts" | "completed":
            return f"Неверное число аргументов для команды {command}"
        case _:
            return f"Неизвестная команда: {command}"


def main():
    data = build_data(submissions)
    print("Студенты:", sorted(data["students"]))
    print("Лабораторные:", sorted(data["labs"]))
    print("Попытки по студентам:", data["attempts"])
    print("Лучшие результаты:", data["best"])
    print("Число попыток:", data["count"])

    both = students_with_both(data, "lab_01", "lab_02")
    print("Сдавали обе работы:", sorted(both))
    assert both == {"anna", "boris"}
    assert data["best"][("anna", "lab_01")] == 5
    assert data["count"][("anna", "lab_01")] == 2
    assert data["students"] == {"anna", "boris", "daria"}

    # добавление новой записи без полной перестройки
    add_submission(data, ("daria", "lab_02", 4))
    add_submission(data, ("boris", "lab_01", 5))
    print("\nПосле добавления двух записей:")
    print("Сдавали обе работы:", sorted(students_with_both(data, "lab_01", "lab_02")))
    print("Лучшие результаты:", data["best"])
    print("Число попыток:", data["count"])
    assert data["best"][("boris", "lab_01")] == 5
    assert data["count"][("boris", "lab_01")] == 2
    assert students_with_both(data, "lab_01", "lab_02") == {"anna", "boris", "daria"}

    # текстовые запросы
    print("\nЗапросы:")
    queries = [
        "student anna",
        "best anna lab_01",
        "attempts boris lab_02",
        "completed lab_01",
        "student petr",
        "best anna lab_09",
        "completed lab_99",
        "best anna",
        "delete anna",
        "",
    ]
    for q in queries:
        print(f"> {q}")
        print(" ", run_query(data, q))
    assert run_query(data, "delete x") == "Неизвестная команда: delete"
    assert "не найден" in run_query(data, "student petr")


if __name__ == "__main__":
    main()
