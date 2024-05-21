from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name="home"),
    path('book.htm',views.book,name="book"),
    path('student.htm',views.student,name="student"),
    path('emp.htm',views.emp,name="emp"),
]