student = {"name": "Ali", "age": 17, "grade": "11"}

print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Grade: {student['grade']}")
student["name"]="Saad"
print(student)
student.popitem
print(student)

student= {
"S001":{"name":"Saad","age":20,"grade":3.20},
"S002":{"name":"Saad","age":20,"grade":3.20},
"S003":{"name":"Saad","age":20,"grade":3.20},
}
print (student["S001"].get("name4"))


schedule= {
"Sunday": ["Programming", "Networks","Cybersecurity"],
"Monday": ["HTML","Python","C#"],
"Tuseday":       ["HTML","Python","C#"],


}
print (schedule["Sunday"][1])