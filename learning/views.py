from django.shortcuts import render ,get_object_or_404 , redirect 
from rest_framework import generics , permissions
# Create your views here.
from .models import  HomeNav,CustomUser
from .serializers import  NavSerializer
import requests
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
# def homepage(request):
#     nav_url = f"http://127.0.0.1:8000/api/getnav/"
#     nav_response = requests.get(nav_url)
#     nav_items = HomeNav.objects.filter(parent_category=None)
#     return render(request,'homepage.html',{'nav_items':nav_items})

 
def homepage(request):
    nav_url = f"http://127.0.0.1:8000/api/getnav/"
    nav_response = requests.get(nav_url)
    nav_items = HomeNav.objects.filter(parent_category=None).order_by('id')
    crlimg=carousel_img.objects.all()
    card=carditems.objects.all()
    diver=content_image.objects.all()

    kl=footer_content.objects.all()
    links = FooterLink.objects.all()
    services = FooterService.objects.all()
    contact_info = ContactInfo.objects.first()
    social = SocialLink.objects.all()
    # homehero = hero.objects.all()



    return render(request,'homepage.html',{'kl':kl,'links':links,'services':services,'contact_info':contact_info,'social':social,'nav_items':nav_items,'nav_response':nav_response,'crlimg':crlimg,'card':card,'services': services})


def navheader(request):
    nav_items = HomeNav.objects.filter(parent_category=None)
    return render(request, 'navheader.html', {'nav_items':nav_items})
 
    
    
def carousel_home(request):
    if request.method=="GET":
        b=carousel_img.objects.all()
        return render(request,"carousel_home.html",{'b':b})

def carousel_insert(request):
    if request.method=="POST":
        image=request.FILES.get('image')
        c=carousel_img(image=image)
        c.save()
        return HttpResponse("image is inserted")
    return render(request,"crl_img.html")
    
def card_insert(request):
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['content']
        image=request.FILES.get('image')
        cd=carditems(title=title,content=content,image=image)
        cd.save()
        return HttpResponse("your card is inserted")
    return render(request,"card_insert.html")
    
def content_image_insert(request):
    if request.method=="POST":
        title1=request.POST['title1']
        content1=request.POST['content1']
        image1=request.FILES.get('image1')
        title2=request.POST['title2']
        content2=request.POST['content2']
        image2=request.FILES.get('image2')
        title3=request.POST['title3']
        content3=request.POST['content3']
        image3=request.FILES.get('image3')
        title4=request.POST['title4']
        content4=request.POST['content4']
        image4=request.FILES.get('image4')
        cnt=content_image(title1=title1,content1=content1,image1=image1,title2=title2,content2=content2,image2=image2,title3=title3,content3=content3,image3=image3,title4=title4,content4=content4,image4=image4)
        cnt.save()
        return HttpResponse("your card is inserted")
    return render(request,"content_image_insert.html")


class NavListView(generics.ListAPIView):
    queryset = HomeNav.objects.filter(parent_category=None)
    serializer_class = NavSerializer
    http_method_names = ['get']

class NavCreateView(generics.CreateAPIView):
    queryset = HomeNav.objects.all()
    serializer_class = NavSerializer
    http_method_names = ['post']

from .forms import NavForm
def create_nav(request):
    form = NavForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = NavForm()
    return render(request, "create_nav.html",{'form':form})

def homenavbarinsert(request):
    k=HomeNav.objects.all()
    if request.method=="POST":
        nav_name=request.POST.get('nav_name')
        nav_url = request.POST.get('nav_url')
        parent_category=request.POST.get('parent_category')
        

        p=HomeNav(nav_name=nav_name,nav_url=nav_url,parent_category_id=parent_category)
        p.save()

        return HttpResponse("inserted successfully")
          
    return render(request,"homenavbarinsert.html",{'k':k})



from django.shortcuts import render,redirect
from rest_framework import generics
from .models import Schools,MenuItem
from .serializers import StudentFormSerializer
import requests
from django.http import HttpResponse,HttpResponseRedirect
import json
from .serialization import updateserializationclass
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User 
from django.contrib.auth.hashers import check_password

from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import CustomUser
from django.contrib.auth.decorators import login_required


# def adminA(request):
#     p=logo.objects.all()
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         try:
#             user = CustomUser.objects.get(username=username)
#         except CustomUser.DoesNotExist:
#             error_message = "Invalid login credentials. Please try again."
#             return render(request, "login.html", {'error_message': error_message,'p':p})
        
#         if check_password(password, user.password):
#             return redirect('/new_home1')
#         else:
#             error_message = "Invalid login credentials. Please try again."
#             return render(request, "login.html", {'error_message': error_message,'p':p})

#     return render(request, "login.html",{"p":p})

def new_home1(request):
    admin=admindrop.objects.all()
    username = request.user.username
    return render(request,"hom4.html", {"username": username,"admin":admin})

def adminB(request):
    return render(request, "adminlogin.html")

from django.contrib.auth.forms import PasswordResetForm  
from django.urls import reverse
from django.contrib import messages
from learning.EmailBackEnd import EmailBackEnd

from django.contrib.auth import login as auth_login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from .models import OAuthCredentials

from django.contrib.auth import login as auth_login
from django.urls import reverse

def doLogin(request):
    if request.method != "POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password=request.POST.get("password"))
        if user is not None:
            auth_login(request, user)
            # Check user type and redirect accordingly
            if user.user_type == "1":
                redirect_url = '/sidenavbar'
            elif user.user_type == "2":
                redirect_url = '/teacher_sidebar'
            elif user.user_type == "3":
                user.save_login_record()
                redirect_url = '/student_sidebar'
            elif user.user_type == "0":
                redirect_url = '/new_home1'
            else:
                redirect_url = reverse("Employ_home")
                
            # Retrieve OAuth credentials associated with the logged-in user
            try:
                oauth_credentials = OAuthCredentials.objects.get(user=user)
                request.session['credentials'] = {
                    'token': oauth_credentials.token,
                    'refresh_token': oauth_credentials.refresh_token,
                    'token_uri': oauth_credentials.token_uri,
                    'client_id': oauth_credentials.client_id,
                    'client_secret': oauth_credentials.client_secret
                }
            except OAuthCredentials.DoesNotExist:
                # Clear any existing credentials from the session
                request.session.pop('credentials', None)

            return HttpResponseRedirect(redirect_url)
        else:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect("/adminB")


def logout1(request):

    if request.user.user_type == "3" :
        request.user.save_logout_record() 
    logout(request)
    return HttpResponseRedirect("/adminB")



def attendance_stu(request):
    all=Schools.objects.filter(usernumber=request.user.id).first() 

    k=MenuItem.objects.filter(parent_category=None)
    cl=cls_name.objects.filter(school_id=all)
    return render(request,"attend.html",{'k':k,'cl':cl})

from django.shortcuts import render
from django.utils import timezone
from .models import Student, EmployeeLoginLogout
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Class, CustomUser, EmployeeLoginLogout
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Class, CustomUser, EmployeeLoginLogout
from datetime import datetime

from collections import defaultdict
from datetime import datetime

from datetime import datetime, timedelta
from collections import defaultdict

from datetime import timedelta

from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import datetime
from .models import CustomUser, cls_name, EmployeeLoginLogout

def class_students(request, class_id):
    k = MenuItem.objects.filter(parent_category=None)
    selected_class = get_object_or_404(cls_name, id=class_id)
    today = timezone.now().date()
    students = Student.objects.filter(className=selected_class)
    if not students:
        return HttpResponse("No students are in this class.")
    student_data = []

    for student in students:
        first_login = EmployeeLoginLogout.objects.filter(employee=student.mystudent, login_time__date=today).first()

        if student.shift:
            shift_end_time = datetime.combine(today, student.shift.end_time)
            last_logout = EmployeeLoginLogout.objects.filter(
                employee=student.mystudent, 
                logout_time__date=today, 
                logout_time__lt=shift_end_time
            ).order_by('-logout_time').first()

            shift_start_datetime = datetime.combine(today, student.shift.start_time)
            shift_end_datetime = shift_end_time

            # Check if shift has ended
            shift_ended = timezone.now() >= shift_end_datetime
        else:
            last_logout = None
            shift_start_datetime = None
            shift_end_datetime = None
            shift_ended = False

        login_logout_entries = EmployeeLoginLogout.objects.filter(employee=student.mystudent, login_time__date=today)

        # Include first_login entry if it exists
        if first_login:
            login_logout_entries |= EmployeeLoginLogout.objects.filter(pk=first_login.pk)

        total_shift_duration = (shift_end_datetime - shift_start_datetime).total_seconds() / 3600 if shift_start_datetime and shift_end_datetime else 0  # Total shift duration in hours
        total_shift_duration_minutes = int(total_shift_duration * 60)  # Convert hours to minutes

        total_worked_duration = 0
        total_entry_percentage = 0

        for entry in login_logout_entries:
            if entry.logout_time and shift_start_datetime and shift_end_datetime and shift_start_datetime <= entry.login_time <= shift_end_datetime and shift_start_datetime <= entry.logout_time <= shift_end_datetime:
                duration_seconds = (entry.logout_time - entry.login_time).total_seconds()
                entry_duration_hours = duration_seconds / 3600
                total_worked_duration += entry_duration_hours

                # Calculate entry percentage (ensure total_shift_duration is not zero)
                entry_percentage = (entry_duration_hours / total_shift_duration) * 100 if total_shift_duration > 0 else 0
                entry.percentage = round(entry_percentage, 2)  # Round to two decimal places
                total_entry_percentage += entry.percentage

            else:
                entry.percentage = 0  

        if total_entry_percentage > 100:
            last_entry = login_logout_entries.last()
            total_entry_percentage += entry_percentage

        total_percentage = min(total_entry_percentage, 100)

        if shift_ended:
            if total_entry_percentage < 50:
                status = "Absent"
            elif total_entry_percentage < 60:
                status = "Half Day"
            else:
                status = "Full Day"
        else:
            status = "Shift in Progress"

        student_data.append({
            'student': student,
            'first_login': first_login,
            'last_logout': last_logout,  # Display None if no last_logout
            'login_logout_entries': login_logout_entries,
            'total_shift_duration_minutes': total_shift_duration_minutes,
            'total_worked_duration': total_worked_duration,
            'total_percentage': min(total_entry_percentage, 100),  # Limit total percentage to 100
            'shift_ended': shift_ended,
            'status': status,
        })

    class_names = cls_name.objects.all()

    # Ensure the rendering does not fail if a student lacks a shift
    if any(student.shift for student in students):
        shift_end_time = max((datetime.combine(today, student.shift.end_time) for student in students if student.shift), default=None)
    else:
        shift_end_time = None

    return render(request, "class_students.html", {'selected_class': selected_class, 'student_data': student_data, 'class_names': class_names, 'k': k, 'shift_end_time': shift_end_time})

from django.contrib.auth.tokens import default_token_generator

