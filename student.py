class Student:

    def __init__(self,name,subscores):
        self.name = name
        self.subscores = subscores
    def average(self):
        return sum(self.subscores) / len(self.subscores)

stu_1 = Student("Aditya",[87,63,99])
print(f"{stu_1.average():2f}")