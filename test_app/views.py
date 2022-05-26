from datetime import datetime
from random import randint
from django.contrib import auth
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpRequest
from pyweb_2021_1_shilo.settings import VERSION_SERVER

class DatetimeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        now = f'Username: {request.user.username} Server version: {VERSION_SERVER}'

        return HttpResponse(now)


class RandomintView(View):
    def get(self, requset: HttpRequest) -> HttpResponse:
        random_ = randint(1, 100000)

        return HttpResponse(random_)