from django.contrib.auth import update_session_auth_hash
def password(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = CustomUser.objects.get(username=username)

        if new_password != confirm_password:
            error_message = 'New passwords do not match.'
            return render(request, 'reset_password.html', {'error_message': error_message})
        

        user.set_password(new_password)
        user.save()

        update_session_auth_hash(request, user)  

        
        success_message = 'Password changed successfully!'
        return render(request, 'reset_password.html', {'success_message': success_message})


        

    return render(request, 'reset_password.html')

class StudentFormListCreateView(generics.ListCreateAPIView):
    queryset = Schools.objects.all()
    serializer_class = StudentFormSerializer

class actionapi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Schools.objects.all()
    serializer_class=updateserializationclass
    template_name="action.html"



def new_home(request):
        return render(request, 'home1_content.html')

import requests
from django.shortcuts import render, HttpResponse, redirect
from .models import CustomUser, Schools, plans, plans1, plans2

from django.http import HttpResponse
from django.shortcuts import render
from .models import PricingPlan

from django.shortcuts import render
from django.http import HttpResponse
from .models import PricingPlan, CustomUser, Schools

def regform(request, plan_id):
    try:
        plan = PricingPlan.objects.get(pk=plan_id)
    except PricingPlan.DoesNotExist:
        return HttpResponse('Invalid plan ID')

    if request.method == "POST":
        organizationname = request.POST.get('organizationname')
        registrationno = request.POST.get('registrationno')
        address = request.POST.get('address')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        image1 = request.FILES.get('image1')
        phoneno = request.POST.get('phoneno')
        strength = request.POST.get('strength')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            user = CustomUser(username=username, email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()

        data = Schools.objects.create(
            organizationname=organizationname,
            registrationno=registrationno,
            address=address,
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            image1=image1,
            phoneno=phoneno,
            strength=strength,
            password=password,
            confirm_password=confirm_password,
            usernumber=user,
            plan_id=plan,  # Save the selected plan object
        )
        data.save()
       
        return HttpResponse('Registered Successfully..!!')

    if plan.name in ['Basic', 'Premium', 'Advanced ']:
        return render(request, 'new.html', {'plan': plan})
    else:
        return HttpResponse('Invalid plan type')



from django.shortcuts import render, get_object_or_404

def view_profile(request, organization_id):
    admin=admindrop.objects.all()
    
    organization_profile = get_object_or_404(Schools, id=organization_id)

    context = {'organization_profile': organization_profile,'admin':admin}
    return render(request, 'view_profile_template.html', context)



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
import requests

def retrieve(request):
    admin=admindrop.objects.all()
    
    page = request.GET.get('page', 1)


    api_url = 'http://127.0.0.1:8000/student-form/'


    # Fetch data from the API
    response = requests.get(api_url)
    data = response.json()

    # Assuming 'items_per_page' is the number of items you want to display per page
    items_per_page = 3
    paginator = Paginator(data, items_per_page)

    try:
        res = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        res = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver last page of results.
        res = paginator.page(paginator.num_pages)

    return render(request, "retrirvedata.html", {'res': res,"admin":admin})




def action(request):
    cl=requests.get('http://127.0.0.1:8000/student-form/')
    res=cl.json()
    return render(request,"action.html",{'res':res})

def edit(request,id):
   if request.method=="GET":
        e=Schools.objects.get(id=id)
   return render(request,"action.html",{'e':e})

def update(request,id):
     if request.method=="POST":
        organizationname = request.POST.get('organizationname')
        registrationno = request.POST.get('registrationno')
        address = request.POST.get('address')
        hod = request.POST.get('hod')
        email = request.POST.get('email')
        image1 = request.FILES.get('image1')
        phoneno = request.POST.get('phoneno')
        strength = request.POST.get('strength')
        a=Schools.object.get(id=id)
        a.organizationname=organizationname
        a.registrationno=registrationno
        a.address=address
        a.hod=hod
        a.email=email
        a.image1=image1
        a.phoneno=phoneno
        a.strength=strength
        a.save()
        return redirect("/retrirve/")
     return render(request,"action.html")

def Employ_home(request):
    k=MenuItem.objects.filter(parent_category=None)
    return render(request,'adminsidebar.html',{'k':k})



from django.shortcuts import render, redirect
from .models import Student, CustomUser
from django.contrib.auth.hashers import make_password


def studentregform(request):
    shifts=shift_names.objects.all()
    k=MenuItem.objects.filter(parent_category=None)
    sch = Schools.objects.filter(usernumber=request.user.id).first()
    classes = cls_name.objects.filter(school_id=sch)
    message = ''

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        shift_name=request.POST.get('shift')
        confirm_password = request.POST.get('confirm_password')
        registration_date = request.POST.get('registration_date')
        className = request.POST.get('className')
        gender = request.POST.get('gender')
        mobile_number = request.POST.get('mobile_number')
        parents_name = request.POST.get('parents_name')
        parents_mobile_number = request.POST.get('parents_mobile_number')
        date_of_birth = request.POST.get('date_of_birth')
        address = request.POST.get('address')
        username = request.POST.get('username')

        shift_instance=get_object_or_404(shift_names,name=shift_name)
        user=CustomUser.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,user_type=3,shift=shift_instance)

        user.save()

        mystudent=CustomUser.objects.get(id=user.id)
        sch=Schools.objects.filter(usernumber=request.user.id).first()
        classes_instance=cls_name.objects.get(id=className)

        student = Student(
            first_name=first_name,
            last_name=last_name,
            email=email,
            shift=shift_instance,
            password=password,
            confirm_password=confirm_password,
            registration_date=registration_date,
            className=classes_instance,
            gender=gender,
            mobile_number=mobile_number,
            parents_name=parents_name,
            parents_mobile_number=parents_mobile_number,
            date_of_birth=date_of_birth,
            address=address,
            mystudent=mystudent,
            username=username,
            schoolid=sch,
        )
        student.save()
        message = 'Student added successfully.'
        
        

    return render(request, 'studentreg.html',{'k':k,'classes':classes,'message':message,'shifts':shifts})


# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
# from .models import Teachers, ZoomMeeting

# from datetime import datetime, timedelta

# @login_required
# def teacher_dashboard(request):
#     teacher = Teachers.objects.get(admin=request.user)
#     now_utc = datetime.now(timezone.utc)
#     upcoming_meetings = ZoomMeeting.objects.filter(
#         Teacher_name_id=teacher.id, meeting_date__gte=now_utc
#     ).select_related('class_name', 'subject_name')  

#     completed_meetings = ZoomMeeting.objects.filter(
#         Teacher_name_id=teacher.id, endtime__lt=now_utc
#     ).select_related('class_name', 'subject_name')

#     for meeting in upcoming_meetings:
#         meeting.endtime = datetime.combine(meeting.meeting_date, meeting.endtime)

#     context = {'teacher': teacher, 'upcoming_meetings': upcoming_meetings, 'completed_meetings': completed_meetings}
#     return render(request, 'teacher_dashboard.html', context)


from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone  # Correct import for timezone
from .models import Teachers, ZoomMeeting
from datetime import datetime, timedelta

@login_required
def teacher_dashboard(request):
    teacher = Teachers.objects.get(admin=request.user)
    now_utc = timezone.now()  # Use timezone.now() to get the current time in UTC
    upcoming_meetings = ZoomMeeting.objects.filter(
        Teacher_name_id=teacher.id, meeting_date__gte=now_utc
    ).select_related('class_name', 'subject_name')

    completed_meetings = ZoomMeeting.objects.filter(
        Teacher_name_id=teacher.id, endtime__lt=now_utc
    ).select_related('class_name', 'subject_name')

    for meeting in upcoming_meetings:
        meeting.endtime = datetime.combine(meeting.meeting_date, meeting.endtime)

    context = {'teacher': teacher, 'upcoming_meetings': upcoming_meetings, 'completed_meetings': completed_meetings}
    return render(request, 'teacher_dashboard.html', context)



# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
# from .models import Student, ZoomMeeting
# @login_required
# def student_dashboard(request):
#     student = Student.objects.get(mystudent=request.user) 
 

#     from datetime import datetime, timezone
#     now_utc = datetime.now(timezone.utc)  

#     upcoming_meetings = ZoomMeeting.objects.filter(
#         class_name_id=student.className.id,
#         meeting_date__gte=now_utc  
#     ).select_related('class_name','subject_name')

#     context = {
#         'student': student,
#         'upcoming_meetings': upcoming_meetings,
       
#     }
#     return render(request, 'student_dashboard.html', context)



@login_required
def student_dashboard(request):
    student = get_object_or_404(Student, mystudent=request.user)
    now_utc = timezone.now()

    try:
        if hasattr(student, 'className') and student.className is not None:
            class_name_id = student.className.id
            upcoming_meetings = ZoomMeeting.objects.filter(
                class_name_id=class_name_id,
                meeting_date__gte=now_utc
            ).select_related('class_name', 'subject_name')
        else:
            upcoming_meetings = []
    except cls_name.DoesNotExist:
        upcoming_meetings = []

    context = {
        'student': student,
        'upcoming_meetings': upcoming_meetings,
    }
    return render(request, 'student_dashboard.html', context)




from django.shortcuts import render
from .models import Student

def allstudents(request):
    
    students = Student.objects.filter()
    context = {'students': students}
    return render(request, 'allstudents.html', context)


from django.shortcuts import render,redirect
from .models import lms
from .serialization import stdserializationclass
from django.http import HttpResponse,FileResponse
# Create your views here.
def reg(request):
    if request.method=="POST":
        image1=request.FILES.get('image1')
        image2=request.FILES.get('image2')
        image3=request.FILES.get('image3')
        image4=request.FILES.get('image4')
        image5=request.FILES.get('image5')
        k=lms(image1=image1,image2=image2,image3=image3,image4=image4,image5=image5)
        k.save()
        return HttpResponse("image added")
    return render(request,"reg1.html")

def data(request):
    if request.method=="GET":
        k=lms.objects.all()
    return render(request,"display1.html",{'k':k})

def home(request):
    if request.method=="GET":
        k=lms.objects.all()
    return render(request,"display.html",{'k':k})

def edit(request,id):
    k1=lms.objects.get(id=id)
    return render(request,"up.html",{'k1':k1})

def update(request,id):
    if request.method=="POST":
        image1=request.FILES.get('image1')
        image2=request.FILES.get('image2')
        image3=request.FILES.get('image3')
        image4=request.FILES.get('image4')
        image5=request.FILES.get('image5')
        k=lms.objects.get(id=id)
        k.image1=image1
        k.image2=image2
        k.image3=image3
        k.image4=image4
        k.image5=image5
        k.save()
        return redirect("/data")
    return render(request,"up.html")

def delete(request,id):
    d=lms.objects.get(id=id)
    d.delete()
    return redirect("/data")


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Course, Subject
from .forms import  CourseForm, SubjectForm
from .models import *
from .forms import *

def register(request):
    k=Course.objects.all()
    k1=Subject.objects.all()
    if request.method == "POST":
        organizationname = request.POST.get('organizationname')
        registrationno = request.POST.get('registrationno')
        address = request.POST.get('address')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        designation  = request.POST.get('designation')
        department  = request.POST.get('department')
        dob  = request.POST.get('dob')
        experiance = request.POST.get('experiance')
        gender = request.POST.get('gender')
        qualification  = request.POST.get('qualification')
       
        email = request.POST.get('email')
        image1 = request.FILES.get('image1')
        phoneno = request.POST.get('phoneno')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')


        
        data=Teachers.objects.create(
            organizationname= organizationname,
            registrationno= registrationno,
            address= address,
            first_name= first_name,
            last_name= last_name,
            username=username,
            designation=designation,
            department=department,
            dob=dob,
            qualification=qualification,
            
            image1=image1,
            email= email,
            experiance=experiance,
            phoneno= phoneno,
            gender=gender,
            password=password,
            confirm_password=confirm_password,
            
            
        )
        data.save()
        user=CustomUser.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,user_type=2)
        user.save()
       
        
        # user.save()
        
        
        
        return HttpResponse('Registered Successfully..!!')
  
    return render(request, 'teacher_register.html',{'k':k,'k1':k1})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import MenuItem, Schools, Teachers


def teacher_read(request):
    # Filter top-level menu items
    k = MenuItem.objects.filter(parent_category=None)

    # Get the school associated with the logged-in user
    school = Schools.objects.filter(usernumber=request.user.id).first()

    # Filter teachers based on the school
    data1 = Teachers.objects.filter(schoolid=school)

    return render(request, 'teacher_read.html', {'k': k, 'data1': data1})


def edit_teacher(request,id):
   k=Course.objects.all()
   k1=Subject.objects.all()
   dataget = Teachers.objects.get(id=id)
   data = Teachers.objects.all()
        
   if request.method == 'POST':

            organizationname = request.POST.get('organizationname')
            registrationno = request.POST.get('registrationno')
            address = request.POST.get('address')
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            designation  = request.POST.get('designation')
            department  = request.POST.get('department')
            dob  = request.POST.get('dob')
            gender = request.POST.get('gender')
            experiance = request.POST.get('experiance')
            qualification  = request.POST.get('qualification')
            subject1  = request.POST.get('subject1')
            course1  = request.POST.get('course1')
            email = request.POST.get('email')
            image1 = request.FILES.get('image1')
            phoneno = request.POST.get('phoneno')
            password=request.POST.get('password')
            confirm_password=request.POST.get('confirm_password')


        
            dataget.organizationname = organizationname
            dataget.registrationno = registrationno
            dataget.address = address
            dataget.username = username
            dataget.first_name = first_name
            dataget.last_name = last_name 
            dataget.email = email
            dataget.image1 = image1
            dataget.phoneno = phoneno
            dataget.department = department 
            dataget.designation = designation
            dataget.dob = dob
            dataget.gender = gender
            dataget.experiance = experiance
            dataget.qualification = qualification
            dataget.course1 = course1
            dataget.subject1 = subject1
            dataget.password = password
            dataget.confirm_password = confirm_password
            dataget.save()

            return redirect('teacher_read')  
        
   return render(request, 'edit_teacher_template.html', {'k':k,'k1':k1,'dataget':dataget,'data':data})
        

def teacher_delete(request,id):
    data = Teachers.objects.get(id=id)
    data.delete()
    return redirect('teacher_read')   



@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_course')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})


def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_subject')
    else:
        form = SubjectForm()
    return render(request, 'add_subject.html', {'form': form})


# from .models import teachersidebar
# def teacherside(request):
#     k1=teachersidebar.objects.filter(parent_category=None)
#     return render(request,'teacher_sidebar.html',{'k1':k1})


from .models import UploadedFile
from .forms import UploadFileForm

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_file')
    else:
        form = UploadFileForm()
    files = UploadedFile.objects.all()
    return render(request, 'upload_file.html', {'form': form, 'files': files})




def download_file(request, id):
    error_message = "Invalid login credentials. Please try again."

    if request.method=='POST':
          
            try:
                 
               user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
               if user != None:

                  login(request,user)
                  if user.user_type=="1":
                      uploaded_file = UploadedFile.objects.get(id=id)
                      response = HttpResponse(uploaded_file.file, content_type='application/force-download')
                      response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
                      return response




            except CustomUser.DoesNotExist:
                 error_message = "Invalid login credentials. Please try again."
                 return redirect('/upload_2')


    return render(request, "upload_file.html", {'error_message': error_message})



def upload_2(request,id):
    files = UploadedFile.objects.filter(id=id)
    return render(request, 'upload2.html', { 'files': files})

def subjectnames(request):
    files1 = UploadedFile.objects.filter(parent_category__isnull=True)
    return render(request, 'sub_topics.html', { 'files1': files1})

def chapters(request,subject_id):
    files2=UploadedFile.objects.get(pk=subject_id)
    subchapters=files2.subdrop.all()
    return render(request,'chapters.html',{'files2':files2,'subchapters':subchapters})


def logout_view(request):
    logout(request)
    return redirect("/adminB")


