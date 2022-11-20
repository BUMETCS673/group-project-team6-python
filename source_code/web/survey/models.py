from django.db import models
from django.db.models import CASCADE
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.urls import reverse


# Create your models here.

# survey
class Survey(models.Model):
    """
    Survey model
    """
    survey_id = models.AutoField(primary_key=True)
    survey_name = models.CharField(max_length=20)
    num_question = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    send_survey = models.BooleanField(default=False)
    instance = models.OneToOneField('iGroup.Instance', on_delete=CASCADE)

    def get_absolute_url(self):
        return reverse('survey:detail', kwargs={"survey_id": self.survey_id})

    def get_questions_set(self):
        """get all question set to this survey"""
        return self.question_set.all()

    def get_questions_set_order_by_index(self):
        """get all question set order by index to this survey"""
        return self.question_set.all().order_by('question_index')

    def __str__(self):
        """str repr"""
        return self.survey_name


# question

class Question(models.Model):
    """
    Generic question model
    """

    class Meta:
        unique_together = ('survey', 'question_index')

    class QuestionType(models.TextChoices):
        """
        the question types
        """
        single_question = ("SINGLE", "Single choice")
        multiple_question = ("MULTIPLE", "Multiple choice")

    question_id = models.AutoField(primary_key=True)
    question_type = models.CharField(choices=QuestionType.choices, max_length=50)
    question_index = models.IntegerField()  # position in the survey
    question_name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    weight = models.IntegerField(default=0)
    max_choice = models.IntegerField(default=1)
    survey = models.ForeignKey('Survey', on_delete=CASCADE)

    def get_absolute_url(self):
        return self.survey.get_absolute_url()

    def get_options_set(self):
        """get all option to this question"""
        return self.option_set.all()

    def get_option_by_index(self, option_index):
        """get a option by its index"""
        return self.option_set.get(choice_index=option_index)

    def get_options_set_order_by_index(self):
        """get all options to this question and order by their index value"""
        return self.option_set.all().order_by('choice_index')

    def get_options_name_order_by_index(self):
        """get all options name by its index"""
        options_name = self.get_options_set_order_by_index().values('choice_name')
        return options_name

    def get_choice_set(self):
        """get all answers that relate to this question"""
        if self.question_type == "SINGLE":
            return self.choicesingle_set
        elif self.question_type == "MULTIPLE":
            return self.choicemultiple_set

    def __str__(self):
        """str repr"""
        return self.question_name


class Option(models.Model):
    """
    choice field
    """
    choice_index = models.IntegerField()  # the position of the choice
    choice_name = models.CharField(max_length=50)
    question = models.ForeignKey('Question', on_delete=CASCADE)

    def get_question_index(self):
        return self.question.question_index

    def __repr__(self):
        return self.choice_name

    def __str__(self):
        return self.choice_name

    class Meta:
        ordering = ('choice_index',)


# answer sheet
class AnswerSheet(models.Model):
    """
    Answer sheet
    """
    answer_sheet_id = models.AutoField(primary_key=True)
    survey = models.ForeignKey('Survey', on_delete=CASCADE)
    student = models.ForeignKey('account.Student', on_delete=CASCADE)  # should link to student
    active = models.BooleanField(default=True)  # if this answer sheet is the newest answer sheet

    def get_answers(self):
        """
        get all answer that record on this answer sheet
        return answers, which is list of (question,Query set)
        """
        question_set = self.survey.get_questions_set()
        answers = []
        for question in question_set:
            answer = (question, question.get_choice_set().filter(answer_sheet=self))
            answers.append(answer)
        return answers


class ChoiceMultiple(models.Model):
    choice_id = models.AutoField(primary_key=True)
    option = models.ForeignKey('Option', on_delete=CASCADE)
    question = models.ForeignKey('Question', on_delete=CASCADE)
    rank = models.IntegerField(null=False)
    answer_sheet = models.ForeignKey('AnswerSheet', on_delete=CASCADE)

    def get_student(self):
        return self.answer_sheet.student

    def get_question_index(self):
        return self.option.get_question_index()

    def get_choice_index(self):
        return self.option.choice_index


class ChoiceSingle(models.Model):
    choice_id = models.AutoField(primary_key=True)
    option = models.ForeignKey('Option', on_delete=CASCADE)
    question = models.ForeignKey('Question', on_delete=CASCADE)
    answer_sheet = models.ForeignKey('AnswerSheet', on_delete=CASCADE)

    def get_student(self):
        return self.answer_sheet.student

    def get_question_index(self):
        return self.option.get_question_index()

    def get_choice_index(self):
        return self.option.choice_index
