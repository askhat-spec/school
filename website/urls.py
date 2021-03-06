from django.urls import path
from . import views


urlpatterns = [
    path('', views.MainPageView.as_view(), name="index"),
    path('teachers', views.TeachersPageView.as_view(), name="teachers"),
    path('timetable', views.TimetablePageView.as_view(), name="timetable"),
    path('awards', views.AwardsPageView.as_view(), name="awards"),
    path('sections', views.sections, name="sections"),
    path('news/<slug>/', views.PostDetailView.as_view(), name='detail'),
    path('news', views.NewsPageView.as_view(), name='news'),
]