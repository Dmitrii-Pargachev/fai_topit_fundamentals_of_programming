import sys
import tracemalloc

# 1. Размеры отдельных объектов (sys.getsizeof)
empty_list = []
list_10 = list(range(10))
tuple_10 = tuple(range(10))
str_10 = "abcdefghij"
num = 12345
none_obj = None

sizes = [
    {"scenario": "пустой список", "count": len(empty_list), "size": sys.getsizeof(empty_list)},
    {"scenario": "список из 10 чисел", "count": len(list_10), "size": sys.getsizeof(list_10)},
    {"scenario": "кортеж из 10 чисел", "count": len(tuple_10), "size": sys.getsizeof(tuple_10)},
    {"scenario": "строка из 10 символов", "count": len(str_10), "size": sys.getsizeof(str_10)},
    {"scenario": "целое число", "count": 1, "size": sys.getsizeof(num)},
    {"scenario": "None", "count": 1, "size": sys.getsizeof(none_obj)},
]

# 2. Рост списка при append()
data = []
last_size = sys.getsizeof(data)
grow = [{"length": len(data), "size": last_size, "diff": 0}]
for i in range(100):
    data.append(i)
    size = sys.getsizeof(data)
    if size != last_size:
        grow.append({"length": len(data), "size": size, "diff": size - last_size})
        last_size = size

# 3. Измерение через tracemalloc
N = 100_000
traced = []


def trace(scenario, factory):
    tracemalloc.start()
    obj = factory()
    current, peak = tracemalloc.get_traced_memory()
    size = sys.getsizeof(obj)  # размер внешнего объекта (не входит в трассировку)
    count = len(obj)
    tracemalloc.stop()
    traced.append({"scenario": scenario, "count": count, "size": size, "cur_b": current, "peak_b": peak})


trace("list(range(100_000))", lambda: list(range(N)))
trace("tuple(range(100_000))", lambda: tuple(range(N)))
trace("range(100_000)", lambda: range(N))

list_row, range_row = traced[0], traced[2]
peak_ratio = list_row["peak_b"] / range_row["peak_b"] if range_row["peak_b"] else float("inf")

# Вывод отчета
print("Часть 1. Размеры отдельных объектов")
for row in sizes:
    print(row["scenario"], "| элементов:", row["count"], "| размер в байтах:", row["size"])

print()

print("Часть 2. Рост списка")
for row in grow:
    print("длина:", row["length"], "| размер в байтах:", row["size"], "| разница с предыдущим:", row["diff"])

print()

print("Часть 3. Измерение через tracemalloc")
for row in traced:
    print(row["scenario"], "| элементов:", row["count"], "| размер в байтах:", row["size"])
    print("Current memory: %.2f KB" % (row["cur_b"] / 1024))
    print("Peak memory:    %.2f KB" % (row["peak_b"] / 1024))
    print()

print("Отношение пиковых объемов (list / range): %.1f" % peak_ratio)
print("Отношение пиковых объемов (tuple / range): %.1f" % (traced[1]["peak_b"] / range_row["peak_b"]))