# def regform1(request):
#     if request.method == "POST":
#         subjects = request.POST.get('subjects')
#         intro = request.POST.get('intro')
#         description = request.POST.get('description')
#         subid = request.POST.get('subid')
#         chaptername = request.POST.get('chaptername')
#         chapterdis=request.POST.get('chapterdis')
#         subjecttitle=request.POST.get('subjecttitle')
#         subject_description=request.POST.get('subject_description')
#         stdclass.objects.create(
#             subjects=subjects,
#             intro =intro ,
#             description=description,
#             subid =subid ,
#             chaptername=chaptername,
#             chapterdis=chapterdis,
#             subjecttitle=subjecttitle,
#             subject_description=subject_description,
#         )
#         return HttpResponse("inserted successfully")
#     return render(request, "insert_subjects.html")





# def home1(request):
#     if request.method=="GET":
#         n=stdclass.objects.all()
#         return render(request,"display3.html",{'n':n})

# def subject(request, subid):
#     if request.method == "GET":
#         res = stdclass.objects.filter(subid=subid)
#         return render(request, "subject.html", {'res': res})
        
# def chapter(request, id,subid):
#     if request.method == "GET":
#         res1 = stdclass.objects.filter(id=id)
#         n= stdclass.objects.filter(subid=subid)
#         return render(request, "chapter.html", {'res1': res1,'n':n})
    

from .models import  HomeNav,topics

def reg1(request):
    if request.method=="GET":
        priv=topics.objects.all()
        return render(request,"data.html",{'priv':priv})
def display2(request):
     if request.method=="GET":
        pri=topics.objects.all()
        return render(request,"display2.html",{'pri':pri})

def inserted(request):
     if request.method=="POST":
          title=request.POST['title']
          subtitle=request.POST['subtitle']
          content=request.POST['content']
          subject1=request.POST['subject1']
          subject2=request.POST['subject2']
          subject3=request.POST['subject3']
          subject4=request.POST['subject4']
          subject5=request.POST['subject5']
          subject6=request.POST['subject6']
          subject7=request.POST['subject7']
          subject8=request.POST['subject8']
          subject9=request.POST['subject9']
          subject10=request.POST['subject10']
          subject11=request.POST['subject11']
          subject12=request.POST['subject12']
          subject13=request.POST['subject13']
          subject14=request.POST['subject14']
          subject15=request.POST['subject15']
          p=topics(title=title,subtitle=subtitle,content=content,subject1=subject1,subject2=subject2,subject3=subject3,subject4=subject4,subject5=subject5,subject6=subject6,subject7=subject7,subject8=subject8,subject9=subject9,subject10=subject10,subject11=subject11,subject12=subject12,subject13=subject13,subject14=subject14,subject15=subject15)
          p.save()
          
          return redirect ("/reg1/")
     return render(request,"datainserted.html")
def edit(request,id):
    if request.method=="GET":
        pri1=topics.objects.get(id=id)
        return render(request,"update.html",{'pri1':pri1})
def update(request,id):
    if request.method=="POST":
        title=request.POST['title']
        subtitle=request.POST['subtitle']
        content=request.POST['content']
        subject1=request.POST['subject1']
        subject2=request.POST['subject2']
        subject3=request.POST['subject3']
        subject4=request.POST['subject4']
        subject5=request.POST['subject5']
        subject6=request.POST['subject6']
        subject7=request.POST['subject7']
        subject8=request.POST['subject8'] 
        subject9=request.POST['subject9'] 
        subject10=request.POST['subject10'] 
        subject11=request.POST['subject11']
        subject12=request.POST['subject12']
        subject13=request.POST['subject13']
        subject14=request.POST['subject14']
        subject15=request.POST['subject15']
        k=topics.objects.get(id=id) 
        k.title=title
        k.subtitle=subtitle
        k.content=content
        k.subject1=subject1
        k.subject2=subject2
        k.subject3=subject3
        k.subject4=subject4
        k.subject5=subject5
        k.subject6=subject6
        k.subject7=subject7
        k.subject8=subject8
        k.subject9=subject9
        k.subject10=subject10 
        k.subject11=subject11
        k.subject12=subject12
        k.subject13=subject13
        k.subject14=subject14
        k.subject15=subject15
        k.save()
        return redirect("/reg1/")
    return render(request,"update.html")

def delete(request,id):
        k=topics.objects.get(id=id)
        k.delete()
        return redirect("/reg1/") 

def class12(request):
    pri=topics.objects.filter(subtitle__endswith="12")
    return render(request,"display2.html",{'pri':pri})

def class11(request):
    pri=topics.objects.filter(subtitle__endswith="11")
    return render(request,"display2.html",{'pri':pri})

def class10(request):
    pri=topics.objects.filter(subtitle__endswith="10")
    return render(request,"display2.html",{'pri':pri})

def class9(request):
    pri=topics.objects.filter(subtitle__endswith="9")
    return render(request,"display2.html",{'pri':pri})

def class8(request):
    pri=topics.objects.filter(subtitle__endswith="8")
    return render(request,"display2.html",{'pri':pri})

def class7(request):
    pri=topics.objects.filter(subtitle__endswith="7")
    return render(request,"display2.html",{'pri':pri})

def class6(request):
    pri=topics.objects.filter(subtitle__endswith="6")
    return render(request,"display2.html",{'pri':pri})
    
def class5(request):
    pri=topics.objects.filter(subtitle__endswith="5")
    return render(request,"display2.html",{'pri':pri})

def class4(request):
    pri=topics.objects.filter(subtitle__endswith="4")
    return render(request,"display2.html",{'pri':pri})

def class3(request):
    pri=topics.objects.filter(subtitle__endswith="3")
    return render(request,"display2.html",{'pri':pri})

def class2(request):
    pri=topics.objects.filter(subtitle__endswith="2")
    return render(request,"display2.html",{'pri':pri})

def class1(request):
    pri=topics.objects.filter(subtitle__endswith="1")
    return render(request,"display2.html",{'pri':pri})

# from django.shortcuts import get_object_or_404, render
# from .models import stdclass1
# from django.http import FileResponse, HttpResponse
# # Create your views here.

# def regform_sub(request):
#     if request.method == "POST":
#         subjects = request.POST.get('subjects')
#         intro = request.POST.get('intro')
#         description = request.POST.get('description')
#         subid = request.POST.get('subid')
#         chaptername = request.POST.get('chaptername')
#         chapterdis=request.POST.get('chapterdis')
#         pdf=request.FILES.get('pdf')
#         classes=request.POST.get('classes')
#         classid=request.POST.get('classid')
#         stdclass1.objects.create(
#             subjects=subjects,
#             intro =intro ,
#             description=description,
#             subid =subid ,
#             chaptername=chaptername,
#             chapterdis=chapterdis,
#             pdf=pdf,
#             classes=classes,
#             classid=classid
#         )
#         return HttpResponse("inserted successfully")
#     return render(request, "insert_sub.html")

# def home_sub(request):
#     if request.method=="GET":
#         n=stdclass1.objects.all()
#         return render(request,"display_sub.html",{'n':n})
# def sub1(request, classid):
#     if request.method == "GET":
#         res = stdclass1.objects.filter(classid=classid)
#         return render(request, "sub.html", {'res': res})

# def subjects1(request, subid):
#     if request.method == "GET":
#         res = stdclass1.objects.filter(subid=subid)
#         return render(request, "subjects1.html", {'res': res})
      
# def chapter1(request,id,subid,classid):
    
#     error_message = "Invalid login credentials. Please try again."
    
#     if request.method=='POST':
          
#             try:
                 
#                user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
#                if user != None:

#                   login(request,user)
#                   if user.user_type=="1":
#                       uploaded_file = stdclass1.objects.get(id=id)
#                       response = HttpResponse(uploaded_file.pdf, content_type='application/force-download')
#                       response['Content-Disposition'] = f'attachment; filename="{uploaded_file.pdf.name}"'
#                       return response
#             except CustomUser.DoesNotExist:
#                  error_message = "Invalid login credentials. Please try again."
#                  return redirect('/upload_3')

#     # return render(request, 'upload3.html', { 'files': files,'error_message': error_message})
#     res1 = stdclass1.objects.filter(id=id)
#     n= stdclass1.objects.filter(subid=subid)
#     z=stdclass1.objects.filter(classid=classid)
#     m=stdclass1.objects.all()
#     return render(request, "chapter1.html", {'res1': res1,'n':n,'m':m,'z':z,'error_message':error_message})
    
# def serve_pdf(request, document_id):
#     document = get_object_or_404(stdclass1, pk=document_id)
#     response = FileResponse(open(document.pdf.path, 'rb'), content_type='application/pdf')
#     return response



from django.shortcuts import render
from django.views import View
from .models import t_table
from datetime import datetime, timedelta, timezone


class TimeTableView(View):
    template_name = 'time_table.html'

    def get(self, request):
        time_table_data = t_table.objects.all()

        start_end = self.generate_intervals(time_table_data)

        return render(request, self.template_name, {'start_end': start_end})

    def generate_intervals(self, time_table_data):
        start_end=[]
        intervals = []
        for entry in time_table_data:
            start_time=entry.start_time
            end_time=entry.end_time
            period_time = entry.period_time
            reces_break1 = entry.reces_break1
            reces_break2 = entry.reces_break2
            lunch_break = entry.lunch_break
            w_break1=entry.w_break1
            w_break2=entry.w_break2
            w_lunch=entry.w_lunch
            start_time = datetime.combine(datetime.today(), datetime.strptime(start_time, '%I:%M %p').time())
            end_time = datetime.combine(datetime.today(), datetime.strptime(end_time, '%I:%M %p').time())
            while start_time <= end_time:
                intervals.append((start_time.time()))
                if len(intervals) == w_break1:
                    start_time += timedelta(minutes=reces_break1)
                elif len(intervals) == w_lunch:
                    start_time += timedelta(minutes=lunch_break)
                elif len(intervals) == w_break2:
                    start_time += timedelta(minutes=reces_break2)
                else:
                    start_time += timedelta(minutes=period_time)

            for i in range(len(intervals)-1):
                start_end.append((intervals[i],intervals[i+1]))

        return start_end
    



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Course, Subject
from .forms import  CourseForm, SubjectForm

# def teacherregister(request):
#     k=Course.objects.all()
#     k1=Subject.objects.all()
    
#     if request.method == "POST":
#         organizationname = request.POST.get('organizationname')
#         registrationno = request.POST.get('registrationno')
#         address = request.POST.get('address')
#         username = request.POST.get('username')
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         designation  = request.POST.get('designation')
#         department  = request.POST.get('department')
#         dob  = request.POST.get('dob')
#         experiance = request.POST.get('experiance')
#         gender = request.POST.get('gender')
#         qualification  = request.POST.get('qualification')
#         subject1  = request.POST.get('subject1')
#         course1  = request.POST.get('course1')
#         email = request.POST.get('email')
#         image1 = request.FILES.get('image1')
#         phoneno = request.POST.get('phoneno')
#         password=request.POST.get('password')
#         confirm_password=request.POST.get('confirm_password')

 
        
#         data=Teachers.objects.create(
#             organizationname= organizationname,
#             registrationno= registrationno,
#             address= address,
#             first_name= first_name,
#             last_name= last_name,
#             username=username,
#             designation=designation,
#             department=department,
#             dob=dob,
#             qualification=qualification,
#             subject1=subject1,
#             course1=course1,
#             image1=image1,
#             email= email,
#             experiance=experiance,
#             phoneno= phoneno,
#             gender=gender,
#             password=password,
#             confirm_password=confirm_password,
            
            
#         )
#         data.save()
#         user=CustomUser.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password,user_type=2)
#         user.save()
       
        
#         # user.save()
        
        
        
#         return HttpResponse('Registered Successfully..!!')
  
#     return render(request, 'teacher_register.html',{'k':k,'k1':k1})

def teacherregister(request):
    k4=Course.objects.all()
    k1=Subject.objects.all()
    k5=different_shifts.objects.all()  
    k=MenuItem.objects.filter(parent_category=None)
    message = ''


    if request.method == "POST":
        organizationname = request.POST.get('organizationname')
        registrationno = request.POST.get('registrationno')
        address = request.POST.get('address')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        designation  = request.POST.get('designation')
        department  = request.POST.get('department')
        dob  = request.POST.get('dob')
        experiance = request.POST.get('experiance')
        gender = request.POST.get('gender')
        qualification  = request.POST.get('qualification')
        photo=request.FILES.get('photo')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        password=request.POST.get('password')
        staff_type = request.POST.get('staff_type')
        confirm_password=request.POST.get('confirm_password')
        name=request.POST.get('shift_name')
        user=CustomUser.objects.create_user(
            username=username,first_name=first_name,last_name=last_name,email=email,password=password,
            user_type=2)
        user.save()
        admin_user = CustomUser.objects.get(id=user.id)
        shift_instance=get_object_or_404(different_shifts,name=name)
        sch=Schools.objects.filter(usernumber=request.user.id).first()


        student = Teachers(
                organizationname=organizationname,
                registrationno=registrationno,
                address=address,
                first_name=first_name,
                last_name=last_name,
                username=username,
                designation=designation,
                department=department,
                dob=dob,
                qualification=qualification,
                photo=photo,
                email=email,
                experiance=experiance,
                phoneno=phoneno,
                gender=gender,
                password=password,
                staff_type=staff_type,
                confirm_password=confirm_password,
                shift_name=shift_instance,
                admin=admin_user,
                schoolid=sch

            )
        student.save()
        message ='Teacher Added Successfully.'
    return render(request, 'teacher_register.html',{'k':k,'k1':k1,'k5':k5,'k4':k4,'message':message})

# def teacher_read(request):
#     data = Teachers.objects.all()
#     return render(request,'teacher_read.html',{'data':data,})

