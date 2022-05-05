from datetime import datetime
from random import randint

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest


class DatetimeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        now = datetime.now()

        return HttpResponse(now)


class RandomintView(View):
    def get(self, requset: HttpRequest) -> HttpResponse:
        random_ = randint(1, 100000)

        return HttpResponse(random_)