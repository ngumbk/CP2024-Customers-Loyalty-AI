from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the cp2024-cl-ai index.")
