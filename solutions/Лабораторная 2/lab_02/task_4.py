import gc
import sys
import weakref

print("=== Цикл из двух списков ===")
first = []
second = []

first.append(second)
second.append(first)

print("first ссылается на second:", first[0] is second)
print("second ссылается на first:", second[0] is first)

print("Автоматический сборщик включен:", gc.isenabled())
print("Пороги поколений:", gc.get_threshold())
print("Статистика поколений (до):")
for i, stats in enumerate(gc.get_stats()):
    print(f"  поколение {i}: {stats}")

print("Счетчик ссылок first (имя + second[0] + аргумент getrefcount):", sys.getrefcount(first))
print("Счетчик ссылок second:", sys.getrefcount(second))

first_id, second_id = id(first), id(second)
print("id списков:", first_id, second_id)

gc.collect()  # очищаем «фон», чтобы следующий результат относился только к циклу
del first, second
print("Имена удалены. Объекты недоступны из программы, но ссылаются друг на друга.")
collected = gc.collect()
print("gc.collect() вернул:", collected)

print("Статистика поколений (после):")
for i, stats in enumerate(gc.get_stats()):
    print(f"  поколение {i}: {stats}")


print()
print("=== Доказательство освобождения через weakref ===")


class Node:
    def __init__(self):
        self.other = None


n1, n2 = Node(), Node()
n1.other, n2.other = n2, n1
w1, w2 = weakref.ref(n1), weakref.ref(n2)
del n1, n2
print("После del (до gc.collect): живы ли объекты:", w1() is not None, w2() is not None)
gc.collect()
print("После gc.collect():        живы ли объекты:", w1() is not None, w2() is not None)


print()
print("=== Эксперимент с отключенным сборщиком ===")
gc.collect()
gc.disable()
try:
    print("Сборщик включен:", gc.isenabled())
    for _ in range(5):
        a, b = [], []
        a.append(b)
        b.append(a)
    # имена a и b перепривязывались на каждой итерации, поэтому внешних ссылок
    # на первые четыре цикла уже нет; удаляем ссылки на последний цикл
    del a, b
    print("Создано 5 циклов (10 списков), внешних ссылок не осталось")
    print("Выполняем ручную сборку...")
    manual = gc.collect()
    print("gc.collect() собрал объектов:", manual)
finally:
    gc.enable()
print("Сборщик включен снова:", gc.isenabled())


print()
print("=== Практическая задача. Граф из словарей и списков ===")


def make_node(name):
    return {"name": name, "links": []}


gc.collect()
before = gc.collect()
print("Собрано до создания графа:", before)

gc.disable()
try:
    node_a = make_node("A")
    node_b = make_node("B")
    node_c = make_node("C")
    node_d = make_node("D")  # независимый узел

    node_a["links"].append(node_b)
    node_b["links"].append(node_c)
    node_c["links"].append(node_a)

    for node in (node_a, node_b, node_c, node_d):
        print(f"  {node['name']} -> {[n['name'] for n in node['links']]}")

    del node_a, node_b, node_c
    after = gc.collect()
finally:
    gc.enable()

print("Собрано после удаления графа:", after)
assert node_d["name"] == "D" and node_d["links"] == []
print("Независимый узел D остался доступен:", node_d)
