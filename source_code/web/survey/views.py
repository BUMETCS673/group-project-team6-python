import io
from django.shortcuts import render, redirect, Http404, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from .forms import SurveyCreationForm, QuestionCreationForm, \
    OptionCreationForm, QuestionCreationFormSet, \
    OptionCreationFormSet, \
    StudentCreationFrom, SurveyForm
from django.forms.models import modelformset_factory
from iGroup.models import Instance
from account.models import Student
from .models import Survey, Question, AnswerSheet, Option
from django.views.decorators.http import require_http_methods
from .utils import reorder, save_question_set, save_all_student_answer_set
from django.contrib import messages


@login_required(login_url="/login")
def create_update_survey(request, instance_slug=None):
    """create a new survey"""
    current_instructor = request.user
    instance_obj = get_object_or_404(Instance, instructor=current_instructor,
                                     slug=instance_slug)  # report error, need to
    survey, created = Survey.objects.get_or_create(instance=instance_obj)

    if request.method == 'POST':
        survey_form = SurveyCreationForm(request.POST or None, instance=survey)
        questions = survey.get_questions_set()
        question_formset = QuestionCreationFormSet(request.POST or None, queryset=questions)
        if all([survey_form.is_valid(), question_formset.is_valid()]):
            survey = survey_form.save(commit=False)
            survey.save()
            question_index = 0
            for question_form in question_formset:
                question = question_form.save(commit=False)
                question.survey = survey
                question.question_index = question_index
                question.save()
                question_index += 1
        context = {
            'survey_form': survey_form,
            'question_formset': question_formset,
        }
        return render(request, "survey/survey_create.html", context)
    else:
        survey_form = SurveyCreationForm(instance=survey)
        questions = survey.get_questions_set()
        question_formset = QuestionCreationFormSet(queryset=questions)

    context = {
        'survey_form': survey_form,
        'question_formset': question_formset,
    }
    return render(request, "survey/survey_create.html", context)


@login_required(login_url="/login")
def create_update_options(request, question_id=None):
    """create or update option of a given question"""
    current_instructor = request.user
    question_obj = get_object_or_404(Question, question_id=question_id)
    instance_obj = question_obj.survey.instance
    if question_obj.survey.instance.instructor != current_instructor:
        raise Http404  # not allowed to modify

    options = question_obj.get_options_set()

    if request.method == 'POST':
        option_formset = OptionCreationFormSet(request.POST, queryset=options)
        option_index = 0
        if option_formset.is_valid():
            for option_form in option_formset:
                option = option_form.save(commit=False)
                option.question = question_obj
                option.choice_index = option_index
                option.save()
                option_index += 1
        return redirect('survey:survey_create_update', instance_slug=instance_obj.slug)
    else:
        option_formset = OptionCreationFormSet(queryset=options)

    context = {
        'option_formset': option_formset,
        'current_question': question_obj,

    }

    print("okkkk")
    return render(request, "survey/option_create.html", context)


# delete options
@login_required(login_url="/login")
def delete_options(request, question_id=None):
    current_instructor = request.user
    question_obj = get_object_or_404(Question, question_id=question_id)
    instance_obj = question_obj.survey.instance
    if question_obj.survey.instance.instructor != current_instructor:
        raise Http404  # not allowed to modify

    options = question_obj.get_options_set()

    options.delete()
    return redirect('survey:survey_create_update', instance_slug=instance_obj.slug)


# not required login
def survey_answer(request, survey_id):
    """student answer the survey"""
    survey = get_object_or_404(Survey, survey_id=survey_id)

    if request.method == "POST":
        student_form = StudentCreationFrom(request.POST)
        if student_form.is_valid():
            student = student_form.save()
        else:
            raise Http404
        survey_answer_form = SurveyForm(request.POST, survey=survey, student=student)
        if survey_answer_form.is_valid():
            survey_answer_form.save()

    else:
        student_form = StudentCreationFrom()
        survey_answer_form = SurveyForm(None, survey=survey, student=None)


    context = {
        'student_form': student_form,
        'survey_answer_form': survey_answer_form,
        'survey': survey
    }
    return render(request, 'survey/answer/survey_answer.html', context)


#####V2

@login_required(login_url="/login")
def create_survey(request, instance_slug=None):
    """create a new survey"""
    current_instructor = request.user
    instance_obj = get_object_or_404(Instance, instructor=current_instructor,
                                     slug=instance_slug)  # report error, need to
    if Survey.objects.filter(instance=instance_obj, instance__instructor=current_instructor).exists():
        raise Http404
    survey_form = SurveyCreationForm(request.POST or None)
    if survey_form.is_valid():
        survey_obj = survey_form.save(commit=False)
        survey_obj.instance = instance_obj
        survey_obj.save()
        # redirect to question page
        return redirect('survey:survey_index', survey_id=survey_obj.survey_id)
    context = {
        'survey_form': survey_form
    }
    return render(request, 'survey/create_survey.html', context)



