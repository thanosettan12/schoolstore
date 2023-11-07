from django.shortcuts import render
from storeapp.models import Accomplishments
from storeapp.models import Resources

# Create your views here.
def home(request):
    obj1 = Accomplishments.objects.all()
    kum= Resources.objects.all()
    return render(request, 'home.html',{'result':obj1,'results':kum })


# def accom(request):
#     obj = Accomplishments.objects.all()
#     return render(request, 'home.html', {'result': obj})