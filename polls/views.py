from .models import Question

from django.http import HttpResponse
from django.template import loader


def index(req):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list}

    return HttpResponse(template.render(context, req))


def detail(req, question_id):
    return HttpResponse(f'You\'re looking at question {question_id}')


def results(req, question_id):
    return HttpResponse(f'You\'re looking at the results of question {question_id}')


def vote(req, question_id):
    return HttpResponse(f'You\'re voting on question {question_id} ')

