import copy

original = [
    ["Python", 5],
    ["Algorithms", 4],
]

alias = original
shallow = original.copy()
deep = copy.deepcopy(original)


def show_state(title):
    print(f"--- {title} ---")
    print("original:", original)
    print("alias:   ", alias)
    print("shallow: ", shallow)
    print("deep:    ", deep)
    print("id внешних списков:")
    for name, obj in (("original", original), ("alias", alias), ("shallow", shallow), ("deep", deep)):
        print(f"  {name:9}{id(obj)}")
    print("id первого вложенного списка:")
    for name, obj in (("original", original), ("alias", alias), ("shallow", shallow), ("deep", deep)):
        print(f"  {name:9}{id(obj[0])}")
    print("id объекта первой оценки:")
    for name, obj in (("original", original), ("alias", alias), ("shallow", shallow), ("deep", deep)):
        print(f"  {name:9}{id(obj[0][1])}")
    print()


show_state("Начальное состояние")

original.append(["Databases", 5])
show_state("После original.append(['Databases', 5])")

original[0][1] = 3
show_state("После original[0][1] = 3")

print("=== Ошибочная и корректная матрицы ===")
wrong_matrix = [[0] * 3] * 3
print("До изменения:      ", wrong_matrix)
print("id строк wrong:    ", [id(row) for row in wrong_matrix])
wrong_matrix[0][0] = 1
print("После [0][0] = 1:  ", wrong_matrix)

correct_matrix = [[0] * 3 for _ in range(3)]
print("До изменения:      ", correct_matrix)
print("id строк correct:  ", [id(row) for row in correct_matrix])
correct_matrix[0][0] = 1
print("После [0][0] = 1:  ", correct_matrix)
