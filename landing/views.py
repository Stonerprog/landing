from django.http import HttpResponse
from django.shortcuts import render

# def first_page(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

# def first_page(request):
#     new_phrase = "<h1>Bla-bla-bla</h1>"
#     return HttpResponse(new_phrase)

def first_page(request):
    a = 'some text'
    b = "one more message"
    return render(request, 'index.html', {"a": a, "b": b})