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
from .models import Profile,Job_Profile,Education,Experience,Project,Applied
from django.http import JsonResponse
from django.http import HttpResponse
# nlp libraries
import re
import nltk
from nltk.corpus import stopwords
import requests
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tokenize import word_tokenize

def Transform(inputString, lower = True):
    """
    Removes puctuation marks, lowers and splits the string into words and removes stop words from the list
    """
    # remove punctuation marks from string
    string = re.sub("[^a-zA-Z0-9]", " ", inputString)
    
    if(lower):
        string = string.lower()
    
    #split the string
    words = string.split()
    
    #remove stop words
    stopwrds = set(stopwords.words("english"))
    noSW = [w for w in words if w not in stopwrds]
    
    return noSW


def index(request,string=None):
      a=string
      print(a)
      if(a=="" or a==None):
         a="profile"
      template = a+'.html'
      # collecting data for the demo profile
      username = "Ishita Rathi"
      basic_details = Profile.objects.get(full_name=username)
      print (basic_details.full_name)
      education = Education.objects.filter(user=basic_details).distinct()
      experience = Experience.objects.filter(user=basic_details).distinct()
      projects = Project.objects.filter(user=basic_details).distinct()
      jobs_applied = Applied.objects.filter(user=basic_details).distinct()
      jobs=[]
      for job in jobs_applied:
          jobs.append(job.job)
      print(jobs_applied)
      if request.method == 'POST':
         query = request.POST.get('search')
         print(query)
         if query:
            queries = query.split(',')
            if(len(queries)<2):
                  #queries.append(queries[0])
                  results2 = Job_Profile.objects.filter(Company__icontains=queries[0]).distinct()
                  results1 = Job_Profile.objects.filter(designation__icontains=query[0]).distinct()
                  results3 = Job_Profile.objects.filter(location__icontains=query[0]).distinct()                  
                  print(results1)
                  results = results1 | results2 | results3
                  profiles1 = Profile.objects.filter(full_name__icontains=queries[0]).distinct()
                  profiles2 = Profile.objects.filter(current_company__icontains=queries[0]).distinct()            
                  profiles =profiles1 | profiles2
                  print(results)
                  return render(request, 'displayJobs.html', {
                  'query': query, 'results': results ,'profiles': profiles , 'applied':jobs,
                 })
            else:
                  results = []
                  profiles1 = Profile.objects.filter(full_name__icontains=queries[0]).distinct()            
                  profiles2 = Profile.objects.filter(current_company__icontains=queries[1]).distinct()            
                  profiles= profiles1 & profiles2
                  return render(request, 'displayJobs.html', {
                  'query': query, 'results': results ,'profiles': profiles ,'applied':jobs,
                 })
      print(jobs_applied)            
      return render(request, template,  #user_form
        {'basic_details': basic_details, 'education': education, 'experience': experience,
         'projects' :projects,'applied':jobs,})

def allJobs(request):
      template = 'jobs.html'
      # collecting data for the demo profile
      username = "Ishita Rathi"
      basic_details = Profile.objects.get(full_name=username)      
      jobs_applied = Applied.objects.filter(user=basic_details).distinct()
      jobs=[]
      for job in jobs_applied:
          jobs.append(job.job)
      print(jobs)      
      results = Job_Profile.objects.all()
      return render(request, template , {
                  'results': results,'applied':jobs, })

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
      basic_details = Profile.objects.get(full_name=username)
      job_details = Job_Profile.objects.get(id=idone)
      status = Applied.objects.filter(user=basic_details,job=job_details).distinct()
      print(status)
      applied="false"
      if status:
          applied="true"
      print(applied)
      return render(request, 'job_profile.html',{'job_details':job_details, 'status':applied})

def applyJob(request,id=None):
      idone=id
      username = "Ishita Rathi"
      basic_details = Profile.objects.get(full_name=username)
      job_details = Job_Profile.objects.get(id=idone) 
      new_application = Applied(user=basic_details,job=job_details)
      new_application.save()
      return jobDetail(request, idone)


