from django.shortcuts import render

# Create your views here.
def jinga_printing(request):
    d={'name':'Monika','age':25,'Education':'B.pharm'}
    return render(request,'jinga_printing.html',d)