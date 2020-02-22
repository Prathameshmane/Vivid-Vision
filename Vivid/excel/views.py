from django.shortcuts import render
from . models import Table
# Create your views here.

def index_excel(request):
    tabs = Table.objects.all()
    return render(request,'excel/table.html',{'tabs': tabs})
