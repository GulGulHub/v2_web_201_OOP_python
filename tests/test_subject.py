from models.subject import SchoolSubject


class TestSchoolSubject:

    def test_get_name(self):
        subject = SchoolSubject("Maths")
        assert subject.name == "Maths"

    def put_syllabus(self):
        subject_maths = SchoolSubject("Maths")
        subject_maths.put_syllabus("Intro",5)
        assert {5:"Intro"} in subject_maths.syllabus == True



