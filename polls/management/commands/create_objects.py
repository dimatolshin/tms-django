from django.core.management import BaseCommand
from polls.models import Choice, Question
from django.utils import timezone
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        Question1 = Question.objects.create(question_text="Are you Dima?", pub_date=timezone.now())
        Choice1 = Choice.objects.create(question=Question1, choice_text='No', votes=0)
        Choice2= Choice.objects.create(question=Question1,choice_text="Yes",votes=0)

    with open('data.json','r') as data:
        json.load(data)
        for question_text,choice_list in data.items():
            pass


