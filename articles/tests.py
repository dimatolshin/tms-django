from django.test import TestCase
from django.urls import reverse

from .views import Article


def create_article(title, text, author, like_count):
    return Article.objects.create(title=title, text=text, author=author, like_count=like_count)


class ArtilceTest(TestCase):
    def test_empty_list(self):
        article = self.client.get(reverse('articles:main'))
        self.assertEquals(article.status_code, 200)
        self.assertContains(article, 'There are no articles')

    def test_new_list(self):
        article = create_article('1', '2', '3', 4)
        response = self.client.get(reverse("articles:main"))
        self.assertEquals(response.status_code, 200)
        self.assertQuerysetEqual(response.context['articles'], [article])

    def test_get_404_mistake(self):
        article = create_article('1', '2', '3', 4)
        response = self.client.get(reverse('articles:title', args=[3]))
        self.assertEqual(response.status_code, 404)

    def test_article_objects(self):
        article = create_article('1', '2', '3', 4)
        response = self.client.get(reverse('articles:title', args=[article.id]))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, article.text)

    def test_is_popylar(self):
        article = Article(like_count=10000)
        self.assertTrue(article.is_popular())

    def test_is_no_popylar(self):
        article = Article(like_count=1)
        self.assertFalse(article.is_popular())

