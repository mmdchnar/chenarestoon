from django.urls import path
from . import views


urlpatterns = [
        path('', views.index),
        path('<int:question_id>/', views.detail),
        path('<int:question_id>/results/', views.results),
        path('<int:question_id>/vote/', views.vote),
]

