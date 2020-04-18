from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.http.request import HttpRequest
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse

from .models import Question, Choice


def index(request):
    return HttpResponse(r"Hello World! Python and AWS are awesome!")


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


def more_detail(request, question_id, extra_word):
    return HttpResponse(str("question_id = " + str(question_id) + "<br/>extra_word = " + str(extra_word)))


def question_list(request):
    question_list = Question.objects.all()
    template = loader.get_template('polls/question_list.html')
    context = {
        'question_list': question_list
    }
    return HttpResponse(template.render(context, request))


def question_list_shortcut(request):
    question_list = Question.objects.all()
    return render(request, 'polls/question_list.html', {
        'question_list': question_list
    })
    

def deliberate_404(request):
    raise Http404("Deliberate 404")
    return

    
def raise_404_if_question_does_not_exist(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return HttpResponse('Question exists --> ' + question.question_text)


def link_library(request):
    return render(request, 'polls/link_library.html')


def minimal_form(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/minimal_form.html', {
        'question': question
    })
    
    
def v2(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/minimal_form.html', {
            'question': question,
            'error_message': 'Select a valid choice'
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:show_all_choices'))
    

def show_all_choices(request):
    choices = Choice.objects.all()
    return render(request, 'polls/show_all_choices.html', {
        'choices': choices
    })
    
