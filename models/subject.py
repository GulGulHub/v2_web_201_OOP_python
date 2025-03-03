class SchoolSubject:

    # paramterized constructor: to initialize class parameters.
    # name and syllabus is an empty dictionary.
    def __init__(self, name):
        self.name = name
        self.syllabus = {} # dictionary of type: Dict[Number:String] | chapter_number:chapter_name

    # func to get the name of the subject.
    def get_name(self):
        return self.name

    # func to enter the syllabus details with chapters' number and name.
    def put_syllabus(self, chapter_name, chapter_number):
        self.syllabus[chapter_number] = chapter_name


