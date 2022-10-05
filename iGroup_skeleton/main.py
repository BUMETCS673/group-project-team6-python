from survey import Survey
from student import Student
from team import Team
from run import Run
from question import SingleChoiceQuestion
from answer import SingleChoiceAnswer

#1 question
question_1 = SingleChoiceQuestion(question_name="tq1",
                                  description="this is a test",
                                  question_type= "single",
                                  weight=3,
                                  choices= ["python","java","C"]
                                  )
#2 survey
survey_1 = Survey(survey_name = "test")

#3 add question to survey
survey_1.add_question(question_1)

#3 student set up their account(any time before adding them to the survey)
student_1 = Student(student_name="test_stu")

#4 survey add student
survey_1.add_student(student_1)

#5 get answer from student
answer_1 = SingleChoiceAnswer(question=question_1,
                              student= student_1,
                              question_type=question_1.question_type,
                              survey=survey_1,
                              choice= 0)

#6 run the algorithm
#1 create the run
run_1 = Run()
#connect it to the survey
#snap shot the survey
run_1.set_survey()
#run
run_1.run_allocation()








print()