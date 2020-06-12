from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# Create your views here.
def home(req):
    return render(req, 'index.html')


@login_required
def dashboard(req):

    return render(req, 'dashboard.html')
