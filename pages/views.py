from django.shortcuts import render
import string
import random

# Create your views here.

def index(request):
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
    username = request.user.username
    return render(request, "pages/index.html",{'name': username, 'code':code})