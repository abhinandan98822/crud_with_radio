from django.contrib import admin
from . models import Student

# Register your models here.
@admin.register(Student)
class RegisterAdmin(admin.ModelAdmin):
    list_display=['id','name','lastname','username','email','password','salary','gender']
