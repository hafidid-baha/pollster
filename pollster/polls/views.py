from django.shortcuts import render,get_object_or_404
from .models import Question,Choice
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def index(request):
    questions = Question.objects.all()
    context = {'questions':questions}
    return render(request,'polls/index.html',context)

def details(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exists")
    return render(request,'polls/details.html',{'question':question})

def results(request,question_id):
    question = Question.objects.get(pk=question_id)
    return render(request,'polls/results.html',{'question':question})

def vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request,'polls/details.html',{ 'question':question })
    else:
        # return HttpResponse(request.POST['choice'])
        choice.votes += 1
        choice.save()
        return HttpResponseRedirect(reverse('polls:result',args=(question.id,)))



