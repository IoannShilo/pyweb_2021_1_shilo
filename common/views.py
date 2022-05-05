from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest

class HelloworldView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        a = "<h1>Hello, World</h1>"

        return HttpResponse(a)

class IndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'common/index.html')
