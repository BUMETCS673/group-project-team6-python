class Survey:

    def __init__(self,survey_name, **kwargs):

        # self.__survey_id = uuid
        self.__survey_name = survey_name
        self.__questions = []
        self.__students = []
        self.send_survey = False
        self.__active = False

    @property
    def questions(self):
        return self.__questions

    @questions.setter
    def questions(self,question_id):
        self.__questions.append(question_id)

    @questions.deleter
    def questions(self):
        print("delete all questions")
        del self.__questions

    def add_question(self,question):
        print("add question")
        self.__questions.append(question)

    def add_student(self,student):
        self.__students.append(student)