def edit_teacher(request,id):
   k=Course.objects.all()
   k1=Subject.objects.all()
   dataget = Teachers.objects.get(id=id)
   data = Teachers.objects.all()
        
   if request.method == 'POST':

            organizationname = request.POST.get('organizationname')
            registrationno = request.POST.get('registrationno')
            address = request.POST.get('address')
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            designation  = request.POST.get('designation')
            department  = request.POST.get('department')
            dob  = request.POST.get('dob')
            gender = request.POST.get('gender')
            experiance = request.POST.get('experiance')
            qualification  = request.POST.get('qualification')
            subject1  = request.POST.get('subject1')
            course1  = request.POST.get('course1')
            email = request.POST.get('email')
            image1 = request.FILES.get('image1')
            phoneno = request.POST.get('phoneno')
            password=request.POST.get('password')
            confirm_password=request.POST.get('confirm_password')


        
            dataget.organizationname = organizationname
            dataget.registrationno = registrationno
            dataget.address = address
            dataget.username = username
            dataget.first_name = first_name
            dataget.last_name = last_name 
            dataget.email = email
            dataget.image1 = image1
            dataget.phoneno = phoneno
            dataget.department = department 
            dataget.designation = designation
            dataget.dob = dob
            dataget.gender = gender
            dataget.experiance = experiance
            dataget.qualification = qualification
            dataget.course1 = course1
            dataget.subject1 = subject1
            dataget.password = password
            dataget.confirm_password = confirm_password
            dataget.save()

            return redirect('teacher_read')  
        
   return render(request, 'edit_teacher_template.html', {'k':k,'k1':k1,'dataget':dataget,'data':data})
        

def teacher_delete(request,id):
    data = Teachers.objects.get(id=id)
    data.delete()
    return redirect('teacher_read')   



@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_course')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})


