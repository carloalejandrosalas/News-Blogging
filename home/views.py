from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse('loquesea')
    return render(request, 'home/index.html')