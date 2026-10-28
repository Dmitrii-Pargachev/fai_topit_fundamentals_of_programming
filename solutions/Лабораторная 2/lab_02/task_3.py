import sys
import weakref

print("=== Подсчет ссылок ===")
data = [1, 2, 3]
print("После создания:", sys.getrefcount(data))

alias = data
print("После создания alias:", sys.getrefcount(data))

container = [data]
print("После помещения в контейнер:", sys.getrefcount(data))

del alias
print("После del alias:", sys.getrefcount(data))

container.clear()
print("После очистки контейнера:", sys.getrefcount(data))


print()
print("=== Слабая ссылка ===")


class Record:
    def __init__(self, name="record"):
        self.name = name

    def __repr__(self):
        return f"Record({self.name!r})"


record = Record()
weak_record = weakref.ref(record)

print(weak_record())
del record
print(weak_record())


print()
print("=== Практическая задача. Слабый реестр ===")
registry = weakref.WeakValueDictionary()

strong_1 = Record("first")
strong_2 = Record("second")
temp = Record("third")

registry["first"] = strong_1
registry["second"] = strong_2
registry["third"] = temp

print("Исходный состав реестра:", sorted(registry.keys()))

del temp
print("После удаления временной сильной ссылки (temp):", sorted(registry.keys()))
print("  third в реестре:", "third" in registry)

del strong_2
print("После удаления сильной ссылки strong_2:", sorted(registry.keys()))
print("  second в реестре:", "second" in registry)
print("  first в реестре:", "first" in registry, "->", registry.get("first"))

print("Вывод: реестр хранит только слабые ссылки, поэтому не продлевает жизнь объектов.")
