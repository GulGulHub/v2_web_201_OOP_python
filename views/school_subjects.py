from models.subject import SchoolSubject


class SchoolSubjects(SchoolSubject):

    def __init__(self, name):
        super().__init__(name=name)
    # func to get details of the syllabus.

    def get_syllabus_all(self, syllabus_dict):
        self.syllabus = syllabus_dict
        for item in self.syllabus:
            print(item, self.syllabus[item])
            return f"{item}, {self.syllabus[item]}"
        # for key, value in syllabus.items():
        # print(key, value)

    def get_syllabus_by_chapter(self, chapter:int):
        return self.syllabus[chapter]

