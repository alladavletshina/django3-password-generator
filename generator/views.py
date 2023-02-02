from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def about(request):
    return render(request,'generator/about.html')

def home(request):
    return render(request,'generator/home.html')

def password(request):

    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        characters.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('numbers'):
        characters.extend(list('0987654321'))
    if request.GET.get('special'):
        characters.extend(list(',?.,"@[]()'))
    length = int(request.GET.get('length', 12))
    thepassword = ''

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request,'generator/password.html',{'password':thepassword})