def add_subject(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_subject')
    else:
        form = SubjectForm()
    return render(request, 'add_subject.html', {'form': form})

  
def teacher_sidebar(request):
    return render(request,'teacher_sidebar.html')

# def student_sidebar(request):
#     k = studentnav.objects.filter(parent_category=None)
#     return render(request,'student_sidebar.html',{'k':k})
   


def logoupload(request):
    l=applogo.objects.all()
    return render(request,"logo.html",{'l':l})

def logoform(request):
    if(request.method=="POST"):
        logo=request.FILES.get('logo')
        l=applogo(logo=logo);
        l.save()
        messages.success(request,"logo uploaded successfully")
        return redirect("/logoupload")
    return render(request,"logo.html")


def examhome(request):
    if request.method=="GET":
        h=examcont.objects.all()
    return render(request,"examhome.html",{'h':h})

def examdisplay(request):
    if request.method=="GET":
        nav_items = HomeNav.objects.filter(parent_category=None)

        kl=footer_content.objects.all()
        links = FooterLink.objects.all()
        services = FooterService.objects.all()
        contact_info = ContactInfo.objects.first()
        social = SocialLink.objects.all()
        carldisplay=examcarl.objects.all()
        contdisplay=examcont.objects.all()
        carddisplay=examcards.objects.all()
    return render(request,"examdisplay.html",{'nav_items':nav_items,'kl':kl,'links':links,'contact_info':contact_info,'services':services,'carldisplay':carldisplay,'social':social,'contdisplay':contdisplay,'carddisplay':carddisplay})


def examinserte(request):
    if request.method=="POST":
        images=request.FILES.get('images')
        heading=request.POST['heading']
        content=request.POST['content']
        n=examcont.objects.all()
        n=examcont(images=images,heading=heading,content=content)
        n.save()
        return redirect("/examhome")
    return render(request,"examinsert.html")

def examedit(request,id):
    if request.method=="GET":
        u=examcont.objects.get(id=id)
    return render(request,"examupdate.html",{'u':u})

def examupdate(request,id):
    if request.method=='POST':
        images=request.FILES.get('images')
        heading=request.POST['heading']
        content=request.POST['content']
        u=examcont.objects.get(id=id)
        u.images=images
        u.heading=heading
        u.content=content
        u.save()
        return redirect("/examhome")
    return render(request,"examupdate.html")

def examdelete(request,id):
    d=examcont.objects.get(id=id)
    d.delete()
    return redirect("/examhome")


# carl_______________________________________________________________________________

def examhome2(request):
    if request.method=="GET":
        h=examcont.objects.all()
        h2=examcarl.objects.all()
        h3=examcards.objects.all()
    return render(request,"examhome2.html",{'h':h,'h2':h2,'h3':h3})

def examinsert2(request):
    if request.method=="POST":
        images=request.FILES.get('images')
        n2=examcarl.objects.all()
        n2=examcarl(images=images)
        n2.save()
        return redirect("/examhome2")
    return render(request,"examinsert2.html")

def examedit2(request,id):
    if request.method=="GET":
        u2=examcarl.objects.get(id=id)
    return render(request,"examupdate2.html",{'u2':u2})

def examupdate2(request,id):
    if request.method=="POST":
        images=request.FILES.get('images')
        u2=examcarl.objects.get(id=id)
        u2.images=images
        u2.save()
        return redirect("/examhome2")
    return render(request,"examupdate2.html")

def examdelete(request,id):
        d2=examcarl.objects.get(id=id)
        d2.delete()
        return redirect("/examhome2")



# cards_________________________________________________________________________________
def examhome3(request):
    if request.method=="GET":
        h3=examcards.objects.all()
    return render(request,"examhome3.html",{'h3':h3})

def examreadmore(request):
    if request.method=="GET":
        r=examcards.objects.all()
    return render(request,"examrm.html",{'r':r})

def examinsert3(request):
    if request.method=="POST":
        images=request.FILES.get('images')
        field=request.POST['field']
        n3=examcards.objects.all()
        n3=examcards(images=images,field=field)
        n3.save()
        return redirect("/examhome3")
    return render(request,"examinsert3.html")

def examedit3(request,id):
    if request.method=="GET":
        u3=examcards.objects.get(id=id)
    return render(request,"examupdate3.html",{'u3':u3})

def examupdate3(request,id):
    if request.method=="POST":
        images=request.FILES.get('images')
        field=request.POST['field']
        u3=examcards.objects.get(id=id)
        u3.images=images
        u3.field=field
        u3.save()
        return redirect("/examhome3")
    return render(request,"examupdate3.html")

def examdelete3(request,id):
        d3=examcards.objects.get(id=id)
        d3.delete()
        return redirect("/examhome3")

# --------------------------------------------------------------------

def regform_sub(request):
    if request.method == "POST":
        subjects = request.POST.get('subjects')
        intro = request.POST.get('intro')
        description = request.POST.get('description')
        subid = request.POST.get('subid')
        chaptername = request.POST.get('chaptername')
        chapterdis=request.POST.get('chapterdis')
        pdf=request.FILES.get('pdf')
        classes=request.POST.get('classes')
        classid=request.POST.get('classid')
        stdclass.objects.create(
            subjects=subjects,
            intro =intro ,
            description=description,
            subid =subid ,
            chaptername=chaptername,
            chapterdis=chapterdis,
            pdf=pdf,
            classes=classes,
            classid=classid
        )
        return HttpResponse("inserted successfully")
    return render(request, "insert.html")

def home_sub(request):
    if request.method=="GET":
        n=stdclass.objects.all()
        return render(request,"display_sub.html",{'n':n})
def sub(request, classid):
    if request.method == "GET":
        res = stdclass.objects.filter(classid=classid)
        return render(request, "sub.html", {'res': res})

def subject(request, subid):
    if request.method == "GET":
        res = stdclass.objects.filter(subid=subid)
        return render(request, "subject.html", {'res': res})
      
# def chapter(request,id,subid,classid):
#     if request.method == "GET":
#         res1 = stdclass.objects.filter(id=id)
#         n= stdclass.objects.filter(subid=subid)
#         z=stdclass.objects.filter(classid=classid)
#         m=stdclass.objects.all()
#         return render(request, "chapter.html", {'res1': res1,'n':n,'m':m,'z':z})


def chapter(request,id,subid,classid):
    res1 = stdclass.objects.filter(id=id)
    n= stdclass.objects.filter(subid=subid)
    z=stdclass.objects.filter(classid=classid)
    m=stdclass.objects.all()
    error_message = "Invalid login credentials. Please try again."
    
    if request.method=='POST':
          
            try:
                 
               user=EmailBackEnd.authenticate(request,username=request.POST.get("email"),password=request.POST.get("password"))
               if user != None:

                  login(request,user)
                  if user.user_type=="1":
                      uploaded_file = stdclass.objects.get(id=id)
                      response = HttpResponse(uploaded_file.pdf, content_type='application/force-download')
                      response['Content-Disposition'] = f'attachment; filename="{uploaded_file.pdf.name}"'
                      return response
        
                  if user.user_type=="2":
                      uploaded_file = stdclass.objects.get(id=id)
                      response = HttpResponse(uploaded_file.pdf, content_type='application/force-download')
                      response['Content-Disposition'] = f'attachment; filename="{uploaded_file.pdf.name}"'
                      return response
      
                  if user.user_type=="3":
                      uploaded_file = stdclass.objects.get(id=id)
                      response = HttpResponse(uploaded_file.pdf, content_type='application/force-download')
                      response['Content-Disposition'] = f'attachment; filename="{uploaded_file.pdf.name}"'
                      return response
            except CustomUser.DoesNotExist:
                 error_message = "Invalid login credentials. Please try again."
                 return redirect('/chapter')
    res1 = stdclass.objects.filter(id=id)
    n= stdclass.objects.filter(subid=subid)
    z=stdclass.objects.filter(classid=classid)
    m=stdclass.objects.all()
    return render(request, "chapter.html", {'res1': res1,'n':n,'m':m,'z':z,'error_message':error_message})        
    
def serve_pdf(request, document_id):
    document = get_object_or_404(stdclass, pk=document_id)
    response = FileResponse(open(document.pdf.path, 'rb'), content_type='application/pdf')
    return response

from .models import fee, crfee, cardfee

def insert_fee(request):
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['content']
        photo=request.FILES.get('photo')
        title1=request.POST['title1']
        content1=request.POST['content1']
        photo1=request.FILES.get('photo1')
        k=fee(title=title,content=content,photo=photo,title1=title1,content1=content1,photo1=photo1,)
        k.save()
        return HttpResponse("record is inserted")
    return render(request,"insert_fee.html")



def display_fee(request):
    nav_items = HomeNav.objects.filter(parent_category=None)

    kl=footer_content.objects.all()
    links = FooterLink.objects.all()
    services = FooterService.objects.all()
    contact_info = ContactInfo.objects.first()
    social = SocialLink.objects.all()

    if request.method=="GET":
        k=fee.objects.all()
        s=crfee.objects.all()
        c=cardfee.objects.all()
    return render(request,"display_fee.html",{'nav_items':nav_items,'kl':kl,'links':links,'services':services,'contact_info':contact_info,'social':social,'k':k,'s':s,'c':c})


      
def table_fee(request):
    if request.method=="GET":
        k=fee.objects.all()
        p=crfee.objects.all()
        o=cardfee.objects.all()
        return render(request,"table_fee.html",{'k':k,'p':p,'o':o})
      
def edit(request,id):
    if request.method=="GET":
        try:
            t=fee.objects.get(id=id)
        except fee.DoesNotExist:
            t = None
        return render(request,"update_fee.html",{'t':t})
    
        
def update_fee(request,id):
    if request.method=="POST":
        title=request.POST.get('title')
        subtitle=request.POST.get('subtitle')
        content=request.POST.get('content')
        photo=request.FILES.get('photo')
        title1=request.POST.get('title1')
        content1=request.POST.get('content1')
        photo1=request.FILES.get('photo1')
        k1=get_object_or_404(fee,id=id)
        k1.title=title
        k1.subtitle=subtitle
        k1.content=content
        if photo:
            k1.photo=photo
        k1.title1=title1
        k1.content1=content1
        if photo1:
            k1.photo1=photo1
        k1.save()
        return redirect("/table/")
    return render(request,"update_fee.html")
             
def delete_fee(request,id):  
    k1=fee.objects.get(id=id)
    k1.delete()
    return redirect("/table/")   




# carousel views

def crinsert_fee(request):
    if request.method=="POST":
        image=request.FILES.get('image')
        k=crfee(image=image)
        k.save()
        return HttpResponse("record is inserted")
    return render (request,"crinsert_fee.html")


def crtable_fee(request):
    if request.method=="GET":
        p=crfee.objects.all()
        return render(request,"crtable_fee.html",{'p':p})
    
    
def credit_fee(request,id):
    if request.method=="GET":
        q=crfee.objects.get(id=id)
        return render(request,"crupdate_fee.html",{'q':q})
    

def crupdate_fee(request,id):
    if request.method=="POST":
        image=request.FILES.get('image')
        k2=get_object_or_404(crfee,id=id)
        if image:
             k2.image=image
        k2.save()
        return redirect("/crtable_fee/")
    return render(request,"crupdate_fee.html")

        
def crdelete_fee(request,id):
    d=crfee.objects.get(id=id)
    d.delete()
    return redirect("/crtable_fee/") 



# card views

def cardinsert_fee(request):
    if request.method=="POST":
        cardtitle=request.POST['cardtitle']
        cardcontent=request.POST['cardcontent']
        cardphoto=request.FILES.get('cardphoto')
        m=cardfee(cardtitle=cardtitle,cardcontent=cardcontent,cardphoto=cardphoto)
        m.save()
        return HttpResponse("record is inserted")
    return render (request,"cardinsert_fee.html")


def cardtable(request):
    if request.method=="GET":
        o=cardfee.objects.all()
        return render(request,"cardtable_fee.html",{'o':o})
    
    
def cardedit(request,id):
    if request.method=="GET":
        q1=cardfee.objects.get(id=id)
        return render(request,"cardupdate_fee.html",{'q1':q1})
        

def cardupdate_fee(request,id):
    if request.method=="POST":
        cardtitle=request.POST['cardtitle']
        cardcontent=request.POST['cardcontent']
        cardphoto=request.FILES.get('cardphoto')
        k3=get_object_or_404(cardfee,id=id)
        k3.cardtitle=cardtitle
        k3.cardcontent=cardcontent
        if cardphoto:
            k3.cardphoto=cardphoto
        k3.save()
        return redirect("/cardtable/")
    return render(request,"cardupdate_fee.html")     


def carddelete_fee(request,id):
    k2=cardfee.objects.get(id=id)
    k2.delete()
    return redirect("/cardtable/")





def staffmanagement(request):
    nav_items = HomeNav.objects.filter(parent_category=None)

    kl=footer_content.objects.all()
    links = FooterLink.objects.all()
    services = FooterService.objects.all()
    contact_info = ContactInfo.objects.first()
    social = SocialLink.objects.all()
    st=staff.objects.all()
    f=staff_fea.objects.all()
    imp=staff_imp.objects.all()
    p=staff_prob.objects.all()
    return render(request,"staff.html",{'st':st,'f':f,'imp':imp,'p':p,'nav_items':nav_items,'kl':kl,'links':links,'services':services,'contact_info':contact_info,'social':social})

    
def staff_sms(request):
    if request.method == 'POST':
        heading = request.POST['heading']
        image = request.FILES.get('image')
        # discription = request.POST['discription']
        st =staff(heading=heading, image=image)
        st.save()
    return render(request, "staff_insert.html")

def fea_staff(request):
    if request.method=='POST':
        heading = request.POST['heading']
        paragraph2=request.POST['paragraph2']
        # image = request.FILES.get('image')
        discription = request.POST['discription']
        p1=request.POST['p1']
        paragraph2=request.POST['paragraph2']
        # paragraph3=request.POST['paragraph3']
        f = staff_fea(heading=heading,paragraph2=paragraph2, discription=discription,)
        f.save()
    return render(request, "staff.html")

def importance_staff(request):
    if request.method=='POST':
        main_heading = request.POST['main_heading']
        main_heading1 = request.POST['main_heading1']
        image = request.FILES.get('image')
        image2 = request.FILES.get('image2')
        paragraph1=request.POST['paragraph1']
        paragraph2=request.POST['paragraph2']
        imp = staff_imp(main_heading=main_heading, main_heading1=main_heading1,image=image,image2=image2,paragraph1=paragraph1,paragraph2=paragraph2)
        imp.save()
    return render(request, "staff_insert.html")

def prob_staff(request):
    if request.method=='POST':
        heading = request.POST['heading']
        discription = request.POST['discription']
        image = request.FILES.get('image')

        p= staff_prob(heading=heading, discription=discription,image=image)
        p.save()
    return render(request, "staff_cards.html")


from django.shortcuts import render,redirect
from .models import attendmanagecontent,attendmanagecarousel,attendmanagecards
from .serialization import attendmanagementclass1,attendmanagementclass2,attendmanagementclass3
from rest_framework import generics

# Create your views here.
class attendmanagecontentapi(generics.ListCreateAPIView):
    queryset=attendmanagecontent.objects.all()
    serializer_class=attendmanagementclass1
   
   
class amcarouselapi(generics.ListCreateAPIView):
    queryset=attendmanagecarousel.objects.all()
    serializer_class=attendmanagementclass2
    
class amcardsapi(generics.ListCreateAPIView):
    queryset=attendmanagecards.objects.all()
    serializer_class=attendmanagementclass3

    
def attendmanagedisplay(request):
    if request.method=="GET":
        nav_items = HomeNav.objects.filter(parent_category=None)

        kl=footer_content.objects.all()
        links = FooterLink.objects.all()
        services = FooterService.objects.all()
        contact_info = ContactInfo.objects.first()
        social = SocialLink.objects.all()
        attendmanag=attendmanagecontent.objects.all()
        attendcarousel=attendmanagecarousel.objects.all()
        carddisplay= attendmanagecards.objects.all()
         
    return render(request,"attendmanagedisplay.html",{'nav_items':nav_items,'kl':kl,'links':links,'services':services,'contact_info':contact_info,'social':social,'attendmanag':attendmanag,'attendcarousel':attendcarousel,'carddisplay':carddisplay})


def attendmanagecurd(request):
    if request.method=="GET":
        attendcurd=attendmanagecontent.objects.all()
        carouselcurd=attendmanagecarousel.objects.all()
        cardcurd=attendmanagecards.objects.all()
        return render(request,"attendmanagecurd.html",{'attendcurd':attendcurd,'carouselcurd':carouselcurd,'cardcurd':cardcurd})

def attendcontentinsert(request):
    if request.method=="POST":
        image1=request.FILES.get('image1')
        heading=request.POST['heading']
        content=request.POST['content']
        image2=request.FILES.get('image2')
        heading1=request.POST['heading1']
        content1=request.POST['content1']
        insertc=attendmanagecontent.objects.all()
        insertc=attendmanagecontent(image1=image1,heading=heading,content=content,image2=image2,heading1=heading1,content1=content1)
        insertc.save()
        return redirect("/attendmanagecurd")
    return render(request,"attendcontentinsert.html")


def attendcontentedit(request, id):
    if request.method == "GET":
        contentedit = attendmanagecontent.objects.get(id=id)
        return render(request, "attendcontentupdate.html", {'contentedit': contentedit})

def attendcontentupdate(request, id):
    if request.method == "POST":
        image1 = request.FILES.get('image1')
        heading = request.POST['heading']
        content = request.POST['content']
        image2=request.FILES.get('image2')
        heading1=request.POST['heading1']
        content1=request.POST['content1']
        updatec = attendmanagecontent.objects.get(id=id)
        updatec.image1 = image1
        updatec.heading = heading
        updatec.content = content
        updatec.image2=image2
        updatec.heading1=heading1
        updatec.content1=content1
        updatec.save()
        return redirect("/attendmanagecurd")
    return render(request, "attendcontentupdate.html", {'updatec': updatec})

       


def deletecontent(request, id):
    if request.method == "GET":
        deletec = attendmanagecontent.objects.get(id=id)
        deletec.delete()
        return redirect("/attendmanagecurd")



# ******************************************************carousel******************************  
def carouselinsert(request):
    if request.method=="POST":
        image2=request.FILES.get('image2')
        carouinsert=attendmanagecarousel.objects.all()
        carouinsert=attendmanagecarousel(image2=image2)
        carouinsert.save()
        return redirect("/attendmanagecurd")
    return render(request,"carouselinsert.html")

def carouseledit(request, id):
    if request.method == "GET":
        caredit = attendmanagecarousel.objects.get(id=id)
        return render(request, "carouselupdate.html", {'caredit': caredit})
    
def carouselupdate(request, id):
    if request.method == "POST":
        image2 = request.FILES.get('image2')
        carouupdate = attendmanagecarousel.objects.get(id=id)
        carouupdate.image2 = image2
        carouupdate.save()
        return redirect("/attendmanagecurd")
    return render(request, "carouselupdate.html", {'carouupdate': carouupdate})





def carouseldelete(request, id):
    caroudelete = attendmanagecarousel.objects.get(id=id)
    caroudelete.delete()
    return redirect("/attendmanagecurd")






# *****************************************************cards********************************************




def cardinsert(request):
    if request.method=="POST":
        image3=request.FILES.get('image3')
        field=request.POST['field']
        carinsert=attendmanagecards.objects.all()
        carinsert=attendmanagecards(image3=image3,field=field)
        carinsert.save()
        return redirect("/attendmanagecurd")
    return render(request,"cardinsert.html")

def cardedit(request, id):
    if request.method == "GET":
        caedit = attendmanagecards.objects.get(id=id)
        return render(request, "cardupdate.html", {'caedit': caedit})





def carupdate(request,id):
    if request.method=="POST":
        image3=request.FILES.get('image3')
        field=request.POST['field']
        caredit =attendmanagecards.objects.get(id=id)
        caredit.image3=image3
        caredit.field=field
        caredit.save()
        return redirect("/attendmanagecurd")
    return render(request,"cardupdate.html")

def carddelete(request,id):
        carddel=attendmanagecards.objects.get(id=id)
        carddel.delete()
        return redirect("/attendmanagecurd")   
    

from django.shortcuts import render,redirect
from .models import paymentfeatures,crpaymentfeatures,cardpaymentfeatures
from django.http import HttpResponse
# Create your views here.

def insert_paymentfeatures(request):
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['content']
        photo=request.FILES.get('photo')
        title1=request.POST['title1']
        content1=request.POST['content1']
        photo1=request.FILES.get('photo1')
        k=paymentfeatures(title=title,content=content,photo=photo,title1=title1,content1=content1,photo1=photo1,)
        k.save()
        return HttpResponse("record is inserted")
    return render(request,"insert_paymentfeatures.html")


def table_paymentfeatures(request):
    if request.method=="GET":
        k=paymentfeatures.objects.all()
        p=crpaymentfeatures.objects.all()
        return render(request,"table_paymentfeatures.html",{'k':k,'p':p,})

################ carousel ################

def crinsert_paymentfeatures(request):
    if request.method=="POST":
        image=request.FILES.get('image')
        k=crpaymentfeatures(image=image)
        k.save()
        return HttpResponse("record is inserted")
    return render (request,"crinsert_paymentfeatures.html")

def crtable_paymentfeatures(request):
    if request.mthod=="GET":
        p=crpaymentfeatures.objects.all()
        return render (request,"crtable_paymentfeatures.html",{'p':p})

################ cards ################

def cardinsert_paymentfeatures(request):
    if request.method=="POST":
        cardtitle=request.POST['cardtitle']
        cardcontent=request.POST['cardcontent']
        cardphoto=request.FILES.get('cardphoto')
        m=cardpaymentfeatures(cardtitle=cardtitle,cardcontent=cardcontent,cardphoto=cardphoto)
        m.save()
        return HttpResponse("record is inserted")
    return render (request,"cardinsert_paymentfeatures.html")

############  Display ################

def display_paymentfeatures(request):
     if request.method=="GET":
        nav_items = HomeNav.objects.filter(parent_category=None)

        kl=footer_content.objects.all()
        links = FooterLink.objects.all()
        services = FooterService.objects.all()
        contact_info = ContactInfo.objects.first()
        social = SocialLink.objects.all()
        k=paymentfeatures.objects.all()
        s=crpaymentfeatures.objects.all()
        c=cardpaymentfeatures.objects.all()
        return render(request,"display_paymentfeatures.html",{'k':k,'s':s,'c':c,'nav_items':nav_items,'kl':kl,'links':links,'services':services,'contact_info':contact_info,'social':social})


def admission_home1(request):
    if request.method=="GET":
        h1=admissioncarl.objects.all()
        h2=admissioncont.objects.all()
        h3=admissioncards.objects.all()
    return render(request,"admission_home1.html",{'h1':h1,'h2':h2,'h3':h3})

def admission_display(request):
    if request.method=="GET":
        nav_items = HomeNav.objects.filter(parent_category=None)

        kl=footer_content.objects.all()
        links = FooterLink.objects.all()
        services = FooterService.objects.all()
        contact_info = ContactInfo.objects.first()
        social = SocialLink.objects.all()
        adcarl=admissioncarl.objects.all()
        adcont=admissioncont.objects.all()
        adcards=admissioncards.objects.all()
    return render(request,"admission_display.html",{'adcarl':adcarl,'adcont':adcont,'adcards':adcards,'nav_items':nav_items,'kl':kl,'links':links,'services':services,'contact_info':contact_info,'social':social})


def admission_insert1(request):
    if request.method=="POST":
        images=request.FILES.get('images')
        content=request.POST['content']
        n1=admissioncarl.objects.all()
        n1=admissioncarl(images=images,content=content)
        n1.save()
        return redirect("/admission_home1")
    return render(request,"admission_insert1.html")

 
def admission_edit1(request,id):
    if request.method=="GET":
        u1=admissioncarl.objects.get(id=id)
    return render(request,"admission_update1.html",{'u1':u1})

def admission_update1(request,id):
    if request.method=="POST":
        images=request.FILES.get('images')
        content=request.POST['content']
        u1=admissioncarl.objects.get(id=id)
        u1.images=images
        u1.content=content
        u1.save()
        return redirect("/admission_home1")
    return render(request,"admission_update1.html")

def admission_delete1(request,id):
        d1=admissioncarl.objects.get(id=id)
        d1.delete()
        return redirect("/admission_home1")

# content___________________________________________________________________________________________________________

def admission_home2(request):
    if request.method=="GET":
        h2=admissioncont.objects.all()
    return render(request,"admission_home2.html",{'h2':h2})


def admission_insert2(request):
    if request.method=="POST":
        images=request.FILES.get('images')
        heading=request.POST['heading']
        content=request.POST['content']
        images1=request.FILES.get('images1')
        heading1=request.POST['heading1']
        content1=request.POST['content1']
        n2=admissioncont.objects.all()
        n2=admissioncont(images=images,heading=heading,content=content,images1=images1,heading1=heading1,content1=content1)
        n2.save()
        return redirect("/admission_home2")
    return render(request,"admission_insert2.html")

def admission_edit2(request,id):
    if request.method=="GET":
        u2=admissioncont.objects.get(id=id)
    return render(request,"admission_update2.html",{'u2':u2})

def admission_update2(request,id):
    if request.method=="POST":
        images=request.FILES.get('images')
        heading=request.POST['heading']
        content=request.POST['content']
        images1=request.FILES.get('images1')
        heading1=request.POST['heading1']
        content1=request.POST['content1']
        u2=admissioncont.objects.get(id=id)
        u2.images=images
        u2.heading=heading
        u2.content=content
        u2.images1=images1
        u2.heading1=heading1
        u2.content1=content1
        u2.save()
        return redirect("/admission_home2")
    return render(request,"admission_update2.html")


def admission_delete2(request,id):
        d2=admissioncont.objects.get(id=id)
        d2.delete()
        return redirect("/admission_home2")

# cards________________________________________________________________________________________

def admission_home3(request):
    if request.method=="GET":
        h3=admissioncards.objects.all()
    return render(request,"admission_home3.html",{'h3':h3})

def admission_insert3(request):
    if request.method=="POST":
        images=request.FILES.get('images')
        heading=request.POST['heading']
        content=request.POST['content']
        n3=admissioncards.objects.all()
        n3=admissioncards(images=images,heading=heading,content=content)
        n3.save()
        return redirect("/admission_home3")
    return render(request,"admission_insert3.html")

def admission_edit3(request,id):
    if request.method=="GET":
        u3=admissioncards.objects.get(id=id)
    return render(request,"admission_update3.html",{'u3':u3})

def admission_update3(request,id):
    if request.method=="POST":
        images=request.FILES.get('images')
        heading=request.POST['heading']
        content=request.POST['content']
        u3=admissioncards.objects.get(id=id)
        u3.images=images
        u3.heading=heading
        u3.content=content
        u3.save()
        return redirect("/admission_home3")
    return render(request,"admission_update3.html")

def admission_delete3(request,id):
        d3=admissioncards.objects.get(id=id)
        d3.delete()
        return redirect("/admission_home3")



from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import FooterLink,FooterService,ContactInfo,SocialLink

from .models import *
from .forms import *

def contact(request):
    nav_items = HomeNav.objects.filter(parent_category=None)
    links = FooterLink.objects.all()
    services = FooterService.objects.all()
    contact_info = ContactInfo.objects.first()
    social = SocialLink.objects.all()
    contact_info2 = ContactInfo2.objects.first()  
    kl=footer_content.objects.all()

    context = {
                 'links':links,'nav_items':nav_items,'kl':kl,'services':services,'contact_info':contact_info,'social':social,'contact_info2': contact_info2
        }
    if request.method == 'POST':
        # Retrieve form data directly from the request
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Save the message to the database
        contact_message = ContactMessage(name=name, email=email, subject=subject, message=message)
        contact_message.save()

        # Optionally, you can send an email notification here.
        return redirect('success_page')  # Redirect to a success page
    else:
        return render(request, 'contact.html',context)



def success_page(request):
        return render(request,'contactsuccess.html')

def create_contact_info(request):
    if request.method == 'POST':
        form = ContactInfo2Form(request.POST)  # Assuming you have a form for validation
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page
    else:
        form = ContactInfo2Form()
    context = {'form': form}
    return render(request, 'create_contact_info.html', context)

def view_contact_info(request):
    contact_info2 = ContactInfo2.objects.first()  # Adjust for multi-record retrieval if needed
    context = {'contact_info2': contact_info2}
    return render(request, 'view_contact_info.html', context)

def update_contact_info(request, pk):  # Assuming a primary key for identification
    try:
        contact_info2 = ContactInfo2.objects.get(pk=pk)
    except ContactInfo2.DoesNotExist:
        raise Http404("Contact information not found")

    if request.method == 'POST':
        form = ContactInfo2Form(request.POST, instance=contact_info2)
        if form.is_valid():
            form.save()
            return redirect('view_contact_info')
    else:
        form = ContactInfo2Form(instance=contact_info2)
    context = {'form': form}
    return render(request, 'update_contact_info.html', context)

def delete_contact_info(request, pk):  # Assuming a primary key for identification
    try:
        contact_info2 = ContactInfo2.objects.get(pk=pk)
    except ContactInfo2.DoesNotExist:
        raise Http404("Contact information not found")

    if request.method == 'POST':
        contact_info2.delete()
        return redirect('contact_list')  # Redirect to a list of contact information
    else:
        context = {'contact_info2': contact_info2}
        return render(request, 'delete_contact_info.html', context)
    

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import ContactMessage

def retrieve_contact_messages(request):
    contact_messages = ContactMessage.objects.all().order_by('-timestamp')
    context = {'contact_messages': contact_messages}
    return render(request, 'retrive_contact.html', context)

def reply_message(request, message_id):
    message = ContactMessage.objects.get(id=message_id)

    if request.method == 'POST':
        reply_content = request.POST.get('reply_content')
        send_mail(
            subject='Re: ' + message.subject,
            message=reply_content,
            from_email=settings.DEFAULT_FROM_EMAIL,  # Adjust as needed
            recipient_list=[message.email],
        )
        return redirect('retrieve_contact_messages')  # Redirect to message list

    return render(request, 'reply_message_form.html', {'message': message})

def upload_image(request):
    
    if request.method=="POST":
        image=request.FILES.get('image')
        ading=adminphoto.objects.first()
        if ading:
            ading.image=image
            ading.save()
        else:
            pho=adminphoto(image=image)
            pho.save()
        messages.success(request,"your Profile Pic is saved successfully")  
        return redirect("/new_home1")
    return render(request,"upload_image.html")

def footer_view(request):
    links = FooterLink.objects.all()
    services = FooterService.objects.all()
    contact_info = ContactInfo.objects.first()
    social = SocialLink.objects.all()


    return render(request, 'footer.html', {
        'links': links,
        'services': services,
        'contact_info': contact_info,
        'social' : social
    })




from .models import liveclasscontent,liveclasscarousel,liveclasscards
from .serialization import liveclassmanagementclass1,livemanagementclass2,livemanagementclass3
from rest_framework import generics

# Create your views here.
class liveclasscontentapi(generics.ListCreateAPIView):
    queryset=liveclasscontent.objects.all()
    serializer_class=liveclassmanagementclass1
   
   
class lccarouselapi(generics.ListCreateAPIView):
    queryset=liveclasscarousel.objects.all()
    serializer_class=livemanagementclass2
    
class lccardsapi(generics.ListCreateAPIView):
    queryset=liveclasscards.objects.all()
    serializer_class=livemanagementclass3

    
def liveclassmanagedisplay(request):
    if request.method=="GET":
        nav_items = HomeNav.objects.filter(parent_category=None)

        kl=footer_content.objects.all()
        links = FooterLink.objects.all()
        services = FooterService.objects.all()
        contact_info = ContactInfo.objects.first()
        social = SocialLink.objects.all()
        livemanag=liveclasscontent.objects.all()
        livecarousel=liveclasscarousel.objects.all()
        liveclassdisplay= liveclasscards.objects.all()
         
    return render(request,"livemanagedisplay.html",{'livemanag':livemanag,'livecarousel':livecarousel,'liveclassdisplay':liveclassdisplay,'nav_items':nav_items,'kl':kl,'links':links,'services':services,'contact_info':contact_info,'social':social})


def  livemanagecurd(request):
    if request.method=="GET":
        livemanagecurd=liveclasscontent.objects.all()
        livecarouselcurd=liveclasscarousel.objects.all()
        liveclasscardcurd= liveclasscards.objects.all()
        return render(request,"livemanagecurd.html",{'livemanagecurd':livemanagecurd,'livecarouselcurd':livecarouselcurd,'liveclasscardcurd':liveclasscardcurd})

def livecontentinsert(request):
    if request.method=="POST":
        image1=request.FILES.get('image1')
        heading=request.POST['heading']
        content=request.POST['content']
        content1=request.POST['content1']

        insertc=liveclasscontent.objects.all()
        insertc=liveclasscontent(image1=image1,heading=heading,content=content,content1=content1)
        insertc.save()
        return redirect("/livemanagecurd")
    return render(request,"livecontentinsert.html")


def livecontentedit(request, id):
    if request.method == "GET":
        lcontentedit = liveclasscontent.objects.get(id=id)
        return render(request, "livecontentupdate.html", {'lcontentedit': lcontentedit})

def livecontentupdate(request, id):
    if request.method == "POST":
        image1 = request.FILES.get('image1')
        heading = request.POST['heading']
        content = request.POST['content']
        content1 = request.POST['content1']

        updatec = liveclasscontent.objects.get(id=id)
        updatec.image1 = image1
        updatec.heading = heading
        updatec.content = content
        updatec.content1 = content1
        updatec.save()
        return redirect("/livemanagecurd")
    return render(request, "livecontentupdate.html", {'updatec': updatec})





def livecontentdelete(request, id):
    if request.method == "GET":
        deletec = liveclasscontent.objects.get(id=id)
        deletec.delete()
        return redirect("/livemanagecurd")



# ******************************************************carousel******************************  
def livecarouselinsert(request):
    if request.method=="POST":
        image2=request.FILES.get('image2')
        lcarouinsert= liveclasscarousel.objects.all()
        lcarouinsert= liveclasscarousel(image2=image2)
        lcarouinsert.save()
        return redirect("/livemanagecurd")
    return render(request,"livecarouselinsert.html")

def livecarouseledit(request, id):
    if request.method == "GET":
        lcaredit =  liveclasscarousel.objects.get(id=id)
        return render(request, "livecarouselupdate.html", {'lcaredit': lcaredit})
    
def livecarouselupdate(request, id):
    if request.method == "POST":
        image2 = request.FILES.get('image2')
        lcarouupdate =  liveclasscarousel.objects.get(id=id)
        lcarouupdate.image2 = image2
        lcarouupdate.save()
        return redirect("/livemanagecurd")
    return render(request, "livecarouselupdate.html", {'lcarouupdate': lcarouupdate})







def livecarouseldelete(request, id):
    lcaroudelete =  liveclasscarousel.objects.get(id=id)
    lcaroudelete.delete()
    return redirect("/livemanagecurd")









# *****************************************************cards********************************************




def livecardinsert(request):
    if request.method=="POST":
        image3=request.FILES.get('image3')
        field=request.POST['field']
        lcarinsert= liveclasscards.objects.all()
        lcarinsert= liveclasscards(image3=image3,field=field)
        lcarinsert.save()
        return redirect("/livemanagecurd")
    return render(request,"livecardinsert.html")

def livecardedit(request, id):
    if request.method == "GET":
        lcaedit =  liveclasscards.objects.get(id=id)
        return render(request, "livecardupdate.html", {'lcaedit': lcaedit})




    

def livecarupdate(request,id):
    if request.method=="POST":
        image3=request.FILES.get('image3')
        field=request.POST['field']
        lcaredit = liveclasscards.objects.get(id=id)
        lcaredit.image3=image3
        lcaredit.field=field
        lcaredit.save()
        return redirect("/livemanagecurd")
    return render(request,"livecardupdate.html")

def livecarddelete(request,id):
        lcarddel= liveclasscards.objects.get(id=id)
        lcarddel.delete()
        return redirect("/livemanagecurd")
 
 

def timetable_home1(request):
    if request.method=="GET":
        h1=timetablecarl.objects.all()
        h2=timetablecont.objects.all()
        h3=timetablecards.objects.all()
    return render(request,"timetable_home1.html",{'h1':h1,'h2':h2,'h3':h3})

# def timetable_display(request):
#     if request.method=="GET":
#         k=timetablecarl.objects.all()
#         s=timetablecont.objects.all()
#         c=timetablecards.objects.all()
      
#     return render(request,"timetable_display.html",{'k':k,'s':s,'c':c})

def timetable_display(request):
     if request.method=="GET":
        nav_items = HomeNav.objects.filter(parent_category=None)

        kl=footer_content.objects.all()
        links = FooterLink.objects.all()
        services = FooterService.objects.all()
        contact_info = ContactInfo.objects.first()
        social = SocialLink.objects.all()
        k=Time.objects.all()
        s=Timage.objects.all()
        c=cards.objects.all()
        return render(request,"Table.html",{'k':k,'s':s,'c':c,'nav_items':nav_items,'kl':kl,'links':links,'services':services,'contact_info':contact_info,'social':social})

def timetable_insert1(request):
    if request.method=="POST":
        images=request.FILES.get('images')
        content=request.POST['content']
        n1=timetablecarl.objects.all()
        n1=timetablecarl(images=images,content=content)
        n1.save()
        return redirect("/timetable_home1")
    return render(request,"timetable_insert1.html")

def timetable_edit1(request,id):
    if request.method=="GET":
        u1=timetablecarl.objects.get(id=id)
    return render(request,"timetable_update1.html",{'u1':u1})

def timetable_update1(request,id):
    if request.method=="POST":
        images=request.FILES.get('images')
        content=request.POST['content']
        u1=timetablecarl.objects.get(id=id)
        u1.images=images
        u1.content=content
        u1.save()
        return redirect("/timetable_home1")
    return render(request,"timetable_update1.html")

def timetable_delete1(request,id):
    d1=timetablecarl.objects.get(id=id)
    d1.delete()
    return redirect("/timetable_home1")

# content___________________________________________________________________________________________________________

def timetable_home2(request):
    if request.method=="GET":
        h2=timetablecont.objects.all()
    return render(request,"timetable_home2.html",{'h2':h2})


def timetable_insert2(request):
    if request.method=="POST":
        images=request.FILES.get('images')
        heading=request.POST['heading']
        content=request.POST['content']
        n2=timetablecont.objects.all()
        n2=timetablecont(images=images,heading=heading,content=content)
        n2.save()
        return redirect("/timetable_home2")
    return render(request,"timetable_insert2.html")

def timetable_edit2(request,id):
    if request.method=="GET":
        u2=timetablecont.objects.get(id=id)
    return render(request,"timetable_update2.html",{'u2':u2})

def timetable_update2(request,id):
    if request.method=="POST":
        images=request.FILES.get('images')
        heading=request.POST['heading']
        content=request.POST['content']
        u2=timetablecont.objects.get(id=id)
        u2.images=images
        u2.heading=heading
        u2.content=content
        u2.save()
        return redirect("/timetable_home2")
    return render(request,"timetable_update2.html")

def timetable_delete2(request,id):
    d2=timetablecont.objects.get(id=id)
    d2.delete()
    return redirect("/timetable_home2")

# cards________________________________________________________________________________________

def timetable_home3(request):
    if request.method=="GET":
        h3=timetablecards.objects.all()
    return render(request,"timetable_home3.html",{'h3':h3})

def timetable_insert3(request):
    if request.method=="POST":
        images=request.FILES.get('images')
        heading=request.POST['heading']
        content=request.POST['content']
        n3=timetablecards.objects.all()
        n3=timetablecards(images=images,heading=heading,content=content)
        n3.save()
        return redirect("/timetable_home3")
    return render(request,"timetable_insert3.html")

def timetable_edit3(request,id):
    if request.method=="GET":
        u3=timetablecards.objects.get(id=id)
    return render(request,"timetable_update3.html",{'u3':u3})

def timetable_update3(request,id):
    if request.method=="POST":
        images=request.FILES.get('images')
        heading=request.POST['heading']
        content=request.POST['content']
        u3=timetablecards.objects.get(id=id)
        u3.images=images
        u3.heading=heading
        u3.content=content
        u3.save()
        return redirect("/timetable_home3")
    return render(request,"timetable_update3.html")

def timetable_delete3(request,id):
    d3=timetablecards.objects.get(id=id)
    d3.delete()
    return redirect("/timetable_home3")
   



def footer1(request):
    if request.method=="POST":
        linkname=request.POST['linkname']
        linkurl=request.POST['linkurl']
        order=request.POST['order']
       
        k=footer_content(linkname=linkname,linkurl=linkurl,order=order)
        k.save()
        return HttpResponse("data is recorded successfully")
    return render(request,"footer_register_form.html")


def footer_data(request):
    kl=footer_content.objects.all()
    links = FooterLink.objects.all()
    services = FooterService.objects.all()
    contact_info = ContactInfo.objects.first()
    social = SocialLink.objects.all()

    return render(request,"footer_subjects.html",{'kl':kl,'links':links,'services':services,'contact_info':contact_info,'social':social})


def adminA_Password_save(request):
    if request.method == 'POST':
        user = CustomUser.objects.get(is_superuser=True,id=request.user.id)
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password and password == confirm_password:
            user.password = make_password(password)
            user.save()
        return redirect('/new_home1')
    return render(request,"adminA_password.html")

from django.shortcuts import render, get_object_or_404, redirect
from .models import staff_imp

def importance_staff(request):
    if request.method=='POST':
        main_heading = request.POST['main_heading']
        image = request.FILES.get('image')
        paragraph1=request.POST['paragraph1']
        paragraph2=request.POST['paragraph2']
        imp = staff_imp(main_heading=main_heading, image=image,paragraph1=paragraph1,paragraph2=paragraph2)
        imp.save()
    return render(request, "staff_imp_insert.html")

def display_staff_imp_data(request):
    staff_imp_data = staff_imp.objects.all()
    return render(request, 'display_staff_imp_data.html', {'staff_imp_data': staff_imp_data})
def display_staff_imp_data(request):
    staff_imp_data=staff_imp.objects.all()
    return render(request,'display_staff_imp_data.html',{'staff_imp_data':staff_imp_data})

def edit_staff_imp_data(request, pk):
    data = get_object_or_404(staff_imp, pk=pk)

    if request.method == "POST":
        data.main_heading = request.POST['main_heading']
        if 'image' in request.FILES:
            data.image = request.FILES['image']
        data.paragraph1 = request.POST['paragraph1']
        data.paragraph2 = request.POST['paragraph2']
        data.save()
        return redirect('display_staff_imp_data')

    return render(request, 'edit_staff_imp_data.html', {'data': data})

def delete_staff_imp_data(request, pk):
    data = get_object_or_404(staff_imp, pk=pk)
    if request.method == "POST":
        data.delete()
        return redirect('display_staff_imp_data')
    return render(request, 'delete_staff_imp_data.html', {'data': data})

def prob_staff(request):
    if request.method == 'POST':
        heading = request.POST['heading']
        discription = request.POST['discription']  # Fix the typo here
        p1 = request.POST['p1']
        p = staff_prob(heading=heading, discription=discription, p1=p1)
        p.save()
    return render(request, "staff_prob_insert.html")

def display_staff_prob_data(request):
    staff_prob_data = staff_prob.objects.all()
    return render(request, 'display_staff_prob_data.html', {'staff_prob_data': staff_prob_data})

def edit_staff_prob_data(request, pk):
    data = get_object_or_404(staff_prob, pk=pk)

    if request.method == "POST":
        data.heading = request.POST['heading']
        data.discription = request.POST['discription']
        data.p1 = request.POST['p1']
        data.save()
        return redirect('display_staff_prob_data')

    return render(request, 'edit_staff_prob_data.html', {'data': data})

def delete_staff_prob_data(request, pk):
    data = get_object_or_404(staff_prob, pk=pk)
    if request.method == "POST":
        data.delete()
        return redirect('display_staff_prob_data')
    return render(request, 'delete_staff_prob_data.html', {'data': data})

from django.shortcuts import render, get_object_or_404, redirect
from .models import staff_fea

def fea_staff(request):
    if request.method == 'POST':
        heading = request.POST['heading']
        p1=request.POST['p1']
        paragraph2 = request.POST['paragraph2']
        discription = request.POST['discription']
        f = staff_fea(heading=heading,  p1=p1, paragraph2=paragraph2, discription=discription)
        f.save()
    return render(request, "staff_fea_insert.html")

def display_fea_data(request):
    fea_data = staff_fea.objects.all()
    staff_prob_data = staff_prob.objects.all()
    staff_imp_data = staff_imp.objects.all()
    return render(request, 'display_fea_data.html', {'fea_data': fea_data,'staff_prob_data':staff_prob_data,'staff_imp_data':staff_imp_data})

def edit_fea_data(request, pk):
    data = get_object_or_404(staff_fea, pk=pk)
    if request.method == "POST":
        # Update the data fields based on the form submission
        data.heading = request.POST['heading']
        data.discription = request.POST['discription']
        data.p1 = request.POST['p1']
        data.paragraph2 = request.POST['paragraph2']
        data.save()  
        return redirect('display_fea_data')  # Redirect to the display page after successful update
    return render(request, 'edit_fea_data.html', {'data': data})

def delete_fea_data(request, pk):
    data = get_object_or_404(staff_fea, pk=pk)
    if request.method == "POST":
        data.delete()
        return redirect('display_fea_data')
    return render(request, 'delete_fea_data.html', {'data': data})


def insert_library(request):
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['content']
        photo=request.FILES.get('photo')
        title1=request.POST['title1']
        content1=request.POST['content1']
        photo1=request.FILES.get('photo1')
        k=library(title=title,content=content,photo=photo,title1=title1,content1=content1,photo1=photo1,)
        k.save()
        return HttpResponse("record is inserted")
    return render(request,"insert_library.html")


def table_library(request):
    if request.method=="GET":
        k=library.objects.all()
        p=cimage.objects.all()
        return render(request,"table_library.html",{'k':k,'p':p,})

################ carousel ################

def crinsert_cimage(request):
    if request.method=="POST":
        image=request.FILES.get('image')
        k=cimage(image=image)
        k.save()
        return HttpResponse("record is inserted")
    return render (request,"crinsert_card.html")

def crtable_card(request):
    if request.mthod=="GET":
        p=cimage.objects.all()
        return render (request,"crtable_card.html",{'p':p})

################ cards ################

def cardinsert_card(request):
    if request.method=="POST":
        cardtitle=request.POST['cardtitle']
        cardcontent=request.POST['cardcontent']
        cardphoto=request.FILES.get('cardphoto')
        m=card(cardtitle=cardtitle,cardcontent=cardcontent,cardphoto=cardphoto)
        m.save()
        return HttpResponse("record is inserted")
    return render (request,"cardinsert_paymentfeatures.html")

############  Display ################

def display_display(request):
     if request.method=="GET":
        nav_items = HomeNav.objects.filter(parent_category=None)

        kl=footer_content.objects.all()
        links = FooterLink.objects.all()
        services = FooterService.objects.all()
        contact_info = ContactInfo.objects.first()
        social = SocialLink.objects.all()
        k=library.objects.all()
        s=cimage.objects.all()
        c=card.objects.all()
        return render(request,"pavan.html",{'k':k,'s':s,'c':c,'nav_items':nav_items,'kl':kl,'links':links,'services':services,'contact_info':contact_info,'social':social})


from django.shortcuts import render
form = MyForm()
def dd(request):
    if request.method=="POST":
        content=request.POST["content"]
        mn=MyForm.objects.create(content=content)
    return render(request, 'temp.html', {'form': form})

def ins(request):
    f=text.objects.all()
    if request.method=="POST":
        details=request.POST["details"]
        mn=text(details=details)
        mn.save()
        return HttpResponseRedirect('/ins')
    return render(request,"create.html",{'f':f})






from django.shortcuts import render
form = MyForm()
def dd(request):
    if request.method=="POST":
        content=request.POST["content"]
        mn=MyForm.objects.create(content=content)
    return render(request, 'temp.html', {'form': form})

def ins(request):
    f=text.objects.all()
    if request.method=="POST":
        details=request.POST["details"]
        mn=text(details=details)
        mn.save()
        return HttpResponseRedirect('/ins')
    return render(request,"create.html",{'f':f})

def pricing1(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        pr = pricing_head(title=title,content=content)
        pr.save()
        return HttpResponse("record is submitted")
    return render(request,"pricing_head_reg.html")

def home(request):
    if request.method=="GET":
        pr=pricing_head.objects.all()
    return render(request,"pricing_table.html",{'pr':pr})  

def edit(request,id):
        pr1=pricing_head.objects.get(id=id)
        return render(request,"pricingupdate.html",{'pr1':pr1})  

def update(request,id):
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['content']
        pr=pricing_head.objects.get(id=id)
        pr.title=title
        pr.content=content
        pr.save()
        return redirect("/home")
    return render(request,"pricingupdate.html")

def delete(request,id):
        pr=pricing_head.objects.get(id=id)
        pr.delete()
        return redirect("/home")

def pricing2(request):
    if request.method == "POST":
        icon = request.POST['icon']
        title = request.POST['title']
        content = request.POST['content']
        prb = pricing_body(title=title,content=content,icon=icon)
        prb.save()
        return HttpResponse("record is inserted")
    return render(request,"pricing_body_reg.html")

def body_table(request):
    if request.method=="GET":
        s=pricing_body.objects.all()
    return render(request,"body_read.html",{'s':s})

def body_edit(request,id):
    prb1=pricing_body.objects.get(id=id)
    return render(request,"body_up.html",{'prb1':prb1})

def body_update(request,id):
    if request.method=="POST":
        title=request.POST['title']
        content=request.POST['content']
        icon=request.POST['icon']
        prb=pricing_body.objects.get(id=id)
        prb.title=title
        prb.content=content
        prb.icon=icon
        prb.save()
        return redirect("/body_table")
    return render(request,"body_up.html")

def body_delete(request,id):
    prb=pricing_body.objects.get(id=id)
    prb.delete()
    return redirect("/body_table")


def pricing(request):  
    nav_items = HomeNav.objects.filter(parent_category=None)
    kl = footer_content.objects.all()
    links = FooterLink.objects.all()
    services = FooterService.objects.all()
    contact_info = ContactInfo.objects.first()
    social = SocialLink.objects.all()
    pr1 = pricing_head.objects.all()
    prb = pricing_body.objects.all()
    k = plans.objects.all()
    p1 = plans1.objects.all()
    k2 = plans2.objects.all()
    
    # Retrieve all pricing plans
    pricing_plans = PricingPlan.objects.all()
    
  
    
    return render(request, "pricing.html", {
        'nav_items': nav_items,
        'pr1': pr1,
        'prb': prb,
        'k': k,
        'kl': kl,
        'k2': k2,
        'p1': p1,
        'links': links,
        'services': services,
        'contact_info': contact_info,
        'social': social,
        'pricing_plans': pricing_plans
    })


# def order_now(request, plan_type, plan_id):
#     # Fetch the plan details based on plan_type and plan_id
#     # For example:
#     if plan_type == 'basic':
#         plan = plans.objects.get(pk=plan_id)
#     elif plan_type == 'premium':
#         plan = plans1.objects.get(pk=plan_id)
#     elif plan_type == 'advanced':
#         plan = plans2.objects.get(pk=plan_id)
#     return redirect('regform', plan_type=plan_type, plan_id=plan_id)

from .models import plans,plans1,plans2

# def plans_reg(request):
#     if request.method=="POST":
#         plan=request.POST['plan']
#         amt=request.POST['amt']
#         features=request.POST['features']
#         k=plans(plan=plan,amt=amt,features=features)
#         k.save()
#         return HttpResponse("data is inserted")
#     return render(request,"plans_reg.html")

# def plans_table(request):
#     if request.method=="GET":
#         k=plans.objects.all()
       
#     return render(request,"read.html",{'k':k})

# def plans_reg1(request):
#     if request.method=="POST":
#         plan1=request.POST['plan1']
#         amt1=request.POST['amt1']
#         features1=request.POST['features1']
#         k1=plans1(plan1=plan1,amt1=amt1,features1=features1)
#         k1.save()
#         return HttpResponse("data is inserted")
#     return render(request,"plans_reg1.html")

# def plans_reg2(request):
#     if request.method=="POST":
#         plan2=request.POST['plan2']
#         amt2=request.POST['amt2']
#         features2=request.POST['features2']
#         k2=plans2(plan2=plan2,amt2=amt2,features2=features2)
#         k2.save()
#         return HttpResponse("data is inserted")
#     return render(request,"plans_reg2.html")


# views.py
from django.shortcuts import render
from .models import PricingPlan

def add_pricing_plan(request):
    success_message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        price_monthly = request.POST.get('price_monthly')
        price_yearly = request.POST.get('price_yearly')
        
        # Create a new PricingPlan object
        new_plan = PricingPlan.objects.create(
            name=name,
            price_monthly=price_monthly,
            price_yearly=price_yearly
        )
        
        # Set the success message
        success_message = 'Pricing plan created successfully!'
    
    return render(request, 'add_pricing_plan.html', {'success_message': success_message})

# views.py
from django.shortcuts import render
from .models import Feature, PricingPlan

def add_feature(request):
    success_message = None
    if request.method == 'POST':
        name = request.POST.get('name')
        plan_id = request.POST.get('plan')
        plan = PricingPlan.objects.get(pk=plan_id)
        
        # Create a new Feature object
        new_feature = Feature.objects.create(
            name=name,
            plan=plan
        )
        
        # Set the success message
        success_message = 'Feature added successfully!'
    
    # Pass the pricing plans and success message to the template
    pricing_plans = PricingPlan.objects.all()
    return render(request, 'add_feature.html', {'pricing_plans': pricing_plans, 'success_message': success_message})

def pricing_table(request):
    # Retrieve all pricing plans and their features
    pricing_plans = PricingPlan.objects.all()
    return render(request, 'pricing_table.html', {'pricing_plans': pricing_plans})





from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils.safestring import mark_safe
from django.http import HttpResponseServerError
from .models import CustomUser, EmployeeLoginLogout, shift_names, teachersidebar, Student
from datetime import datetime, date, timedelta
import calendar
from django.http import HttpResponseServerError
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import date, datetime, timedelta
import calendar
import re
import logging
from datetime import datetime, timedelta
from calendar import HTMLCalendar
from django.shortcuts import render
from django.views.generic import ListView
from django.urls import reverse_lazy
from .models import Student, CustomUser, teachersidebar, shift_names, EmployeeLoginLogout
import re
from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.utils.safestring import mark_safe
from django.http import HttpResponseServerError
from .models import Student, CustomUser, shift_names, EmployeeLoginLogout, MenuItem
from datetime import datetime, date, timedelta
import calendar
import re
import logging
from calendar import HTMLCalendar

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.utils.safestring import mark_safe
from datetime import datetime, date, timedelta
import calendar, re, logging
from calendar import HTMLCalendar
from .models import Student, CustomUser, shift_names, EmployeeLoginLogout, MenuItem

class CombinedView(ListView):
    model = Student
    template_name = 'percentage_view.html'

    def convert_duration_to_seconds(self, duration):
        """Converts a timedelta duration to seconds."""
        return int(duration.total_seconds())

    def parse_duration_string(self, duration_string):
        """Parses a string formatted as 'Xh Xm Xs' into a timedelta object."""
        duration_match = re.match(r'(\d+)h (\d+)m (\d+)s', duration_string)
        if duration_match:
            hours, minutes, seconds = map(int, duration_match.groups())
            return timedelta(hours=hours, minutes=minutes, seconds=seconds)
        return timedelta()

    def calculate_total_hours(self, start, end):
        """Calculates the total hours between two time objects."""
        start_datetime = datetime.combine(date.today(), start)
        end_datetime = datetime.combine(date.today(), end)
        return end_datetime - start_datetime

    def calculate_percentage_per_day(self, records, shifts):
        """Calculates the attendance percentage per day."""
        total_duration_per_day_percentage = {}
        total_duration_per_day = {}

        for record in records:
            day = record.login_time.date()
            total_duration_per_day[day] = total_duration_per_day.get(day, timedelta()) + self.parse_duration_string(record.get_total_duration())

        for day, total_duration in total_duration_per_day.items():
            total_seconds_for_day = sum(self.convert_duration_to_seconds(shift.total_hours) for shift in shifts)
            percentage = (total_duration.total_seconds() / total_seconds_for_day * 100) if total_seconds_for_day > 0 else 0
            total_duration_per_day_percentage[day] = percentage

        return total_duration_per_day_percentage

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        student_id = self.kwargs.get('id')
        student = get_object_or_404(Student, pk=student_id)
        employee_instance = student.mystudent

        if not employee_instance:
            logging.error("No linked CustomUser for the given student.")
            return context

        shifts = shift_names.objects.all()
        for shift in shifts:
            shift.total_hours = self.calculate_total_hours(shift.start_time, shift.end_time)

        records = EmployeeLoginLogout.objects.filter(employee=employee_instance).order_by('login_time')
        total_duration_per_day_percentage = self.calculate_percentage_per_day(records, shifts)

        d = self.get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month, total_duration_per_day_percentage).formatmonth(withyear=True)

        context.update({
            'calendar': mark_safe(cal),
            'prev_month': self.prev_month(d),
            'next_month': self.next_month(d),
            'student': student,
            'employee_instance': employee_instance,
            'shifts': shifts,
            'total_duration_per_day_percentage': total_duration_per_day_percentage,
            'k': MenuItem.objects.filter(parent_category=None)
        })

        return context

    def get_date(self, req_month):
        if req_month:
            year, month = (int(x) for x in req_month.split('-'))
            return date(year, month, day=1)
        return datetime.today()

    def prev_month(self, d):
        first = d.replace(day=1)
        prev_month = first - timedelta(days=1)
        month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
        return month

    def next_month(self, d):
        days_in_month = calendar.monthrange(d.year, d.month)[1]
        last = d.replace(day=days_in_month)
        next_month = last + timedelta(days=1)
        month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
        return month

class Calendar(HTMLCalendar):
    def __init__(self, year=None, month=None, percentages=None):
        self.year = year
        self.month = month
        self.percentages = percentages or {}
        super(Calendar, self).__init__()

    def formatday(self, day, percentages):
        if day == 0:
            return '<td></td>'
        try:
            percentage = percentages[date(self.year, self.month, day)]
            bg_color = 'yellow' if 40 <= percentage < 60 else 'green' if percentage >= 60 else 'red'
            return f"<td style='background-color:{bg_color}'><span class='date'>{day}</span><br></td>"
        except KeyError:
            return f"<td><span class='date'>{day}</span></td>"

    def formatweek(self, theweek):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, self.percentages)
        return f'<tr> {week} </tr>'

    def formatmonth(self, withyear=True):
        cal = f'<table border="2" cellpadding="0" cellspacing="0" class="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week)}\n'
        cal += f'</table>\n'
        return cal

