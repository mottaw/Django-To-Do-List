from django.urls import path
from django.http import HttpResponse

def test(request):
    return HttpResponse("ok")

urlpatterns = [
    path('', test),
]