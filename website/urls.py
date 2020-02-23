from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('teachers', views.TeachersPageView.as_view(), name="teachers"),
    path('timetable', views.TimetablePageView.as_view(), name="timetable"),
    path('awards', views.awards, name="awards"),
    path('sections', views.sections, name="sections"),
    path('news/<slug>/', views.detail_view, name='detail'),
    path('news', views.NewsPageView.as_view(), name='news'),
]