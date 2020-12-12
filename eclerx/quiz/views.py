from django.shortcuts import render
from . models import Test
# Create your views here.


def exam(request):
    results = Test.objects.all()
    return render(request, 'index.html', {"Test": results})