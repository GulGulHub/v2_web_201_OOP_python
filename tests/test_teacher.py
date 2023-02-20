from models.teacher import SchoolTeacher


class TestSchoolTeacher:

    def test_get_name(self):
        teach_obj = SchoolTeacher("Miller")
        assert teach_obj.name == "Miller"
