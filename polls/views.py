from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from .models import Question


def index(request: HttpResponse):
    questions = Question.objects.order_by('-pub_date')[:5]
    context = {'questions': questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id: int):
    question = get_object_or_404(Question, id=question_id)
    context = {'question': question}
    return render(request, 'polls/detail.html', context)


def vote(request, question_id: int):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choices.get(id=request.POST['choice'])
    except (KeyError):
        return render(request, "polls/detail.html", {
            'error_message': "You didn't select a choice",
            'question': question
        })
    selected_choice.votes += 1
    selected_choice.save()
    return redirect('polls:results', question.id)


def results(request, question_id: int):
    question = get_object_or_404(Question, id=question_id)
    context = {'question': question}
    return render(request, 'polls/results.html', context)
