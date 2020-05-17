from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Timetable, Teachers, Awards


class MainPageView(ListView):
    model = Post
    queryset = Post.objects.order_by('publish').reverse()[:2]
    template_name = 'index.html'


def news_detail_view(request, slug):
    post = Post.objects.get(slug__iexact = slug)
    return render(request, 'news_detail.html', context={'post':post, 
                                                        'object':Post.objects.get(slug = slug)})


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
    paginate_by = 16
    queryset = Teachers.objects.all()
    template_name = 'teachers.html'


class AwardsPageView(ListView):
    model = Awards
    paginate_by = 16
    queryset = Awards.objects.all()
    template_name = 'awards.html'


def sections(request):
    return render(request, 'sections.html', {})