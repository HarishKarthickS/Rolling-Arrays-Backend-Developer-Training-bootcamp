from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {
        'name': 'Dilasa',
        'age': 20,
        'nationality': 'Indian',
    }
    return render(request, 'index.html', context)

def count(request):
    text = request.POST.get('text')
    word_count = len(text.split())
    char_count = len(text)
    line_count = text.count('\n')
    space_count = text.count(' ')
    return render(request, 'counter.html', {'word_count': word_count, 'char_count': char_count, 'line_count': line_count, 'space_count': space_count})
