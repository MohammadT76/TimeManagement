from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View


class Hello(View):
    def get(self,request):
        return HttpResponse('hello and welcome to this website .')
