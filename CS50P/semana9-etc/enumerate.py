students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

print()

students = ["Hermione", "Harry", "Ron"]

# enumerate retorna tanto o valor quanto o indice da sequencia
for i, student in enumerate(students):
    print(i + 1, student)