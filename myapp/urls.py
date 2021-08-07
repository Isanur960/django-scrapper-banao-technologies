from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index.as_view(), name='index'),
    path('scrp', views.Scrape_req.as_view(), name='Scrapper'),
    path('detail', views.Detail.as_view(), name='Detail'),
]
