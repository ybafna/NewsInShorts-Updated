from urllib.request import Request

from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from getNews.models import Source, News
from getNews.views import get_category_news, get_image_news, search


def create_source(index):
    Source.objects.create(source_id=str(index),
                          name="SourceName" + str(index),
                          description="Description" + str(index),
                          url="URL" + str(index),
                          category="Category" + str(index),
                          country="Country" + str(index),
                          urlsToLogos_small="SmallLogo" + str(index),
                          urlsToLogos_medium="MediumLogo" + str(index),
                          urlsToLogos_large="LargeLogo" + str(index))


def create_sources(n):
    for i in range(n):
        create_source(i + 1)


def create_news_object(index, source_index):
    News.objects.create(author="Author" + str(index),
                        title="Title" + str(index),
                        description="Description" + str(index),
                        url="URL" + str(index),
                        urlToImage="UrlToImage" + str(index),
                        publishedDate="2021-11-01",
                        source=Source.objects.get(source_id=source_index)
                        )


def create_news(n, source_index):
    for i in range(n):
        create_news_object(i + 1, str(source_index))


class SourceTestCase(TestCase):
    def setUp(self):
        for source in Source.objects.all():
            Source.objects.get(id=source.id).delete()

        for news in News.objects.all():
            News.objects.get(id=news.id).delete()

    def test_sources(self):
        create_sources(2)
        source1 = Source.objects.get(source_id="1")
        source2 = Source.objects.get(source_id="2")
        self.assertEqual(source1.name, 'SourceName1')
        self.assertEqual(source2.name, 'SourceName2')
        self.assertEqual(source1.category, 'Category1')
        self.assertEqual(source2.category, 'Category2')


class NewsTestCase(TestCase):
    def setUp(self):
        for source in Source.objects.all():
            Source.objects.get(id=source.id).delete()

        for news in News.objects.all():
            News.objects.get(id=news.id).delete()

    def test_category_news(self):
        create_sources(2)
        create_news(2, 1)
        create_news(5, 2)

        category_news_1 = get_category_news("Category1")
        category_news_2 = get_category_news("Category2")

        self.assertEquals(len(category_news_1), 2)
        self.assertEquals(len(category_news_2), 5)

    def test_image_news(self):
        create_sources(2)
        create_news(2, 1)
        create_news(5, 2)

        # Check for news objects with empty urls
        news_object1 = News.objects.all().filter(source__in=["1"]).get(author="Author1")
        news_object1.urlToImage = None
        news_object1.save()

        image_news_1 = get_image_news("1")
        image_news_2 = get_image_news("2")
        self.assertEquals(len(image_news_1), 1)
        self.assertEquals(len(image_news_2), 5)
