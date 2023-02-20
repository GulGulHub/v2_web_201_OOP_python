from models.student import Student
from models.physics_teacher import PhysicsTeacher
from views.school_students import SchoolStudents
from models.subject import SchoolSubject
from views.school_teachers import SchoolTeachers
from models.teacher import SchoolTeacher
from views.school_subjects import SchoolSubjects

# # This file is just for our convenience for now to print and check methods and their behaviour.
#
# # Student is data type / Class is a data type - eg. strings, Int, floats
# student = Student(name="Jyotsna", age=29, class_number=3)
# # access class variables
# print(student.age) # 29
# print(student.class_number) # 3
# print(student.name) # Jyotsna
#
# SchoolStudents().enroll_student(student)
# SchoolStudents().all_students()
#
# # TODO: put into a view
# enroll_teachers()
#physics_teacher_1 = physics_teacher.PhysicsTeacher(name="Mia", lab_number="101")

# teacher_miller = PhysicsTeacher(name="Miller", lab_number="101")
#
# school_teacher = SchoolTeachers()
#
# school_teacher.enroll_teacher(teacher_miller)
#
# print(school_teacher.enrolled_teachers)
#
#
# #
# print("Teacher details:")
# print("name:"+physics_teacher_1.name, "lab number:" + physics_teacher_1.get_lab_number())
#
# # create a new object of type SchoolSubject and print its name
# school_subject = SchoolSubject(name="Physics")
# print(school_subject.name)
#
# student_Dora = Student(name="Dora", age=27, class_number=4)
# student_Dora.calculate_year_of_birth(2023)

#print(student_Dora.class_number)
#
# teach1 = SchoolTeacher("Lee")
# print(teach1.name)
# school_teachers_ob = SchoolTeachers()
# school_teachers_ob.enroll_teacher(teach1)
# print(school_teachers_ob.enrolled_teachers)
#
# teach_list = school_teachers_ob.fetch_data_with_teacher_name("Lee")
# print(teach_list[0].name)


syllabus = {3:"678", 4:"help", 5:"me"}

subject = SchoolSubject("Physics")
subject.put_syllabus("Intro",5)
print(subject.syllabus)


school_subjects = SchoolSubjects(subject)

school_subjects.get_syllabus_all(subject.syllabus)