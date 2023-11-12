from django import views
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


class IndexView(views.View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'sample_app/index.html')
