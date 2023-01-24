class Student:
    def __init__(self, student:dict):
        """[summary]

        Args:
            student (dict): {'name': 'name_of_student', 'grades': Tuple whit grades}
        """
        self.name = student['name']
        self.grades = student['grades']
    
    def average(self) -> float:
        return sum(self.grades)/len(self.grades)

data = {'name': 'Abelardo', 'grades': (90,91,92)}
student1 = Student(data)
print(f'student1.name: {student1.name}')
print(f'student1.grades: {student1.grades}')
print(f'student1.average(): {student1.average()}')
