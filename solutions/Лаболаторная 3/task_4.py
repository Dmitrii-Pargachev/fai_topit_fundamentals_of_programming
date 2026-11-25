"""Задание 4. Функции, параметры и области видимости."""


def arithmetic_mean(values: list[float]) -> float:
    """Возвращает среднее арифметическое непустого списка.

    Для пустого списка контракт выполнить нельзя, возвращается 0.0.
    """
    if not values:
        return 0.0
    return sum(values) / len(values)


def normalize_name(name: str) -> str:
    """Удаляет лишние пробелы и приводит каждую часть имени к нужному регистру."""
    parts = name.split()
    if not parts:
        return ""
    return " ".join(part.capitalize() for part in parts)


def build_report(
    student: str,
    results: list[int],
    *,
    precision: int = 2,
    prefix: str = "Результат",
) -> str:
    """Формирует строковый отчет о результатах студента."""
    name = normalize_name(student)
    if not results:
        return f"{prefix}: {name} - нет результатов"
    mean = arithmetic_mean(results)
    return f"{prefix}: {name}, среднее {mean:.{precision}f}, работ {len(results)}"


def collect_tags(*tags: str, lowercase: bool = True) -> tuple[str, ...]:
    """Возвращает очищенные теги без пустых значений и повторов."""
    result = []
    for tag in tags:
        clean = tag.strip()
        if lowercase:
            clean = clean.lower()
        if clean and clean not in result:
            result.append(clean)
    return tuple(result)


# ---------- проверки ----------
def run_asserts():
    # arithmetic_mean
    assert arithmetic_mean([1, 2, 3]) == 2
    assert arithmetic_mean([5]) == 5
    assert arithmetic_mean([]) == 0.0
    assert arithmetic_mean([1.5, 2.5]) == 2.0

    # normalize_name
    assert normalize_name("  иВАНов   иВАН ") == "Иванов Иван"
    assert normalize_name("anna") == "Anna"
    assert normalize_name("   ") == ""

    # build_report
    assert build_report("анна", [4, 5]) == "Результат: Анна, среднее 4.50, работ 2"
    assert build_report("анна", [4, 5], precision=0) == "Результат: Анна, среднее 4, работ 2"
    assert build_report("борис", []) == "Результат: Борис - нет результатов"
    assert build_report("борис", [3], prefix="Итог") == "Итог: Борис, среднее 3.00, работ 1"

    # collect_tags
    assert collect_tags("Python", " python ", "", "Code") == ("python", "code")
    assert collect_tags("A", "a", lowercase=False) == ("A", "a")
    assert collect_tags() == ()

    # исходные коллекции не меняются
    data = [4, 5, 3]
    copy = data[:]
    arithmetic_mean(data)
    build_report("x", data)
    assert data == copy


# ---------- LEGB ----------
course = "Python"                      # G: глобальное имя


def outer():
    attempts = 0                       # E: имя объемлющей функции
    topic = "функции"                  # E

    def inner():
        nonlocal attempts              # изменяем имя из outer
        attempts += 1
        message = f"{course}, {topic}, попытка {attempts}"   # L: message; E: topic, attempts; G: course
        return message, len(message)   # B: len - встроенное имя

    print(inner()[0])
    print(inner()[0])
    return attempts


# ---------- изменяемое значение по умолчанию ----------
def add_result_bad(value, results=[]):
    results.append(value)
    return results


def add_result(value, results=None):
    if results is None:
        results = []
    else:
        results = list(results)        # исходный список не меняем
    results.append(value)
    return results


# ---------- практическое расширение ----------
def apply_to_results(operation, values):
    """Применяет функцию к каждому результату, не меняя исходную последовательность."""
    return [operation(v) for v in values]


def square(x):
    return x * x


def make_threshold_checker(threshold):
    def check(score):
        return score >= threshold      # threshold хранится в замыкании
    return check


def main():
    run_asserts()
    print("Все assert пройдены\n")

    print("Позиционные и именованные аргументы:")
    print(build_report("иванов иван", [5, 4, 4]))
    print(build_report("иванов иван", [5, 4, 4], precision=1, prefix="Итог"))
    print(collect_tags("Python", "  code ", "python", ""))
    print(collect_tags("Python", "Python", lowercase=False))

    print("\nРаспаковка * и **:")
    args = ["петров пётр", [3, 4, 5]]
    kwargs = {"precision": 0, "prefix": "Оценка"}
    print(build_report(*args, **kwargs))
    tags = ["a", "B", "a"]
    print(collect_tags(*tags))

    print("\nLEGB:")
    result = outer()
    print("attempts после outer():", result)
    print("глобальный course не изменился:", course)

    print("\nИзменяемое значение по умолчанию:")
    print(add_result_bad(1), add_result_bad(2), add_result_bad(3))
    print(add_result(1), add_result(2), add_result(3))
    old = [10]
    print(add_result(20, old), "исходный:", old)
    assert add_result(1) == [1] and add_result(2) == [2]

    print("\nФункции как аргументы:")
    scores = [50, 65, 80, 95]
    print(apply_to_results(square, scores))
    print(apply_to_results(lambda x: x + 5, scores))

    passed_60 = make_threshold_checker(60)
    passed_90 = make_threshold_checker(90)
    print("порог 60:", [passed_60(s) for s in scores])
    print("порог 90:", [passed_90(s) for s in scores])
    assert passed_60(60) and not passed_90(60)
    print("значения в замыканиях:", passed_60.__closure__[0].cell_contents,
          passed_90.__closure__[0].cell_contents)


if __name__ == "__main__":
    main()
