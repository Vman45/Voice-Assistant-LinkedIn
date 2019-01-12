from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django import forms
#from .forms import SignupForm ,UserFormlog,ProfileForm ,Inputlog
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
#from .tokens import account_activation_token
from django.contrib.auth.models import User
#from django.contrib.auth.models import check_password
from django.core.mail import EmailMessage
from django.contrib import auth
from .models import Profile,Job_Profile,Education,Experience,Project
from django.http import JsonResponse


def index(request,string=None):
      a=string
      template = a+'.html'
      # collecting data for the demo profile
      username = "Ishita Rathi"
      basic_details = Profile.objects.get(full_name=username)
      print (basic_details.full_name)
      education = Education.objects.filter(user=basic_details).distinct()
      experience = Experience.objects.filter(user=basic_details).distinct()
      projects = Project.objects.filter(user=basic_details).distinct()

      if request.method == 'POST':
         query = request.POST.get('search')
         print(query)
         if query:
            results2 = Job_Profile.objects.filter(Company__icontains=query).distinct()
            results1 = Job_Profile.objects.filter(designation__icontains=query).distinct()
            print(results1)
            results = results1 | results2
            profiles = Profile.objects.filter(full_name__icontains=query).distinct()            
            print(results)
         else:
            results = []
            profiles = []
         return render(request, 'displayJobs.html', {
        'query': query, 'results': results ,'profiles': profiles ,
         })
      return render(request, template,  #user_form
        {'basic_details': basic_details, 'education': education, 'experience': experience,
         'projects' :projects})

def addEdu(request):
      username = "Ishita Rathi"
      basic_details = Profile.objects.get(full_name=username)
      if request.method == 'POST':
         college = request.POST.get('college')
         course = request.POST.get('course')
         new_edu = Education(user=basic_details,college=college,course=course)
         new_edu.save()
         msg = "Education successfully added!"
         return render(request, 'addEdu.html', {
        'msg': msg   })
         return redirect('profile.html')
      return render(request, 'addEdu.html')

def addProject(request):
      username = "Ishita Rathi"
      basic_details = Profile.objects.get(full_name=username)
      if request.method == 'POST':
         title = request.POST.get('title')
         description = request.POST.get('description')
         new_project = Project(user=basic_details,title=title,description=description)
         new_project.save()
         msg = "New Project successfully added!"
         return render(request, 'addProject.html', {
        'msg': msg   })

      return render(request, 'addProject.html')

def addExp(request):
      username = "Ishita Rathi"
      basic_details = Profile.objects.get(full_name=username)
      if request.method == 'POST':
         designation = request.POST.get('designation')
         company = request.POST.get('company')
         start_date = request.POST.get('start_date')
         end_date = request.POST.get('end_date')
         description = request.POST.get('description')
         course = request.POST.get('course')         
         new_exp = Experience(user=basic_details,designation=designation,company=company,start_date=start_date,end_date=end_date,description=description)
         new_exp.save()
         msg = "New experience successfully added!"
         return render(request, 'addExp.html', {
        'msg': msg   })

      return render(request, 'addExp.html')
    
def jobDetail(request,id=None):
      idone=id
      username = "Ishita Rathi"
      job_details = Job_Profile.objects.get(id=idone)
      return render(request, 'job_profile.html',{'job_details':job_details})
    
def process(request):
      if request.is_ajax():
        #output = request.raw_post_data
        output = request.GET.get('color', None)    
        print(output)
      print("ajax call is made")
      data = {
            'res': "happy"
            }
      return JsonResponse(data)







      
