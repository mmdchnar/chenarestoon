from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from . import views


app_name = 'polls'

urlpatterns = [
        path('', views.IndexView.as_view(), name='index'),
        path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('polls/images/favicon.ico'))),
        path('<int:pk>/', views.DetailView.as_view(), name='detail'),
        path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
        path('<int:question_id>/vote/', views.vote, name='vote'),
]

