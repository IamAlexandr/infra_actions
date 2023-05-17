from django.http import HttpResponse


def index(request):
    return HttpResponse('Y меня получилось!')


def second_page(request):
    return HttpResponse('A это вторая страница')
