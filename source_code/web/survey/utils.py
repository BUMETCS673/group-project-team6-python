from survey.models import Option, Question
import csv


def reorder(question):
    existing_options = Option.objects.filter(question=question)
    if not existing_options.exists():
        return
    number_of_option = existing_options.count()
    new_ordering = range(0, number_of_option)

    for order, option in zip(new_ordering, existing_options):
        option.order = order
        option.save()


def save_question_set(IO_string, survey):
    """read and save csv to a survey"""
    """
    note: question type: 1 is mul,0 is single
    first row is the header
    return [# of success, total question input]
    """

    reader = csv.DictReader(IO_string)
    total_question = reader.line_num
    count_question_save = 0
    for question_idx, question in enumerate(reader):
        try:
            question_index = int(question['question_index'])
            question_type = "SINGLE" if str(question['question_type']) == '0' else "MULTIPLE" if str(question[
                                                                                                         'question_type']) == '1' else None
            max_choice = int(question['max_choice'])
            weight = int(question['weight'])
            name = str(question['name'])
            description = str(question['description'])
            options = question['options'].splitlines()
            question_obj = save_question(question_index=question_index,
                                         question_type=question_type,
                                         max_choice=max_choice,
                                         weight=weight,
                                         question_name=name,
                                         description=description,
                                         survey=survey)
            for choice_index, option_name in enumerate(options):
                save_option(choice_index=choice_index, choice_name=option_name, question=question_obj)
            count_question_save += 1
        except Exception as e:
            print(f"error{question}+++++++++++", e)
        print([count_question_save, total_question])
    return [count_question_save, total_question]


def save_question(question_index, question_type, max_choice, weight, question_name, description, survey):
    """save a question to the survey"""
    question, _ = Question.objects.get_or_create(survey=survey,
                                                 question_index=question_index,
                                                 question_type=question_type,
                                                 max_choice=max_choice,
                                                 weight=weight,
                                                 question_name=question_name,
                                                 description=description)
    return question


def save_option(choice_index, choice_name, question):
    """save an option of a question"""
    option, _ = Option.objects.get_or_create(choice_index=choice_index,
                                             choice_name=choice_name,
                                             question=question)
    return option
