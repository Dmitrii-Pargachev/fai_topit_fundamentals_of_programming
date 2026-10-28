import copy

print("=== Эксперимент A. Неизменяемый объект ===")
a = 10
b = a

print(a, b)
print(id(a), id(b))

a += 1

print(a, b)
print(id(a), id(b))

print()
print("=== Эксперимент B. Изменяемый объект ===")
first = [10, 20]
second = first

print(first, second)
print(id(first), id(second))

second.append(30)

print(first, second)
print(id(first), id(second))

# Дополнение: переназначение second на новый список с теми же элементами
second = list(first)
print("После переназначения second:")
print("first == second:", first == second)
print("first is second:", first is second)
print(id(first), id(second))

second.append(40)
print("После second.append(40):", first, second)
print("first изменился:", first != [10, 20, 30])

print()
print("=== Практическая задача. Конфигурации проекта ===")


def show(title, cfg_1, cfg_2):
    print(title)
    print("  config_1:", cfg_1)
    print("  config_2:", cfg_2)


config_1 = {
    "name": "Учебный проект",
    "members": ["Анна", "Борис"],
    "launch_params": [["debug", True], ["workers", 2]],
}

# 1. Простое присваивание -- общий объект
config_2 = config_1
show("До изменений (присваивание):", config_1, config_2)
config_2["members"].append("Виктор")
config_2["launch_params"][1][1] = 8
show("После изменений через config_2:", config_1, config_2)
print("  config_1 is config_2:", config_1 is config_2)
print("  Нежелательное совместное изменение: config_1 тоже изменился")

# 2. Независимая конфигурация -- глубокая копия
config_1 = {
    "name": "Учебный проект",
    "members": ["Анна", "Борис"],
    "launch_params": [["debug", True], ["workers", 2]],
}
config_2 = copy.deepcopy(config_1)
show("До изменений (deepcopy):", config_1, config_2)

config_2["name"] = "Копия проекта"
config_2["members"].append("Виктор")
config_2["launch_params"][1][1] = 8
show("После изменений через config_2:", config_1, config_2)

assert config_1 is not config_2
assert config_1["members"] is not config_2["members"]
assert config_1["launch_params"] is not config_2["launch_params"]
assert config_1["launch_params"][1] is not config_2["launch_params"][1]
assert config_1["members"] == ["Анна", "Борис"]
assert config_1["launch_params"] == [["debug", True], ["workers", 2]]
assert config_1["name"] == "Учебный проект"

print("Итог:")
print("  Присваивание: общими оказались весь словарь, список участников и вложенные списки параметров.")
print("  deepcopy: независимыми оказались все изменяемые объекты, assert подтвердил независимость.")
print("  Строка названия копируется по ссылке, но она неизменяема, поэтому общей проблемы не создает.")
