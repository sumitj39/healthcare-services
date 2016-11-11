from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from models import Disease
import os
from forms import SearchForm
from models import Disease,Location,Hospital,DiseaseService,Specialization,Service

# Create your views here.

def index(request):
    return render(request, 'hms/index.html')

def search_hospital(request):
    return render(request,'hms/searchhospital.html')

def reviews(request):
    if request.method == 'POST':
        return HttpResponse("<h2>THANKS FOR YOUR REVIEW</h2> ")
    return render(request,'hms/review.html')

def results(request):
    if request.method == 'POST':
        print("COMING")
        myform=SearchForm(request.POST)
        if myform.is_valid():
            dname = myform.cleaned_data['disease_name']
            lname = myform.cleaned_data['location_name']
            d = Disease.objects.get(dname=dname)
            l = Location.objects.get(lname = lname)
            htodisp = Hospital.objects.all().filter(hlocation=l)
            """ds = DiseaseService.objects.all().filter(sdisease=d)
            spl = Specialization.objects.all().filter(hosp=htodisp,disease_service=ds)
            rate = spl.rate
            unit_price = ds.dservice.unit_price
            print"""
    return render(request,'hms/results.html',context={'htodisp':htodisp})