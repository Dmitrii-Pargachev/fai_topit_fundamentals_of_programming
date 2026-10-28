"""
Информационная карточка вычислительного эксперимента.
Запрашивает параметры, вычисляет длительность и комплексный коэффициент.
"""

name = input("Имя исследователя: ")
exp_name = input("Название эксперимента: ")
runs = int(input("Количество выполненных запусков: "))
duration = float(input("Длительность одного запуска (с): "))
real_part = float(input("Действительная часть коэффициента: "))
imag_part = float(input("Мнимая часть коэффициента: "))

total_sec = runs * duration
total_min = total_sec / 60
coeff = complex(real_part, imag_part)
modulus_sq = real_part ** 2 + imag_part ** 2
has_runs = bool(runs)

print()
print("========================================")
print(f"ЭКСПЕРИМЕНТ: {exp_name}")
print(f"Исследователь: {name}")
print(f"Запуски: {runs}")
print(f"Общее время: {total_sec:.2f} с ({total_min:.2f} мин)")
print(f"Коэффициент: {coeff}")
print(f"Квадрат модуля: {modulus_sq:.2f}")
print(f"Есть выполненные запуски: {has_runs}")
print("========================================")

# Диагностическая строка с типами
print(f"\nТипы: name:{type(name)}, exp_name:{type(exp_name)}, runs:{type(runs)}, duration:{type(duration)}, real_part:{type(real_part)}, imag_part:{type(imag_part)}")