from django.db import models
from .models import Profile,Job_Profile,Education,Project,Experience,Applied
from django.contrib import admin


# Register your models here.
admin.site.register(Profile)
admin.site.register(Job_Profile)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Experience)
admin.site.register(Applied)
