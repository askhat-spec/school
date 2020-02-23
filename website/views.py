from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Timetable, Teachers, Awards


def index(request):
    return render(request, 'index.html', {})


def detail_view(request, slug):
    post = Post.objects.get(slug__iexact = slug)
    return render(request, 'news_detail.html', context={'post':post})


class NewsPageView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = 'news.html'


class TimetablePageView(ListView):
    model = Timetable
    queryset = Timetable.objects.all()
    template_name = 'timetable.html'


class TeachersPageView(ListView):
    model = Teachers
    queryset = Teachers.objects.all()
    template_name = 'teachers.html'


class AwardsPageView(ListView):
    model = Awards
    queryset = Awards.objects.all()
    template_name = 'awards.html'


def sections(request):
    return render(request, 'sections.html', {})