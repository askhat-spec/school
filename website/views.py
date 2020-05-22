from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Timetable, Teachers, Awards


class MainPageView(ListView):
    model = Post
    queryset = Post.objects.all()[:2]
    template_name = 'index.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'news_detail.html'


class NewsPageView(ListView):
    model = Post
    paginate_by = 15
    queryset = Post.objects.all()
    template_name = 'news.html'


class TimetablePageView(ListView):
    model = Timetable
    queryset = Timetable.objects.all()
    template_name = 'timetable.html'


class TeachersPageView(ListView):
    model = Teachers
    paginate_by = 20
    queryset = Teachers.objects.all()
    template_name = 'teachers.html'


class AwardsPageView(ListView):
    model = Awards
    paginate_by = 20
    queryset = Awards.objects.all()
    template_name = 'awards.html'


def sections(request):
    return render(request, 'sections.html', {})