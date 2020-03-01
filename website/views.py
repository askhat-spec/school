from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Timetable, Teachers, Awards


def index(request):
    return render(request, 'index.html', {})


def news_detail_view(request, slug):
    post = Post.objects.get(slug__iexact = slug)
    return render(request, 'news_detail.html', context={'post':post})


class NewsPageView(ListView):
    model = Post
    paginate_by = 1
    queryset = Post.objects.all()
    template_name = 'news.html'


class TimetablePageView(ListView):
    model = Timetable
    queryset = Timetable.objects.all()
    template_name = 'timetable.html'


class TeachersPageView(ListView):
    model = Teachers
    paginate_by = 1
    queryset = Teachers.objects.all()
    template_name = 'teachers.html'


class AwardsPageView(ListView):
    model = Awards
    paginate_by = 1
    queryset = Awards.objects.all()
    template_name = 'awards.html'


def sections(request):
    return render(request, 'sections.html', {})