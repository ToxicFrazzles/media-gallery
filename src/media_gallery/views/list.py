from django import views
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from ..models import MediaFile


@method_decorator(csrf_exempt, name='dispatch')
class ListView(views.View):
    def post(self, request: HttpRequest) -> HttpResponse:
        start = request.POST.get(key="start", default=-1)
        limit = request.POST.get(key="limit", default=30)
        limit = max(min(limit, 30), 1)

        media = MediaFile.objects.filter().order_by("-date")
        if start > 0:
            media = media[start:start+limit]
        else:
            media = media[:limit]

        result = [
            (m.file.url, m.name, m.date)
            for m in media
        ]
        return JsonResponse({'list': result})
