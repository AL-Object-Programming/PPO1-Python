from Student import Student
import random

if __name__ == '__main__':
    names = ['Andrew', 'William', 'James', 'Harper', 'Mason', 'Evelyn', 'Ella', 'Avery']
    last_names = ['Smith', 'Jones', 'Williams', 'Brown']
    students = []

    for index in range(10):
        students.append(Student(
            random.choice(names),
            random.choice(last_names),
            random.randint(39000, 39999),
            (random.getrandbits(1))))

for student in students:
    if student.status:
        print(student.last_name + ' ' + student.name + ' (' + str(student.index) + ')')
