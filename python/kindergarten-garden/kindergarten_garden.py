STUDENTS = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']
class Garden:
    def __init__(self, diagram, students=STUDENTS):
        self.students = students
        self.diagram = diagram.split() 
        self.students.sort()

    def plants(self, student):
        Plant = {"R" : "Radishes", "C" : "Clover", "G" : "Grass", "V" : "Violets"}
        result = []
        indice = self.students.index(student)
        for i in range(2):
            result.append(Plant[self.diagram[i][indice*2]])
            result.append(Plant[self.diagram[i][indice*2+1]])
        return result