from django.shortcuts import render
from .models import Student, Teachers

def students_view(request):
    # Fetching the menu items for teachers.
    k5 = teachermenu.objects.filter(parent_category=None)

    # Retrieve the logged-in teacher based on the admin field linked to the current user.
    teacher = Teachers.objects.filter(admin=request.user).first()

    # Ensure that the teacher object is found, if not you may want to handle the case where the teacher is not found.
    if not teacher:
        return HttpResponse("Teacher not found.", status=404)

    # Retrieve students that belong to the same school as the logged-in teacher.
    # It's important to check if the teacher has a school assigned.
    if teacher.schoolid:
        students = Student.objects.filter(schoolid=teacher.schoolid)
    else:
        students = Student.objects.none()  # No school associated with this teacher, return empty query.

    return render(request, "students_view.html", {'k': students, 'k5': k5})



from django.shortcuts import render, redirect
from .models import Subject, MenuItem, Schools

def addsubject1(request):
    k = MenuItem.objects.filter(parent_category=None)
    sch = Schools.objects.filter(usernumber=request.user.id).first()
    message = ''

    if request.method == "POST":
        name = request.POST.get('name')
        sub = Subject(name=name, school_id=sch)
        sub.save()
        message = 'Added Subject Successfully.'
        
        return redirect("/manage_sub")
    return render(request, 'addSubject1.html', {'message': message, 'k': k})

