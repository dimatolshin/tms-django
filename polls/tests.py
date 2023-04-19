from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Question


class QuestionModelTest(TestCase):
    def test_was_published_recently(self):
        pub_date = timezone.now() - timezone.timedelta(hours=2)
        question = Question(pub_date=pub_date)
        self.assertTrue(question.was_published_recently())

    def test_was_no_published_recently(self):
        pub_date = timezone.now() - timezone.timedelta(days=2)
        question = Question(pub_date=pub_date)
        self.assertFalse(question.was_published_recently())

    def test_was_no_publishe_recently(self):
        pub_date = timezone.now() + timezone.timedelta(days=2)
        question = Question(pub_date=pub_date)
        self.assertFalse(question.was_published_recently())


def create(question_text, days):
    pub_date = timezone.now() + timezone.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=pub_date)


class QuestionIndexViewTest(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, 'No polls are available')

    def test_future_question_and_past_question(self):
        past_question = create('past', -30)
        create('future', 30)
        response= self.client.get(reverse('polls:index'))
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(response.cotext['latest_question_list'],[past_question])