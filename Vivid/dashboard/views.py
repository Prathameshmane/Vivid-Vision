from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
import datetime
# Create your views here.

@login_required
def base_dash(request):
    return render(request, 'dashboard/base_dash.html')
