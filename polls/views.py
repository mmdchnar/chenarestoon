from os import walk, remove, path
from .models import Question, Choice, File
from .forms import UploadFileForm
 
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


def files(req):
    
    files = []
    files_and_dirs = walk('polls/static/files')
    for dir in files_and_dirs:
        for file in dir[2]:
            files.append(dir[0][18:] + file)
    files.sort(key=str.lower)

    if req.method == 'POST':
        form = UploadFileForm(req.POST, req.FILES)
        if form.is_valid():
            file = File(file=req.FILES['file'])
            file.save()
            for i in list(walk('polls/media'))[0][2]:
                if not path.exists('polls/static/files/' + i):
                    open('polls/static/files/' + i, 'wb').write(open('polls/media/' + i, 'rb').read())
                    remove('polls/media/' + i)
                else:
                    counter = 1
                    if '.' in i: 
                        temp = i.split('.')
                        temp_1 = i.replace('.' + temp[-1], '')

                        while path.exists('polls/static/files/' + temp_1 + '_' + str(counter) + '.' + temp[-1]):
                            counter += 1

                        open('polls/static/files/' + temp_1 + '_' + str(counter) + '.' + temp[-1],
                             'wb').write(open('polls/media/' + i, 'rb').read())
                    else:
                        while path.exists('polls/static/files/' + i + '_' + str(counter)):
                            counter += 1

                        open('polls/static/files/' + i + '_' + str(counter),
                             'wb').write(open('polls/media/' + i, 'rb').read())

                    remove('polls/media/' + i)

            return HttpResponseRedirect(reverse('files'))
    else:
        form = UploadFileForm()

    return render(req, 'polls/files.html', {'files': files})


def vote(req, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=req.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(req, 'polls/detail.html', {'question': question,
            'error_message': 'You didn\'nt select a choice.'})
    else:
        selected_choice.vote += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def page_not_found(req, ex):
    return render(req, 'polls/404.html')


def server_error(req):
    return render(req, 'polls/404.html')

