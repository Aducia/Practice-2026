# Список студентів та їхніх оцінок
students_grades = {
    "Кирило": [5, 4, 5, 4],
    "Артем": [4, 3, 4, 4],
    "Владислава": [5, 5, 5, 4]
}

# Словник для збереження середнього балу кожного студента
average_grades = {}

# Множина для збереження унікальних оцінок
unique_grades = set()

for name, grades in students_grades.items():
    # Додаємо оцінки до множини унікальних значень
    unique_grades.update(grades)

    # Обчислення середнього балу
    average = sum(grades) / len(grades)

    # Заповнення словника у форматі {ім’я: середній_бал}
    average_grades[name] = round(average, 2)

print("Середній бал студентів:")
for name, grades in average_grades.items():
    print(f"{name}: {grades}")

print("\nУнікальні оцінки:")
for grades in unique_grades:
    print(grades)