from views.school_subjects import SchoolSubjects
from models.subject import SchoolSubject



class TestSchoolSubjects:

    def test_get_syllabus_all(self):
        subject_maths = SchoolSubject("Maths")
        subject_maths.put_syllabus("Intro", 5)
        school_subjects = SchoolSubjects("Maths", subject_maths.syllabus)
        assert school_subjects.get_syllabus_all() == 5, "Intro"
