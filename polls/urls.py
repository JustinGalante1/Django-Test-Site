from django.urls import path

# in polls directory

from . import views

app_name = 'polls'
urlpatterns = [
    # /polls/
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # /polls/5/
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # polls/5/results/
    # path('<int:question_id>/results', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('suggestions/', views.suggestions, name='suggestions'),
    path('suggestions/list/', views.suggestions_list, name='suggestions_list'),
]