@require_http_methods(['POST'])
@login_required(login_url="/login")
def upload_questions_csv(request, survey_id=None):
    """upload question set from csv file"""
    current_instructor = request.user
    survey_obj = get_object_or_404(Survey, survey_id=survey_id, instance__instructor=current_instructor)
    context = {}
    if request.method == "GET":
        render(request, 'survey/upload/upload_questions_csv.html', context)

    csv_file = request.FILES['csv_file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    question_set = csv_file.read().decode('utf-8-sig')
    io_string = io.StringIO(question_set)
    total_saved, total_upload = save_question_set(io_string, survey_obj)

    context = {  # not used yet
        "total_saved": total_saved,
        "total_upload": total_upload,
        'survey_obj': survey_obj
    }
    return redirect('survey:survey_index', survey_id=survey_id)


@login_required(login_url="/login")
def edit_survey():
    pass


@login_required(login_url="/login")
def delete_survey():
    pass


@login_required(login_url="/login")
def survey_index(request, survey_id=None):
    """show page of survey"""
    current_instructor = request.user
    survey_obj = get_object_or_404(Survey,
                                   survey_id=survey_id,
                                   instance__instructor=current_instructor)
    context = {
        'survey_obj': survey_obj
    }
    return render(request, 'survey/survey_index.html', context)


@login_required(login_url="/login")
def question_list(request, survey_id=None):
    current_instructor = request.user
    survey_obj = get_object_or_404(Survey,
                                   survey_id=survey_id,
                                   instance__instructor=current_instructor)
    question_set = survey_obj.get_questions_set()
    context = {
        'question_set': question_set
    }

    return render(request, 'survey/partials/question_list.html', context)


@login_required(login_url="/login")
def add_question(request, survey_id=None):
    """add question to the survey"""
    current_instructor = request.user
    survey_obj = get_object_or_404(Survey, survey_id=survey_id, instance__instructor=current_instructor)
    question_set = survey_obj.get_questions_set()
    num_questions = len(question_set)
    if request.method == "POST":
        # create question
        question_form = QuestionCreationForm(request.POST)
        if question_form.is_valid():
            question_obj = question_form.save(commit=False)
            question_obj.survey = survey_obj
            question_obj.question_index = num_questions + 1
            question_obj.save()
            return redirect('survey:survey_index', survey_id=survey_obj.survey_id)
    else:
        # GET
        question_form = QuestionCreationForm()
    context = {
        'question_form': question_form
    }
    return render(request, 'survey/question_form.html', context)


@login_required(login_url="/login")
def edit_question(request, survey_id=None, question_id=None):
    """edit question in the survey"""
    current_instructor = request.user
    survey_obj = get_object_or_404(Survey, survey_id=survey_id, instance__instructor=current_instructor)
    question_obj = get_object_or_404(Question, survey=survey_obj, question_id=question_id)
    if request.method == "POST":
        # create question
        question_form = QuestionCreationForm(request.POST, instance=question_obj)
        if question_form.is_valid():
            question_form.save()
            context = {
                'survey_obj': survey_obj,

            }
            return render(request, 'survey/survey_index.html', context)
    else:
        # GET
        question_form = QuestionCreationForm(instance=question_obj)
    context = {
        'question_form': question_form,
        'question_obj': question_obj
    }
    return render(request, 'survey/question_form.html', context)


@login_required(login_url="/login")
def remove_question():
    pass


@login_required(login_url="/login")
def add_option(request, survey_id=None, question_id=None):
    """add option for this question"""
    current_instructor = request.user
    survey_obj = get_object_or_404(Survey, survey_id=survey_id, instance__instructor=current_instructor)
    question_obj = get_object_or_404(Question, survey=survey_obj, question_id=question_id)
    option_set = question_obj.get_options_set()
    num_option = len(option_set)
    if request.method == "POST":
        # create question
        option_form = OptionCreationForm(request.POST, question=question_obj)
        if option_form.is_valid():
            option_obj = option_form.save(commit=False)
            option_obj.question = question_obj
            option_obj.choice_index = num_option
            option_obj.save()
            print("done", option_obj.choice_index)
            return redirect('survey:option_list',
                            survey_id=survey_obj.survey_id,
                            question_id=question_obj.question_id)
        print("not done")
    else:
        # GET
        option_form = OptionCreationForm(question=question_obj)
    context = {
        'option_form': option_form
    }
    return render(request, 'survey/option_form.html', context)


@login_required(login_url="/login")
def option_list(request, survey_id=None, question_id=None):
    current_instructor = request.user
    survey_obj = get_object_or_404(Survey,
                                   survey_id=survey_id,
                                   instance__instructor=current_instructor)
    question_obj = get_object_or_404(Question, survey=survey_obj, question_id=question_id)
    option_set = question_obj.get_options_set()
    context = {
        'option_set': option_set,
        'question_obj': question_obj,
        'survey_obj': survey_obj
    }

    return render(request, 'survey/partials/option_list.html', context)


@login_required(login_url="/login")
def option_sort(request, question_id=None):
    option_order = request.POST.getlist('option_order')
    print(option_order)
    current_instructor = request.user
    question_obj = get_object_or_404(Question,
                                     question_id=question_id,
                                     survey__instance__instructor=current_instructor)
    option_set = []
    for idx, option_pk in enumerate(option_order):
        option_obj = Option.objects.get(pk=option_pk,
                                        question=question_obj)
        print(option_obj)
        option_obj.choice_index = idx
        option_obj.save()
        option_set.append(option_obj)
    print(option_set)
    context = {
        'option_set': option_set,
        'question_obj': question_obj
    }
    return render(request, 'survey/partials/option_list.html', context)


@require_http_methods(['DELETE'])
@login_required(login_url="/login")
def delete_option(request, pk=None, question_id=None):
    current_instructor = request.user
    option_obj = Option.objects.get(pk=pk)
    question_obj = get_object_or_404(Question, question_id=question_id)
    if question_obj.survey.instance.instructor != current_instructor:
        raise Http404
    option_obj.delete()

    reorder(question_obj)

    options = question_obj.get_options_set()
    context = {
        'option_set': options
    }
    return render(request, 'survey/partials/option_list.html', context)


@login_required(login_url="/login")
def upload_answers_csv(request, survey_id=None):
    current_instructor = request.user
    survey_obj = get_object_or_404(Survey, survey_id=survey_id, instance__instructor=current_instructor)
    instance_slug = survey_obj.instance.slug
    context = {
        'survey_obj': survey_obj
    }
    if request.method == "GET":
        render(request, 'survey/upload/upload_questions_csv.html', context)

    csv_file = request.FILES['csv_file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')

    question_set = csv_file.read().decode('utf-8-sig')
    io_string = io.StringIO(question_set)
    save_all_student_answer_set(io_string, survey_obj)

    context = {  # not used yet
        'survey_obj': survey_obj
    }
    return redirect('iGroup:detail', slug=instance_slug)


@require_http_methods(['GET'])
@login_required(login_url="/login")
def student_list(request, survey_id=None):
    """list all student answer this survey"""
    current_instructor = request.user
    survey_obj = get_object_or_404(Survey, survey_id=survey_id, instance__instructor=current_instructor)
    all_responses = survey_obj.answersheet_set  # all answer sheets of this survey
    # only active response, which are all the students
    all_students = [
        ((AnswerSheet.objects.filter(survey=survey_obj, student=answer_sheet.student).count()),
         answer_sheet.student) for answer_sheet in
        all_responses.filter(active=True)]  # [(num of answer sheet, student obj)]

    num_students = len(all_students)
    num_responses = all_responses.count()

    context = {
        'num_students': num_students,
        'num_responses': num_responses,
        'all_responses': all_responses,
        'all_students': all_students,
        'survey_obj': survey_obj,

    }

    return render(request, 'survey/answer/student_list.html', context)


@require_http_methods(['GET'])
@login_required(login_url="/login")
def answer_sheet_list(request, survey_id, student_id):
    """list all answer sheet of a student that response to this survey"""
    current_instructor = request.user
    survey_obj = get_object_or_404(Survey, survey_id=survey_id, instance__instructor=current_instructor)
    student_obj = get_object_or_404(Student, pk=student_id)
    answer_sheet_set = AnswerSheet.objects.filter(survey=survey_obj, student=student_obj)
    num_answer_sheet = answer_sheet_set.count()
    context = {
        'answer_sheet_set': answer_sheet_set,
        'student_obj': student_obj,
        'survey_obj': survey_obj,
        'num_answer_sheet': num_answer_sheet
    }

    return render(request, 'survey/answer/answer_sheet_list.html', context)


@require_http_methods(['GET'])
@login_required(login_url="/login")
def answer_sheet_detail(request, survey_id, answer_sheet_id):
    """detail answer sheet view"""
    current_instructor = request.user
    survey_obj = get_object_or_404(Survey, survey_id=survey_id, instance__instructor=current_instructor)
    answer_sheet_obj = AnswerSheet(answer_sheet_id=answer_sheet_id, survey=survey_obj)
    question_answer_set = answer_sheet_obj.get_answers()  # list of (question,query set)
    context = {
        'question_answer_set': question_answer_set
    }
    return render(request, 'survey/answer/answer_sheet_detail.html', context)
