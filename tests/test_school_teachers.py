from views.school_teachers import SchoolTeachers
from models.teacher import SchoolTeacher


class TestSchoolTeachers:

    def test_enroll_teacher(self):
        teach1 = SchoolTeacher("Lee")
        school_teachers_ob = SchoolTeachers()
        school_teachers_ob.enroll_teacher(teach1)
        assert teach1 in school_teachers_ob.enrolled_teachers

    def test_all_teachers(self):
        teach2 = SchoolTeacher("Ali")
        school_teachers_ob = SchoolTeachers()
        school_teachers_ob.enroll_teacher(teach2)
        assert "Name : Ali" == school_teachers_ob.all_teachers()


    def test_fetch_all_teacher_data(self):
        teach1 = SchoolTeacher("Lee")
        teach2 = SchoolTeacher("Ali")
        school_teachers_ob = SchoolTeachers()
        school_teachers_ob.enroll_teacher(teach1)
        school_teachers_ob.enroll_teacher(teach2)
        all_teach = school_teachers_ob.fetch_all_teacher_data()
        assert teach1 and teach2 in all_teach

    def test_fetch_data_with_teacher_name(self):
        teach1 = SchoolTeacher("Lee")
        school_teachers_ob = SchoolTeachers()
        school_teachers_ob.enroll_teacher(teach1)
        teach_list = school_teachers_ob.fetch_data_with_teacher_name(teach1.name)
        assert teach1 in teach_list
        assert teach1.name == teach_list[0].name
