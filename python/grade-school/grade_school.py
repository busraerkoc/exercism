class School:
    def __init__(self):
        self.student = []

    def add_student(self, name, grade): #dictionary data type
        self.student.append({'name':name, 'grade':grade})

    def roster(self):
        return [for name in students.values()]

    def grade(self, grade_number):
        pass
