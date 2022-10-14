from django.http import HttpResponse
from django.shortcuts import render

def first_page(request):
    a = 'Новая страница'
    text = 'Новый текст'
    text1 = 'еще строка текста'
    return render(request, './index.html', {
        'a':a,
        'text':text,
        'text1':text1
    })