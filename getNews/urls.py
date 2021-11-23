from django.urls import path, re_path

from getNews import views

urlpatterns = [
    path('', views.index, name='index'),
    path('general/', views.category, name="general"),
    path('business/', views.category, name="business"),
    path('sport/', views.category, name="sport"),
    path('entertainment/', views.category, name="entertainment"),
    path('science_nature/', views.category, name="science-nature"),
    path('technology/', views.category, name="technology"),
    path('search/', views.search, name="search"),
    path('trending/', views.trending, name="trending"),
    #Check for updated way
    re_path(r'^(?P<paper_id>[0-9]+)/$', views.paper, name="paper")
]
