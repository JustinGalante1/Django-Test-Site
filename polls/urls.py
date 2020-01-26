from django.urls import path

# in polls directory

from . import views

app_name = 'polls'
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/5/
    path('specifics/<int:question_id>/', views.detail, name='detail'),
    # polls/5/results/
    path('<int:question_id>/results', views.results, name='results'),
    # polls/5/vote/
    path('<int:question_id>/vote', views.vote, name='vote')
]
