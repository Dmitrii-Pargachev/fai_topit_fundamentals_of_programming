student = "Анна Смирнова"
course = "Основы программирования на Python"
completed = 7
total = 10

# 1. Первый и последний символ
print(student[0], student[-1])

# 2. Срез с именем и фамилией
print(student[0:4])
print(student[5:])

# 3. Верхний и нижний регистр
print(student.upper())
print(student.lower())

# 4. Инициалы
print(f"{student[0]}.{student[5]}.")

# 5. Название курса в обратном порядке
print(course[::-1])

# 6. Три способа форматирования
percent = (completed / total) * 100
print("%s — %s: %d/%d (%.1f%%)" % (student, course, completed, total, percent))
print("{} — {}: {}/{} ({:.1f}%)".format(student, course, completed, total, percent))
print(f"{student} — {course}: {completed}/{total} ({percent:.1f}%)")

# 7. Исследование Unicode
symbol = "Я"
print("Символ:", symbol)
print("Позиция:", ord(symbol))
print("Восстановленный:", chr(ord(symbol)))
encoded = symbol.encode("utf-8")
print("Байты:", encoded, "Длина:", len(encoded))

# 8. Неизменяемость строки (вызовет TypeError)
#  student[0] = "X"