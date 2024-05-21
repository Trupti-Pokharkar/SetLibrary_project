from django.contrib import admin
from . models import Library
from . models import Student
from. models import Emp

class LibraryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'publisher', 'publication', 'pages', 'price')
    search_fields = ('name', 'author', 'publisher')  
    list_filter = ('publisher', 'publication') 

admin.site.register(Library, LibraryAdmin)

class StudentAdmin(admin.ModelAdmin):
     list_display = ('stuid', 'name', 'book', 'date', 'rdate')
admin.site.register(Student, StudentAdmin)


class EmpAdmin(admin.ModelAdmin):
    list_display = ('empid', 'name', 'email', 'Mob', 'pos')
admin.site.register(Emp, EmpAdmin)

