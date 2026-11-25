"""Задание 2. Циклы и базовые алгоритмические схемы."""
import random

measurements = [12, 15, 11, 18, 18, 9, 21, 15, 7, 18]


def analyze(values):
    """Этап 1: один проход - сумма, минимум, максимум, число четных."""
    total = 0
    minimum = values[0]
    maximum = values[0]
    even_count = 0
    for x in values:
        total += x
        if x < minimum:
            minimum = x
        if x > maximum:
            maximum = x
        if x % 2 == 0:
            even_count += 1
    return total, minimum, maximum, even_count


def count_above_mean(values, mean):
    """Этап 2: второй проход - сколько значений больше среднего."""
    count = 0
    for x in values:
        if x > mean:
            count += 1
    return count


def linear_search(values, target):
    """Возвращает (индекс первого вхождения или -1, число сравнений)."""
    comparisons = 0
    for i in range(len(values)):
        comparisons += 1
        if values[i] == target:
            return i, comparisons
    return -1, comparisons


def is_prime(n):
    """Проверка простоты: делители только до sqrt(n) включительно."""
    if n < 2:
        return False
    d = 2
    while d * d <= n:      # d <= sqrt(n) без вычисления корня
        if n % d == 0:
            return False
        d += 1
    return True


def selection_sort(values):
    """Сортировка выбором. Возвращает (новый список, число сравнений)."""
    result = list(values)   # исходный список не меняем
    comparisons = 0
    n = len(result)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if result[j] < result[min_index]:
                min_index = j
        result[i], result[min_index] = result[min_index], result[i]
    return result, comparisons


def binary_search(sorted_values, target):
    """Бинарный поиск. Возвращает (индекс или -1, число сравнений).

    За одно сравнение считается одна итерация: элемент в середине
    сравнивается с искомым (трехсторонне: меньше / равно / больше).
    """
    left = 0
    right = len(sorted_values) - 1
    comparisons = 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if sorted_values[mid] == target:
            return mid, comparisons
        elif sorted_values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons


def main():
    # --- статистика ---
    total, minimum, maximum, even_count = analyze(measurements)
    mean = total / len(measurements)
    above = count_above_mean(measurements, mean)
    print("Данные:", measurements)
    print(f"Сумма: {total}")
    print(f"Минимум: {minimum}, максимум: {maximum}")
    print(f"Четных значений: {even_count}")
    print(f"Среднее: {mean}, значений выше среднего: {above}")
    assert (total, minimum, maximum, even_count, above) == (144, 7, 21, 4, 6)

    # --- линейный поиск ---
    try:
        target = int(input("\nВведите число для поиска: "))
    except (EOFError, ValueError):
        target = 18
        print(f"\nВвод недоступен, ищем {target}")
    index, _ = linear_search(measurements, target)
    print(f"Первое вхождение {target}: {index}")
    assert linear_search(measurements, 18)[0] == 3
    assert linear_search(measurements, 12)[0] == 0
    assert linear_search(measurements, 100)[0] == -1

    # --- простые числа ---
    print("\nПроверка простоты:")
    for n in [1, 2, 3, 4, 17, 25, 49, 97, 100, 7919]:
        print(f"  {n}: {is_prime(n)}")
    assert [n for n in range(2, 30) if is_prime(n)] == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert not is_prime(1) and not is_prime(49) and is_prime(7919)

    # --- сортировка и сравнение поисков ---
    rng = random.Random(42)
    print("\nСравнение поисков (число сравнений):")
    print(f"{'n':>5} | {'сорт. выбором':>13} | {'линейный (последний)':>20} | "
          f"{'бинарный (последний)':>20} | {'линейный (нет)':>14} | {'бинарный (нет)':>14}")
    for n in [10, 100, 1000]:
        data = rng.sample(range(10000), n)
        sorted_data, sort_cmp = selection_sort(data)
        assert sorted_data == sorted(data)
        last = sorted_data[-1]
        missing = -1
        lin_last = linear_search(sorted_data, last)
        bin_last = binary_search(sorted_data, last)
        lin_miss = linear_search(sorted_data, missing)
        bin_miss = binary_search(sorted_data, missing)
        assert lin_last[0] == bin_last[0] == n - 1
        assert lin_miss[0] == bin_miss[0] == -1
        print(f"{n:>5} | {sort_cmp:>13} | {lin_last[1]:>20} | {bin_last[1]:>20} | "
              f"{lin_miss[1]:>14} | {bin_miss[1]:>14}")
    print("\nВсе проверки пройдены")


if __name__ == "__main__":
    main()
