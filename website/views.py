from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Timetable, Teachers


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


def index(request):
    return render(request, 'index.html', {})


# def teachers(request):
#     return render(request, 'teachers.html', {})

class TeachersPageView(ListView):
    model = Teachers
    queryset = Teachers.objects.all()
    template_name = 'teachers.html'



def awards(request):
    return render(request, 'awards.html', {})


def sections(request):
    return render(request, 'sections.html', {})