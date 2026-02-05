n = int(input("Введіть кількість елементів масиву: "))

arr = []

for i in range(n):
    value = int(input(f"Введіть елемент {i + 1}: "))
    arr.append(value)

# Бульбашкове сортування
for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Відсортований масив:")
print(arr)