def manage_sub(request):
    k = MenuItem.objects.filter(parent_category=None)
    subjects = Subject.objects.all()
    return render(request, "manage_sub.html", {'k': k, 'subjects': subjects})

def sub_delete(request, id):
    subjects = Subject.objects.get(id=id)
    subjects.delete()
    return redirect("/manage_sub")

def subject_edit(request, id):
    subjects = Subject.objects.get(id=id)
    return render(request, "update_subject.html", {'subjects': subjects})

def subject_update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        subjects = Subject.objects.get(id=id)
        subjects.name = name
        subjects.save()
        return redirect("/manage_sub")
    subjects = Subject.objects.get(id=id)
    return render(request, "update_subject.html", {'subjects': subjects})




# from datetime import datetime, timezone
# from django.shortcuts import render
# from django.utils.timezone import make_aware
# from google.oauth2 import service_account
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
# from .models import Meeting1

# from django.http import HttpResponseRedirect
# from urllib.parse import quote

# def create_meeting1(request):
#     if request.method == "POST":
#         title = request.POST.get('title')
#         eventdate = request.POST.get('eventdate')
#         startingtime = request.POST.get('startingtime')
#         endtime = request.POST.get('endtime')
#         event_id=request.POST.get('event_id')
#         event_start = datetime.strptime(f"{eventdate} {startingtime}", "%Y-%m-%d %H:%M")
#         event_end = datetime.strptime(f"{eventdate} {endtime}", "%Y-%m-%d %H:%M")
        
