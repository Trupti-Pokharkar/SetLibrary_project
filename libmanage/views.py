from django.shortcuts import render,redirect
from .models import Library , Student , Emp
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def home(request):
    return render(request,"home.htm")

def book(request):
    librarys = Library.objects.all()

    if request.method =="POST":
        if "add" in request.POST:
            name = request.POST.get("name")
            author= request.POST.get("author")
            publisher= request.POST.get("publisher")
            publication= request.POST.get("publication")
            pages= request.POST.get("pages")
            price= request.POST.get("price")
            Library.objects.create(
               name=name,
               author=author,
               publisher=publisher,
               publication=publication,
               pages=pages,
               price=price
            )
            messages.success(request,"Book added successfully")

        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            author= request.POST.get("author")
            publisher= request.POST.get("publisher")
            publication= request.POST.get("publication")
            pages= request.POST.get("pages")
            price= request.POST.get("price")
            update_book= Library.objects.get(id=id)
            update_book.name = name
            update_book.author = author
            update_book.publisher = publisher
            update_book.publication = publication
            update_book.pages = pages
            update_book.price = price
                
            update_book.save()

            messages.success(request,"Book Updated successfully")

        elif "delete" in request.POST:
            id= request.POST.get("id")
            Library.objects.get(id=id).delete()
            messages.success(request,"student Deleted succesfully")

        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            librarys = Library.objects.filter(Q(name__icontains=query) |  Q(author__icontains=query)|Q(publisher__icontains=query)|Q(publication__icontains=query)|Q(pages__icontains=query)|Q(price__icontains=query))


    context={"librarys":librarys}
    return render(request,"book.htm",context=context)

def student(request):
    students = Student.objects.all()

    if request.method =="POST":
        if "add" in request.POST:
            stuid= request.POST.get("stuid")
            name= request.POST.get("name")
            book= request.POST.get("book")
            date= request.POST.get("date")
            rdate= request.POST.get("rdate")
            Student.objects.create(
               stuid=stuid,
               name=name,
               book=book,
               date=date,
               rdate=rdate,
            )
            messages.success(request,"Student added successfully")

        elif "update" in request.POST:
            id = request.POST.get("id")
            stuid = request.POST.get("stuid")
            name= request.POST.get("name")
            book= request.POST.get("book")
            date= request.POST.get("date")
            rdate= request.POST.get("rdate")
            update_student = Student.objects.get(id=id)
            update_student.stuid = stuid
            update_student.name = name
            update_student.book = book
            update_student.date= date
            update_student.rdate =rdate
                
            update_student.save()

            messages.success(request,"student Updated successfully")

        elif "delete" in request.POST:
            id= request.POST.get("id")
            Student.objects.get(id=id).delete()
            messages.success(request,"student Deleted succesfully")

        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            students = Student.objects.filter(Q(stuid__icontains=query) |  Q(name__icontains=query)|Q(book__icontains=query)|Q(date__icontains=query)|Q(rdate__icontains=query))

    context={"students":students}
    return render(request,"student.htm",context=context)

def emp(request):
    emps=Emp.objects.all()

    if request.method =="POST":
        if "add" in request.POST:
            empid= request.POST.get("empid")
            name= request.POST.get("name")
            email= request.POST.get("email")
            Mob= request.POST.get("Mob")
            pos= request.POST.get("pos")
            Emp.objects.create(
               empid=empid,
               name=name,
               email=email,
               Mob=Mob,
               pos=pos,
            )
            messages.success(request,"Employee added successfully")

        elif "update" in request.POST:
            id = request.POST.get("id")
            empid= request.POST.get("empid")
            name= request.POST.get("name")
            email= request.POST.get("email")
            Mob= request.POST.get("Mob")
            pos= request.POST.get("pos")
            update_emps = Emp.objects.get(id=id)
            update_emps.empid = empid
            update_emps.name = name
            update_emps.email= email
            update_emps.Mob= Mob
            update_emps.pos =pos
                
            update_emps.save()
            messages.success(request,"Employee Updated successfully")

        elif "delete" in request.POST:
            id= request.POST.get("id")
            Emp.objects.get(id=id).delete()
            messages.success(request,"student Deleted succesfully")

        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            emps = Emp.objects.filter(Q(empid__icontains=query) |  Q(name__icontains=query)|Q(email__icontains=query)|Q(Mob__icontains=query)|Q(pos__icontains=query))

    context={"emps":emps}
    return render(request,"emp.htm",context=context)

