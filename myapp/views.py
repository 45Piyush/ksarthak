from django.shortcuts import render, HttpResponse

def index_page(request):
    return render(request,'index.html')