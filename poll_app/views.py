from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Questions, Choice

# Create your views here.
def index(request):
    latest_question = Questions.objects.order_by('-pub_date')[:5]
    context = {'latest_question': latest_question}
    return render(request, 'poll_app/index.html', context)


def detail(request, question_id):
    try:
        question = Questions.objects.get(pk= question_id)
    except Questions.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'poll_app/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Questions,pk = question_id)
    return render(request, 'poll_app/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Questions, pk = question_id)
    try:
        selected = question.choice_set.get(pk = request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'poll_app/detail.html',{
            'question': question,
            'error_message': "select choice",
        })
    else:
        selected.votes += 1
        selected.save()
        return HttpResponseRedirect(reverse('poll_app:results', args = (question.id,)))
