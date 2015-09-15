from django.test import TestCase
from django.core.urlresolvers import reverse
from article.models import Article
from django.test import TestCase, Client
from django.http.response import HttpResponse

import unittest


import datetime
from django.utils import timezone


# Create your tests here.
class ArticleMethodTests(TestCase):

    def test_was_published_recently_with_future_article(self):
        """
        was_published_recently() should return False for articles whose
        pub_date is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        
        future_article = Article(article_date=time,article_text="Future text", article_title="Future title")
        self.assertEqual(future_article.was_published_recently(), False)

def create_article(article_text, article_title, days):
    """
    Creates a article with the given `article_text` published the given
    number of `days` offset to now (negative for articles published
    in the past, positive for articles that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Article.objects.create(article_text=article_text,
                                   article_date=time)
class articleViewTests(TestCase):
    def test_index_view_with_a_past_article(self):
        """
        articles with a pub_date in the past should be displayed on the
        index page.
        """
        create_article(article_text="Past article.", article_title="Past article.", days=-30)
        response = self.client.get(reverse('article:main'))
        
        self.assertQuerysetEqual(
            response.context['latest_article_list'],
            ['<Article: Past article.>']
        )



class TestBasic(unittest.TestCase):
    "Basic tests"

    def test_basic(self):
        a = 1
        self.assertEqual(1, a)

    def test_basic_2(self):
        a = 1
        assert a == 1