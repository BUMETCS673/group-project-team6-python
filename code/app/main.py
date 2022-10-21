from question import SingleChoiceQuestion, MultipleChoiceQuestion
from survey import Survey
from user import Student
from answer_sheet import AnswerSheet
from team import Team
from instance import Instance

"""
illustrate the steps for creating survey and answer the survey from students
"""

# step 1: you need a survey, so create one
survey_1 = Survey(survey_name="hello", survey_id="unique_id", questions=None, students=None)

# step 2: you need to set questions for the survey
"""
for example: if you have 3 questions: 
1. single choice(choose 1)
    options: 1. Java, 2. C, 3. Python

2. mul choice(choose 2 of them)
    options: 1. Java, 2. C, 3. Python

3. mul choice(choose 3 of them)
    options: 1. Java, 2. C, 3. Python, 4. C++
"""
#question_1 = SingleChoiceQuestion(question_name="q1",
#                                  description="None",
#                                  weight=0,
#                                  choices=["Java", "C", "Python", "R"])
#
#question_2 = SingleChoiceQuestion(question_name="q2",
#                                  description="None",
#                                  weight=0,
#                                  choices=["Java", "C", "Python", "C++"])

question_3 = MultipleChoiceQuestion(question_name="q3",
                                    description="None",
                                    weight=-3,
                                    choices=["Java", "C", "Python", "C++", "R", "Ruby"],
                                    max_num_choice=3)

# step 3: add question to the survey
#survey_1.append_question(question_1)
#survey_1.append_question(question_2)
survey_1.append_question(question_3)
print(len(survey_1.questions))

# step 4: need to have student to answer the survey, so manually set 4 student here
# note: student id should be unique
student_1 = Student(name="stu 1", email="test@gmail.com", user_id=1)
student_2 = Student(name="stu 2", email="test@gmail.com", user_id=2)
student_3 = Student(name="stu 3", email="test@gmail.com", user_id=3)
student_4 = Student(name="stu 4", email="test@gmail.com", user_id=4)
student_5 = Student(name="stu 5", email="test@gmail.com", user_id=5)
student_6 = Student(name="stu 6", email="test@gmail.com", user_id=6)
student_7 = Student(name="stu 7", email="test@gmail.com", user_id=7)
student_8 = Student(name="stu 8", email="test@gmail.com", user_id=8)
student_9 = Student(name="stu 9", email="test@gmail.com", user_id=9)
# step 5: student respond to the survey

# dictionary
# (key = question in that survey, value = index of the option of the question)

student_1_answer = {
    #0: 3,  # single choice
    #1: 2,  # multiple choice
    0: {0: 1}  # multiple choice
}
student_2_answer = {
    #0: 3,  # single choice
    #1: 2,  # multiple choice
    0: {0: 1}  # multiple choice
}
student_3_answer = {
    #0: 3,  # single choice
    #1: 2,  # multiple choice
    0: {0: 1}  # multiple choice
}
student_4_answer = {
    #0: 3,  # single choice
    #1: 2,  # multiple choice
    0: {0: 1, 1: 2}  # multiple choice
}
student_5_answer = {
    #0: 3,  # single choice
    #1: 2,  # multiple choice
    0: {0: 2, 1: 1}  # multiple choice
}
student_6_answer = {
    #0: 3,  # single choice
    #1: 2,  # multiple choice
    0: {0: 2}  # multiple choice
}

student_7_answer = {
    #0: 3,  # single choice
    #1: 2,  # multiple choice
    0: {0: 2}  # multiple choice
}

student_8_answer = {
    #0: 3,  # single choice
    #1: 2,  # multiple choice
    0: {0: 2}  # multiple choice
}

student_9_answer = {
    #0: 3,  # single choice
    #1: 2,  # multiple choice
    0: {0: 1}  # multiple choice
}

# step 6. student submit their response
student_1.answer_survey(survey_1, student_1_answer)
student_2.answer_survey(survey_1, student_2_answer)
student_3.answer_survey(survey_1, student_3_answer)
student_4.answer_survey(survey_1, student_4_answer)
student_5.answer_survey(survey_1, student_5_answer)
student_6.answer_survey(survey_1, student_6_answer)
student_7.answer_survey(survey_1, student_7_answer)
student_8.answer_survey(survey_1, student_8_answer)
student_9.answer_survey(survey_1, student_9_answer)

# step 7. randomly assigned 4 student to the 2 teams, but here for the sake of illustration, I manually assign them
team_1 = Team(team_name="t1", survey_target=survey_1)
team_2 = Team(team_name="t2", survey_target=survey_1)
team_1.team_members = [student_1, student_2, student_3]
team_2.team_members = [student_1, student_2, student_3]

# step 8. calculate the two team scores?

## please write score function for the team class
#print(f"team_1 scores for single choice are {team_1.get_single_choice_scores()}")
#print(f"team_1 scores for multiple choices are {team_1.get_mul_choices_scores()}")

#####run optimization####
students_target = [student_1, student_2, student_3, student_4, student_5, student_6, student_7, student_8, student_9]
test_instance = Instance(60, students_target=students_target, num_team=2, survey_target=survey_1)

result = test_instance.run_instance()
print(result[0].get_all_team_member_id())
print(result[1].get_all_team_member_id())
print()

#result[0].get_mul_choices_scores()
#{0: -1.1058}
#result[1].get_mul_choices_scores()
#{0: -0.7098}
#
#
#
#
#
#
#
#
#

