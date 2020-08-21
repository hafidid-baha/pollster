from django.shortcuts import render
from .models import Question,Choice


def index(request):
    questions = Question.objects.all()
    context = {'questions':questions}
    return render(request,'polls/index.html',context)

def details(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question Does Not Exists")
    render(request,'polls/details.html',{'question':question})