#         SCOPES = ['https://www.googleapis.com/auth/calendar.events']
#         SERVICE_ACCOUNT_FILE = r'C:\Users\Dell\AppData\Local\Programs\Python\Python310\Scripts\meeting_link.json'

#         try:
#             credentials = service_account.Credentials.from_service_account_file(
#                 SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#             service = build('calendar', 'v3', credentials=credentials)

#             meeting_event = {
#                 'summary': title,
#                 'description': 'Meeting description goes here.',  
#                 'start': {
#                     'dateTime': event_start.isoformat(),
#                     'timeZone': 'UTC',
#                 },
#                 'end': {
#                     'dateTime': event_end.isoformat(),
#                     'timeZone': 'UTC',
#                 },
#             }

#             event = service.events().insert(calendarId='primary', body=meeting_event).execute()
#             event_id = event['id']

#             meet_link = f"https://www.google.com/calendar/render?action=TEMPLATE&text={quote(title)}&dates={event_start.isoformat()}%2F{event_end.isoformat()}"

#             return HttpResponseRedirect(meet_link)

#         except HttpError as error:
#             return render(request, 'error.html', {'error': str(error)})

#         except Exception as e:
#             return render(request, 'error.html', {'error': str(e)})

#     return render(request, 'book.html')



# def book(request):
#     current_date = datetime.now().strftime('%Y-%m-%d')
#     return render(request, "book.html", {'current_date': current_date})








from datetime import datetime
from django.shortcuts import render
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from .models import Meeting1
from django.http import HttpResponseRedirect
from urllib.parse import quote
def create_meeting1(request):
    if request.method == "POST":
        title = request.POST.get('title')
        eventdate = request.POST.get('eventdate')
        startingtime = request.POST.get('startingtime')
        endtime = request.POST.get('endtime')
        description = "Meeting description goes here."
        event_start = datetime.strptime(f"{eventdate} {startingtime}", "%Y-%m-%d %H:%M")
        event_end = datetime.strptime(f"{eventdate} {endtime}", "%Y-%m-%d %H:%M")
        SCOPES = ['https://www.googleapis.com/auth/calendar.events']
        SERVICE_ACCOUNT_FILE = r'C:\Users\Dell\AppData\Local\Programs\Python\Python310\Scripts\meeting_link.json'
        try:
            credentials = service_account.Credentials.from_service_account_file(
                SERVICE_ACCOUNT_FILE, scopes=SCOPES)
            service = build('calendar', 'v3', credentials=credentials)
            meeting_event = {
                'summary': title,
                'description': description,
                'start': {
                    'dateTime': event_start.isoformat(),
                    'timeZone': 'UTC',
                },
                'end': {
                    'dateTime': event_end.isoformat(),
                    'timeZone': 'UTC',
                },
            }
            event = service.events().insert(calendarId='primary', body=meeting_event).execute()
            event_id = event['id']
            start_iso = event_start.isoformat().replace(":", "").replace("-", "")
            end_iso = event_end.isoformat().replace(":", "").replace("-", "")
            meet_link = f"https://calendar.google.com/calendar/u/0/r/eventedit?text={quote(title)}&dates={start_iso}/{end_iso}"
            meeting = Meeting1(
                title=title,
                description=description,
                start_time=event_start,
                end_time=event_end,
                meet_link=meet_link
            )
            meeting.save()
            return HttpResponseRedirect(meet_link)
        except HttpError as error:
            return render(request, 'error.html', {'error': str(error)})
        except Exception as e:
            return render(request, 'error.html', {'error': str(e)})
    else:
        current_date = datetime.now().strftime('%Y-%m-%d')
        return render(request, 'book.html', {'current_date': current_date})


def book(request):
    current_date = datetime.now().strftime('%Y-%m-%d')
    return render(request, "book.html", {'current_date': current_date})








def html(request):
    return render(request,"html.html")