def profileDetail(request,id=None):
      idone=id
      username = "Ishita Rathi"
      job_details = Profile.objects.get(id=idone)
      education = Education.objects.filter(user=job_details).distinct()
      experience = Experience.objects.filter(user=job_details).distinct()
      projects = Project.objects.filter(user=job_details).distinct()

      return render(request, 'person_profile.html',{'job_details':job_details,'education':education,
                               'experience':experience, 'projects':projects })

def findEntity(inputData):
      doc = inputData
      # tokenize doc
      tokenized_doc = nltk.word_tokenize(doc)
       
      # tag sentences and use nltk's Named Entity Chunker
      tagged_sentences = nltk.pos_tag(tokenized_doc)
      ne_chunked_sents = nltk.ne_chunk(tagged_sentences)
       
      # extract all named entities
      named_entities = {}
      for tagged_tree in ne_chunked_sents:
          if hasattr(tagged_tree, 'label'):
              entity_name = ' '.join(c[0] for c in tagged_tree.leaves()) #
              entity_type = tagged_tree.label() # get NE category
              named_entities[entity_name] = entity_type
      print(named_entities)
      return named_entities

    
def process(request):
      if request.is_ajax():
        output = request.GET.get('color', None)
        synWord =[['find a lost item', 'find', 'find inform', 'rout up', 'explore', 'forag', 'frisk', 'hunt', 'look', 'manhunt', 'pursuit',
                     'quest', 'ransack', 'scour', 'search'],['add', 'comput a sum', 'add on', 'adjoin', 'button', 'butyl', 'compound', 'concaten',
                  'enrich', 'foot', 'fortifi','gild the lili', 'include', 'inject', 'intercal']]
        word1 = "search"
        word2 = "add"

        wordList = [word1, word2]
      #for number in range(1, 6):
        words = Transform(output)

        print("Tranformed string is: " + str(words))
        result="apply"
        flag = 0
        for word in words:
          for idx, synonyms in enumerate(synWord): 
              if(word in synonyms):
                  result = wordList[idx]
                  print("Operation: " + wordList[idx])
                  flag = 1
                  break
              
          if(flag == 1):
              break

        #if(flag == 0):
        #  result = "You are not speaking a valid operation"
        #  print("You are not speaking a valid operation")
        #else:
        if result=="add":
              #here write code for addition
            link="profile"
            for word in words:
                if word=="experience" or word=="profile" or word=="education" or word=="project":
                    link=word
            data = {
                  'link': link,
                  'operation':result
                  }
            return JsonResponse(data)
        elif result=="apply":
             print("done")
             dictionary = findEntity(output)
             print(dictionary)
             data = {
                  'result': 'result',
                  }
             return JsonResponse(data)

        else:
              print("search action")
              result="search"
                          # code for performing search query
              results = []
              profiles = []
              dictionary = findEntity(output)
              org=""
              person=""
              entity=""
              location=""
              for key, value in dictionary.items():
                  if(value=="ORGANIZATION"):
                        print(key,value)
                        org=key                                               
                                    #results2 = Job_Profile.objects.filter(Company__icontains=value).distinct()
                                    #results1 = Job_Profile.objects.filter(designation__icontains=query).distinct()
                                    #print(results1)
                                    #results = results1 | results2
                  elif(value=="PERSON"):
                        person=key  
                        #profiles = Profile.objects.filter(full_name__icontains=value).distinct()            
                        print(results)
                  else:
                      entity=value
              data = { 'org': org, 'person':person,'operation':result,'entity':entity
                                }      
              return JsonResponse(data)          
                    #return render(request, 'displayJobs.html', {
                     #           'query': value, 'results': results ,'profiles': profiles ,
                      #           })

                                
                    
        print(output)
        print("ajax call is made")
        data = {
                  'res': result
                  }
      return JsonResponse(data)






      
