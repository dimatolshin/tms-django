from django_rq import job

from .models import Question, Choice

@job
def add_view_count(question:Question):
    question.view_count += 1
    question.save()


