"""Задание 1. Условия и классификация данных."""

LEVELS = ["недостаточный", "удовлетворительный", "хороший", "отличный"]


def check_ranges(score, absences):
    """Проверяет диапазоны. Возвращает текст ошибки или None, если всё в порядке."""
    if score < 0 or score > 100:
        return "Ошибка: результат должен быть от 0 до 100"
    elif absences < 0 or absences > 5:
        return "Ошибка: число пропусков должно быть от 0 до 5"
    else:
        return None


def get_level(score, absences):
    """Определяет уровень результата с учетом пропусков."""
    # порядок важен: сначала самая высокая граница, поэтому нижние
    # границы («score <= 89» и т.п.) проверять не нужно
    if score >= 90:
        index = 3
    elif score >= 75:
        index = 2
    elif score >= 60:
        index = 1
    else:
        index = 0

    if absences > 3 and index > 0:
        index -= 1
    return LEVELS[index]


def describe_work(work_type):
    """Пояснение для типа работы (match / case)."""
    match work_type:
        case "exam":
            return "экзаменационная работа"
        case "project":
            return "проектная работа"
        case "practice":
            return "практическая работа"
        case _:
            return "неизвестный тип работы"


def process_record(score, work_type, absences):
    """Возвращает готовую строку результата для одной записи."""
    error = check_ranges(score, absences)
    if error is not None:
        return error
    level = get_level(score, absences)
    return f"{describe_work(work_type)}: {score} баллов, пропусков {absences} -> {level}"


def get_level_only(score, absences):
    """Уровень записи или None, если данные некорректны (для подсчета сводки)."""
    if check_ranges(score, absences) is not None:
        return None
    return get_level(score, absences)


# Часть 4. Тестовые сценарии: (score, work_type, absences, ожидаемый уровень)
TESTS = [
    (0, "exam", 0, "недостаточный"),
    (59, "project", 0, "недостаточный"),
    (60, "practice", 0, "удовлетворительный"),
    (74, "exam", 3, "удовлетворительный"),
    (75, "project", 0, "хороший"),
    (89, "practice", 4, "удовлетворительный"),
    (90, "exam", 0, "отличный"),
    (100, "exam", 5, "хороший"),
    (60, "project", 4, "недостаточный"),
    (30, "practice", 5, "недостаточный"),
]


def run_tests():
    print("Тестовые сценарии:")
    for score, work_type, absences, expected in TESTS:
        actual = get_level(score, absences)
        status = "OK" if actual == expected else "ОШИБКА"
        print(f"  {score:>3} | {work_type:<8} | {absences} | ожидали: {expected:<18} | получили: {actual:<18} | {status}")
        assert actual == expected
    # некорректные данные и неизвестный тип
    assert check_ranges(101, 0) is not None
    assert check_ranges(-1, 0) is not None
    assert check_ranges(50, 6) is not None
    assert check_ranges(50, -1) is not None
    assert describe_work("test") == "неизвестный тип работы"
    print("Все проверки пройдены\n")


def main():
    run_tests()

    # одна запись (в задании данные вводятся пользователем, здесь заданы вручную)
    score, work_type, absences = 82, "project", 4
    print("Одна запись:")
    print(process_record(score, work_type, absences))
    print(process_record(120, "exam", 0))
    print(process_record(70, "lab", 1))
    print()

    # практическое расширение: список записей
    records = [
        (95, "exam", 0),
        (88, "project", 1),
        (76, "practice", 4),
        (60, "exam", 2),
        (59, "project", 0),
        (74, "practice", 5),
        (100, "exam", 3),
        (0, "practice", 0),
        (89, "project", 2),
        (45, "exam", 4),
        (120, "exam", 1),
    ]

    print("Индивидуальные результаты:")
    lines = []
    for number, (score, work_type, absences) in enumerate(records, start=1):
        lines.append(f"{number}. {process_record(score, work_type, absences)}")
    for line in lines:
        print(line)

    summary = {level: 0 for level in LEVELS}
    invalid = 0
    for score, work_type, absences in records:
        level = get_level_only(score, absences)
        if level is None:
            invalid += 1
        else:
            summary[level] += 1

    print("\nСводка по уровням:")
    for level in reversed(LEVELS):
        print(f"  {level}: {summary[level]}")
    print(f"  некорректных записей: {invalid}")


if __name__ == "__main__":
    main()
