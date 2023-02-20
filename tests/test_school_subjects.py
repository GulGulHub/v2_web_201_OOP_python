from views.school_subjects import SchoolSubjects
from models.subject import SchoolSubject



class TestSchoolSubjects:

    def test_get_syllabus_all(self):
        subject_maths = SchoolSubject("Maths")
        subject_maths.put_syllabus("Intro", 5)
        print(subject_maths.syllabus)
        school_subjects = SchoolSubjects("Maths")
        assert school_subjects.get_syllabus_all(subject_maths.syllabus) == "5, Intro"
