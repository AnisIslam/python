class Student:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        # self.id = id

class Teacher:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        # self.id = id 

class School:
    def __init__(self, name, teachers, courses, students):
        self.name = name
        self.teachers = teachers
        self.courses = courses
        self.students = students
        # self.id = id 
    def get_students(self):
        for student in self.students:
            print(student.name)

school_name = "abc school"
softdev_course = Course("SD-1", "Abul Sir")
teacher_1 = Teacher('Abul Sir', softdev_course)
DB_course = Course("DB", "CR bhai")
teacher_2 = Teacher('CR bhai', DB_course)

student_1 = Student('1 no student', 19, 45)
student_2 = Student('2 no student', 33, 485)
student_3 = Student('3 no student', 44, 898)

teachers = [teacher_1, teacher_2]
students = [student_1, student_2, student_3]
courses = [softdev_course,DB_course]

my_school = School(school_name, teachers, courses, students)

print(my_school)
my_school.get_students()