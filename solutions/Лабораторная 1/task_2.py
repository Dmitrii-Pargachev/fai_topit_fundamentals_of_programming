a = 1000
b = a
c = int("1000")

# Прогноз сравнений:
# a == b: True (значения равны)
# a is b: True (это один и тот же объект в памяти, так как b = a)
# a == c: True (значения равны: 1000 и 1000)
# a is c: False (это разные объекты, так как c создан заново через int())

print("Типы:", type(a), type(b), type(c))
print("Идентификаторы:", id(a), id(b), id(c))
print("a == b:", a == b)
print("a is b:", a is b)
print("a == c:", a == c)
print("a is c:", a is c)

# Часть с None
c = None
print("c is None:", c is None)

# Проверка интернирования строк
first = "python"
second = "py" + "thon"
print(first == second) # True
print(first is second) # True, из-за оптимизации интерпретатор склеил "py"+"thon" заранее и указал на тот же объект