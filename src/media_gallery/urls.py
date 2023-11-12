from django.urls import path
from . import views

app_name = "media_gallery"

urlpatterns = [
    path('list/', views.ListView.as_view(), name="list"),
]
