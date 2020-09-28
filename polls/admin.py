from django.contrib import admin
from .models import Question

# Register your models here.
#making it to where the question model can be accessed from admin site
admin.site.register(Question)
