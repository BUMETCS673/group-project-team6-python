from question import SingleChoiceQuestion, MultipleChoiceQuestion
from survey import Survey
from user import Student
from answer_sheet import AnswerSheet
from team import Team

"""
illustrate the steps for creating survey and answer the survey from students
"""

# step 1: you need a survey, so create one
survey_1 = Survey(survey_name="hello", questions=None, students=None)

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
question_1 = SingleChoiceQuestion(question_name="q1",
                                  description="None",
                                  question_type="single choice",
                                  weight=1,
                                  choices=["Java", "C", "Python"])

question_2 = MultipleChoiceQuestion(question_name="q2",
                                    description="None",
                                    question_type="mul choice",
                                    weight=1,
                                    choices=["Java", "C", "Python"],
                                    max_num_choice=2)
question_3 = MultipleChoiceQuestion(question_name="q3",
                                    description="None",
                                    question_type="mul choice",
                                    weight=1,
                                    choices=["Java", "C", "Python", "C++"],
                                    max_num_choice=3)

# step 3: add question to the survey
survey_1.append_question(question_1)
survey_1.append_question(question_2)
survey_1.append_question(question_3)
print(len(survey_1.questions))

# step 4: need to have student to answer the survey, so manually set 4 student here
student_1 = Student(name="stu 1", email="test@gmail.com")
student_2 = Student(name="stu 2", email="test@gmail.com")
student_3 = Student(name="stu 3", email="test@gmail.com")
student_4 = Student(name="stu 4", email="test@gmail.com")

# step 5: student respond to the survey

# dictionary
# (key = question in that survey, value = index of the option of the question)
student_1_answer = {
    question_1: [1],
    question_2: [0, 2],
    question_3: [1, 3, 2]
}
student_2_answer = {
    question_1: [1],
    question_2: [0, 2],
    question_3: [1, 3, 2]
}
student_3_answer = {
    question_1: [0],
    question_2: [0, 1],
    question_3: [2, 3, 1]
}
student_4_answer = {
    question_1: [2],
    question_2: [1, 2],
    question_3: [1, 3, 2]
}

# step 6. student submit their response
student_1.answer_survey(survey_1, student_1_answer)
student_2.answer_survey(survey_1, student_2_answer)
student_3.answer_survey(survey_1, student_3_answer)
student_4.answer_survey(survey_1, student_4_answer)

# step 7. randomly assigned 4 student to the 2 teams, but here for the sake of illustration, I manually assign them
team_1 = Team(team_size=2, team_name="t1", survey_target=survey_1)
team_2 = Team(team_size=2, team_name="t2", survey_target=survey_1)
team_1.team_members = [student_1, student_2]

# step 8. calculate the two team scores?

## please write score function for the team class
print(f"team_1 scores for multiple choice are {team_1.get_single_choice_scores()}")

print()
