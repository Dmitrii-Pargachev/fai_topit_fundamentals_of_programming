import math

# Эксперимент A. int и арифметические операторы
print("=== Эксперимент A: int и арифметические операторы ===")
x = 17
y = 5

add = x + y
sub = x - y
mul = x * y
div = x / y
floordiv = x // y
mod = x % y
power = x ** y

print("x + y  =", add, type(add))
print("x - y  =", sub, type(sub))
print("x * y  =", mul, type(mul))
print("x / y  =", div, type(div))
print("x // y =", floordiv, type(floordiv))
print("x % y  =", mod, type(mod))
print("x ** y =", power, type(power))

# Эксперимент B. Большие целые числа
print("\n=== Эксперимент B: большие целые числа ===")
big = 2 ** 1000
print("2 ** 1000 =", big)
print("Тип:", type(big))

# Эксперимент C. float
print("\n=== Эксперимент C: float ===")
result = 0.1 + 0.2
equal_direct = result == 0.3
difference = result - 0.3
equal_close = math.isclose(result, 0.3)

print("result =", result)
print("result == 0.3:", equal_direct)
print("result - 0.3 =", difference)
print("math.isclose(result, 0.3):", equal_close)

# Эксперимент D. bool, complex и явные преобразования
print("\n=== Эксперимент D: bool, complex и преобразования ===")
v_int = int("42")
v_float = float("3.14")
v_str = str(2026)
v_bool_zero = bool(0)
v_bool_neg = bool(-1)
v_bool_empty = bool("")
v_bool_false_str = bool(False)
v_complex = complex(2, -3)

print('int("42")     =', repr(v_int), type(v_int))
print('float("3.14") =', repr(v_float), type(v_float))
print("str(2026)     =", repr(v_str), type(v_str))
print("bool(0)       =", v_bool_zero, type(v_bool_zero))
print("bool(-1)      =", v_bool_neg, type(v_bool_neg))
print('bool("")      =', v_bool_empty, type(v_bool_empty))
print('bool("False") =', v_bool_false_str, type(v_bool_false_str))
print("complex(2, -3) =", v_complex, type(v_complex))
print("Действительная часть:", v_complex.real)
print("Мнимая часть:", v_complex.imag)
