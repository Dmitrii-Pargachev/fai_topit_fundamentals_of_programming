"""Задание 5. Анализатор учебных результатов.

Правило для студента без результатов: среднее, минимум и максимум = None,
категория = «нет данных». Такой студент не участвует в общем среднем
и не может быть лидером, но попадает в статистику по категориям.
"""

students = {
    "Анна": [78, 91, 84, 88],
    "Борис": [60, 72, 68],
    "Дарья": [95, 93, 97, 90],
    "Илья": [55, 61],
}

CATEGORIES = ["отличный", "хороший", "удовлетворительный", "недостаточный", "нет данных"]


def mean(values):
    """Среднее. Вход: список чисел. Выход: float или None для пустого списка."""
    if not values:
        return None
    total = 0
    for v in values:
        total += v
    return total / len(values)


def minimum(values):
    """Минимум без min(). Для пустого списка возвращает None."""
    if not values:
        return None
    result = values[0]
    for v in values:
        if v < result:
            result = v
    return result


def maximum(values):
    """Максимум без max(). Для пустого списка возвращает None."""
    if not values:
        return None
    result = values[0]
    for v in values:
        if v > result:
            result = v
    return result


def classify(score):
    """Категория по баллу 0-100 (может быть дробным). None -> «нет данных»."""
    if score is None:
        return "нет данных"
    if score >= 90:
        return "отличный"
    if score >= 75:
        return "хороший"
    if score >= 60:
        return "удовлетворительный"
    return "недостаточный"


def student_summary(name, results):
    """Словарь с итогами одного студента. results не изменяется."""
    avg = mean(results)
    return {
        "name": name,
        "count": len(results),
        "mean": avg,
        "min": minimum(results),
        "max": maximum(results),
        "category": classify(avg),
    }


def group_summary(students):
    """Общая статистика группы. Пустая группа -> нули и mean = None."""
    summaries = [student_summary(name, results) for name, results in students.items()]
    categories = {c: 0 for c in CATEGORIES}
    means = []
    for s in summaries:
        categories[s["category"]] += 1
        if s["mean"] is not None:
            means.append(s["mean"])
    return {
        "students": summaries,
        "student_count": len(summaries),
        "group_mean": mean(means),
        "categories": categories,
    }


def find_top_students(students):
    """Имена студентов с наибольшим средним (может быть несколько)."""
    best = None
    top = []
    for name, results in students.items():
        avg = mean(results)
        if avg is None:
            continue
        if best is None or avg > best:
            best = avg
            top = [name]
        elif avg == best:
            top.append(name)
    return top


def make_rating(students):
    """Рейтинг по убыванию среднего (новый список, словарь не меняется)."""
    rated = []
    for name, results in students.items():
        avg = mean(results)
        if avg is not None:
            rated.append((name, avg))
    return sorted(rated, key=lambda pair: pair[1], reverse=True)


def format_report(student_data, group_data):
    """Итоговый текстовый отчет."""
    lines = []
    lines.append("Результаты студентов:")
    for s in student_data:
        if s["mean"] is None:
            lines.append(f"  {s['name']}: нет результатов ({s['category']})")
        else:
            lines.append(
                f"  {s['name']}: среднее {s['mean']:.2f}, мин {s['min']}, "
                f"макс {s['max']}, категория: {s['category']}"
            )
    lines.append("Категории:")
    for c in CATEGORIES:
        lines.append(f"  {c}: {group_data['categories'][c]}")
    if group_data["group_mean"] is None:
        lines.append("Общий средний результат группы: нет данных")
    else:
        lines.append(f"Общий средний результат группы: {group_data['group_mean']:.2f}")
    return "\n".join(lines)


def analyze(students):
    """Полный анализ группы: (отчет, лидеры, рейтинг)."""
    group = group_summary(students)
    report = format_report(group["students"], group)
    return report, find_top_students(students), make_rating(students)


def run_tests():
    # 1. обычный набор
    group = group_summary(students)
    assert group["student_count"] == 4
    assert find_top_students(students) == ["Дарья"]
    assert group["categories"]["отличный"] == 1
    assert group["categories"]["хороший"] == 1
    assert group["categories"]["удовлетворительный"] == 1
    assert group["categories"]["недостаточный"] == 1

    # 2. один студент
    one = {"Олег": [80, 90]}
    assert find_top_students(one) == ["Олег"]
    assert group_summary(one)["group_mean"] == 85

    # 3. несколько лидеров
    tie = {"А": [90, 80], "Б": [85, 85], "В": [70]}
    assert find_top_students(tie) == ["А", "Б"]

    # 4. пустая группа
    empty = {}
    g = group_summary(empty)
    assert g["student_count"] == 0 and g["group_mean"] is None
    assert find_top_students(empty) == []
    assert make_rating(empty) == []

    # 5. студент без результатов
    with_empty = {"Ира": [], "Паша": [70]}
    s = student_summary("Ира", [])
    assert s["mean"] is None and s["category"] == "нет данных"
    assert find_top_students(with_empty) == ["Паша"]
    assert group_summary(with_empty)["group_mean"] == 70

    # 6. границы категорий
    assert classify(90) == "отличный" and classify(89.99) == "хороший"
    assert classify(75) == "хороший" and classify(74.99) == "удовлетворительный"
    assert classify(60) == "удовлетворительный" and classify(59.99) == "недостаточный"
    assert classify(0) == "недостаточный" and classify(100) == "отличный"

    # исходные данные не изменились
    assert students["Илья"] == [55, 61] and list(students) == ["Анна", "Борис", "Дарья", "Илья"]
    print("Все сценарии пройдены (6)\n")


def main():
    run_tests()
    snapshot = {k: v[:] for k, v in students.items()}

    report, leaders, rating = analyze(students)
    print(report)
    print("Лидеры:", ", ".join(leaders))
    print("Рейтинг:")
    for place, (name, avg) in enumerate(rating, start=1):
        print(f"  {place}. {name} - {avg:.2f}")
    assert students == snapshot

    print("\nГруппа со студентом без результатов и с несколькими лидерами:")
    other = {"Ира": [], "Макс": [90, 80], "Нина": [85, 85]}
    report, leaders, rating = analyze(other)
    print(report)
    print("Лидеры:", ", ".join(leaders))

    print("\nПустая группа:")
    print(analyze({})[0])


if __name__ == "__main__":
    main()
