import sys
import tracemalloc

print("=== Часть 1. Размер отдельных объектов (sys.getsizeof) ===")
ten_numbers = list(range(10))
samples = [
    ("пустой список []", []),
    ("список из 10 целых", ten_numbers),
    ("кортеж из 10 целых", tuple(ten_numbers)),
    ("строка из 10 символов", "abcdefghij"),
    ("целое число 12345", 12345),
    ("None", None),
]
for title, obj in samples:
    print(f"{title:24}{sys.getsizeof(obj):>5} байт")

print()
print("=== Часть 2. Рост списка при append() ===")
growing = []
last_size = sys.getsizeof(growing)
print(f"len={len(growing):>3}  size={last_size} байт")
for i in range(100):
    growing.append(i)
    size = sys.getsizeof(growing)
    if size != last_size:
        print(f"len={len(growing):>3}  size={size} байт")
        last_size = size

print()
print("=== Часть 3. Измерение через tracemalloc ===")


def measure(title, factory):
    tracemalloc.start()
    numbers = factory()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(f"{title}")
    print(f"  тип: {type(numbers).__name__}, sys.getsizeof: {sys.getsizeof(numbers)} байт")
    print(f"  текущий объем: {current / 1024:.2f} КБ")
    print(f"  пиковый объем: {peak / 1024:.2f} КБ")
    return peak


peak_list = measure("list(range(100_000))", lambda: list(range(100_000)))
peak_range = measure("range(100_000)", lambda: range(100_000))
print(f"Отношение пиков list/range: {peak_list / peak_range:.0f}")
