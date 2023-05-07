from django.shortcuts import render


#create your views here

def store(request):
    context = {}
    return render(request, 'store/store.html')