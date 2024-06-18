

from django.urls import path
from bboard.views import index, by_rubric
app_name='bboard'
urlpatterns = [
    path('<int:rubric_id>/', by_rubric,name='by_rubric'),
    path('',index,name='index'),
]
