from django.shortcuts import render
from django.http import HttpResponse
import joblib

# Create your views here.

def homepage(request):
    return render(request,'home/home.html')

def salary(request):
    years = request.POST['year'] 
    model = joblib.load('model/Salary_model.pkl')  
    salary = model.predict([[float(years)]])
    data = {"salary":round(salary[0],2)}
    return render(request,'home/home.html',data)
    