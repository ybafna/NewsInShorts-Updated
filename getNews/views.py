import requests
import datetime
from django.shortcuts import render

# Create your views here.
from getNews.models import News, Source


def index(request):
    # get_source()
    # get_all_news()
    all_news = News.objects.all()
    print(all_news)
    all_sources = Source.objects.all()
    return render(request, 'News/homePage.html', {'allNews': all_news, 'allSource': all_sources})


def get_all_news():
    for news in News.objects.all():
        News.objects.get(id=news.id).delete()
    sources = Source.objects.all()
    for source in sources:
        articles = []
        try:
            url = 'https://newsapi.org/v1/articles?source='+source.source_id+'&apiKey=395c9ded48d34f04b6a2fc809d232bc3'
            r = requests.get(url)
            articles = r.json()['articles']
        except:
            pass

        for article in articles:
            news = News()
            news.author = article["author"]
            news.title = article["title"]
            news.description = article["description"]
            news.url = article["url"]
            news.urlToImage = article["urlToImage"]
            date_string = article["publishedAt"]

            try:
                date_string = date_string[0:19]
                news.publishedDate = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S")
            except:
                pass
            news.source = source
            news.save()


# Get top 10 news for every category
def trending(request):
    general_news = get_category_news('general')[0:6]
    sport_news = get_category_news('sport')[0:6]
    business_news = get_category_news('business')[0:6]
    entertainment_news = get_category_news('entertainment')[0:6]
    science_and_nature_news = get_category_news('science-and-nature')[0:6]
    technology_news = get_category_news('technology')[0:6]
    context = {
        'generalNews': general_news,
        'sportNews': sport_news,
        'businessNews': business_news,
        'entertainmentNews': entertainment_news,
        'scienceAndNatureNews': science_and_nature_news,
        'technologyNews': technology_news,

    }
    return render(request, 'News/trending.html', context)


# Get news for a specific newspaper
def paper(request, paper_id):
    paper_source = Source.objects.get(pk=paper_id)
    paper_news = get_image_news(paper_source.source_id)
    context = {
        'paperNews': paper_news,
        'paperNewsTop': paper_news[0:6],
        'paperName': paper_source.name
    }
    return render(request, 'News/paper.html', context)


def get_source():
    for source in Source.objects.all():
        Source.objects.get(id=source.id).delete()
    url = "https://newsapi.org/v1/sources?language=en"
    r = requests.get(url)
    sources = r.json()['sources']
    for source in sources:
        s = Source()
        s.source_id = source["id"]
        s.name = source["name"]
        s.description = source["description"]
        s.url = source["url"]
        category_str = source["category"]
        if category_str == 'science-and-nature':
            category_str = 'science_nature'
        s.category = category_str
        s.country = source["country"]
        s.urlsToLogos_large = source["urlsToLogos"]["large"]
        s.urlsToLogos_medium = source["urlsToLogos"]["medium"]
        s.urlsToLogos_small = source["urlsToLogos"]["small"]
        s.save()


# Get Categorical News
def category(request):
    url = request.get_full_path()
    urls = url.split('/')
    # if request.user.is_authenticated:
        # u = UserProfile.objects.get(user=request.user)
        # at = getattr(u, urls[2])
        # at = at + 1
        # setattr(u, urls[2], at)
        # u.save()

    category_news = get_category_news(urls[2])
    context = {
        'paperNews': category_news,
        'paperNewsTop': category_news[0:6],
        'paperName' : urls[2].upper()
    }
    return render(request, 'News/paper.html', context)


# Get all news with valid images
def get_image_news(source_str):
    all_news = News.objects.all()
    valid_image_news = []
    for news in all_news:
        if news.source.source_id == source_str and news.urlToImage:
            valid_image_news.append(news)
    return valid_image_news


# Get all news for a particular category
def get_category_news(cat):
    all_source = Source.objects.all().filter(category=cat)
    all_news = News.objects.all().filter(source__in=all_source).order_by('-publishedDate')
    category_news = []
    for news in all_news:
        if news.urlToImage:
            category_news.append(news)
    return category_news


# Get all news based on a search key
def search(request):
    keyword_news = set()
    keyword = request.POST['keyword'].lower()
    keyword_string = keyword.split(' ')
    all_news = News.objects.all()
    for news in all_news:
        title = news.title.split(' ')
        for s in title:
            if s.lower() in keyword_string:
                keyword_news.add(news)

    context = {
        'keywordNews': list(keyword_news),
        'keyword': keyword
    }

    return render(request, 'News/search.html', context)


# Check if the user is logged in or not
# def login_check(request):
#     all_news = News.objects.all()
#     all_source = Source.objects.all()
#     if request.user.is_authenticated:
#         u = UserProfile.objects.get(user=request.user)
#         if ((u.sport == 0 and u.general == 0) and (u.business == 0 and u.technology == 0)) and (
#                 u.science_nature == 0 and u.entertainment == 0):
#             return render(request, 'getNews/homePage.html', {'allNews': all_news, 'allSource': all_source})
#         else:
#             categories = {'sport': u.sport, 'general': u.general, 'business': u.business, 'technology': u.technology,
#                           'science_nature': u.science_nature, 'entertainment': u.entertainment}
#             large = max(list, key=categories.get)
#             return redirect(large)