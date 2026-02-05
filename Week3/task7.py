trio = [
    {
        "surname": "Макада",
        "name": "Владислава",
        "grades": [98, 92, 94, 92, 90]
    },
    {
        "name": "Кирило",
        "surname": "Пінчук",
        "grades": [95, 92, 98, 90, 91]
    },
    {
        "surname": "Зіненко",
        "name": "Артем",
        "grades": [82, 94, 89, 93, 89]
    }
]

subjects_count = 5

print("Ім’я\tПрізвище\tСередній бал")

# Середній бал кожного студента
for student in trio:
    avg_student = sum(student["grades"]) / subjects_count
    print(f"{student['name']}\t{student['surname']}\t{avg_student:.2f}")

print("\nСередній бал трійці з дисциплін:")

# Обчислення середнього балу з кожної дисципліни
mat_an = (trio[0]["grades"][0] + trio[1]["grades"][0] + trio[2]["grades"][0]) / 3
disc_math = (trio[0]["grades"][1] + trio[1]["grades"][1] + trio[2]["grades"][1]) / 3
lin_alg = (trio[0]["grades"][2] + trio[1]["grades"][2] + trio[2]["grades"][2]) / 3
ipz = (trio[0]["grades"][3] + trio[1]["grades"][3] + trio[2]["grades"][3]) / 3
opam = (trio[0]["grades"][4] + trio[1]["grades"][4] + trio[2]["grades"][4]) / 3

print("Мат. аналіз:", f"{mat_an:.2f}")
print("Дискретна математика:", f"{disc_math:.2f}")
print("Лінійна алгебра:", f"{lin_alg:.2f}")
print("ІПЗ:", f"{ipz:.2f}")
print("ОПАМ:", f"{opam:.2f}")