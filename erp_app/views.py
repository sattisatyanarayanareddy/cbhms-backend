from django.shortcuts import render,redirect
from .forms import Patient_details,Doctors_login
from .models import Doctors_Details
from django.http import HttpResponse
import cloudinary.uploader
from django.db.models import Q
from django.conf import settings
import json
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        patient_form = Patient_details(request.POST,request.FILES)
        if patient_form.is_valid():
            username = patient_form.cleaned_data['username']
            password = patient_form.cleaned_data['password']
            email = patient_form.cleaned_data['email']
            mobile = patient_form.cleaned_data['mobile']
            languages = patient_form.cleaned_data['languages']
            name = patient_form.cleaned_data['name']
            age = patient_form.cleaned_data['age']
            gender = patient_form.cleaned_data['gender']

            image = patient_form.cleaned_data['img']

            folder = 'patient_profile_images'
            uploading = cloudinary.uploader.upload(image,
            folder = folder,
            api_key = settings.CLOUDINARY_STORAGE['API_KEY'],
            api_secret = settings.CLOUDINARY_STORAGE['API_SECRET'],
            cloud_name = settings.CLOUDINARY_STORAGE['CLOUD_NAME'])
            profile_path = uploading['secure_url']
            if not Doctors_Details.objects.filter(Q(username = username)).exists():
                Doctors_Details.objects.create(
                    name = name,
                    age = age,
                    gender = gender,
                    profile_path = profile_path,
                    email = email,
                    username = username,
                    password = password,
                    mobile = mobile,
                    languages = languages,
                )
                print("details stored......")
                """res_data = {}
                res_data['result'] = 'Success'
                res_data['message'] = 'Docter Added'
                
                return HttpResponse(json.dumps(res_data),content_type="application/json")"""
                return redirect('admin_dashboard')
            else:
                print("User name already exist")
                return render(request,'home.html',status = 400)
        else:
            print("invalid form submission")
            return render(request,'home.html',status = 403)
    else:
        return redirect('home')

def admin_dashboard(request):
    data = Doctors_Details.objects.all()
    return render(request,'admin_dashboard.html',{'data':data})

def doctor_login(request):
    return render(request,'doctor_login.html')
def doctor_validate(request):
    if request.method == 'POST':
        doctor_login = Doctors_login(request.POST)
        if doctor_login.is_valid():
            username = doctor_login.cleaned_data['username']
            password = doctor_login.cleaned_data['password']
            if Doctors_Details.objects.filter(Q(username=username)).exists():
                patient = Doctors_Details.objects.get(username=username)
                if patient.password == password:
                    print("passwords matched")
                    return redirect('doctor_dashboard')
                else:
                    return render(request,'doctor_login.html',{'err_msg':'wrong password'},status=401)
            else:
                return render(request,'doctor_login.html',{'err_msg':'user not exists'},status=401)
    return redirect('doctor_login')

def doctor_dashboard(request):
    return render(request,'doctor_dashboard.html')         
    