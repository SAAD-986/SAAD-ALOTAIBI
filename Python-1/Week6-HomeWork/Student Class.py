class Student:
    def __init__(self, name, age, grade):
    
        self.name = name
        self.age = age
        self.grade = grade

s1 = Student("Sara", 17, "11A")
s2 = Student("Ahmed", 18, "12B")
print(f"Student 1: {s1.name}, Age: {s1.age}, Grade: {s1.grade}")
print(f"Student 2: {s2.name}, Age: {s2.age}, Grade: {s2.grade}")