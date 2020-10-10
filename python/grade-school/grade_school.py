class School:
    def __init__(self):
        self.student = {}

    def add_student(self, name, grade):
        if grade not in self.student.keys():
            self.student[grade] = [name]
        else:
            self.student[grade].append(name)
    
    def roster(self):
        result = []
        for grades in sorted(self.student.keys()):
            for names in sorted(self.student[grades]):
                result.append(names)
        return result

    def grade(self, grade_number):
        if grade_number in self.student.keys():
            return sorted(self.student[grade_number])
        else:
            return []

