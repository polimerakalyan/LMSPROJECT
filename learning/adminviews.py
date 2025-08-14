import base64
from datetime import timezone
from django.shortcuts import render ,get_object_or_404 , redirect

from lms_main import settings
from lms_main.settings import BASE_DIR 
from . models import *
from django.http import HttpResponse,HttpResponseRedirect, JsonResponse
from django.urls import reverse


# def sidenavbar(request):
   
#     data = Schools.objects.filter(usernumber=request.user.id).first()

#     plans=Teachers.objects.filter(schoolid=data)
#     std=Student.objects.filter(schoolid=data)
#     teacher_count = Teachers.objects.filter(schoolid__usernumber=request.user.id).count()
#     student_count=Student.objects.filter(schoolid__usernumber=request.user.id).count()
  


#     am=admin_main.objects.all()
#     k=MenuItem.objects.filter(parent_category=None)
#     return render(request,'admin-template/adminsidebar.html',{'student_count':student_count,'teacher_count':teacher_count,'std':std,'plans':plans,'k':k,'am':am})

from django.utils import timezone
from django.shortcuts import render

def sidenavbar(request): 
    all_schools = Schools.objects.filter(usernumber=request.user.id).first() 
    pending_leave_count = all_schools.leave_set.filter(is_status=0, read=0).count()
    k1 = all_schools.leave_set.filter(read=0) 
    k2 = all_schools.leave_set.filter(user_type=2, read=0)  
    k4 = all_schools.leave_set.filter(user_type=3, read=0)
    
    k = MenuItem.objects.filter(parent_category=None)
    teachers_count, teaching_staff_count, non_teaching_staff_count = get_teachers_count(request) 
    student_count, classes_count = get_student_class_count(request) 
    current_time = timezone.now()  # Get the current time in UTC

    context = {
        'teachers_count': teachers_count,
        'teaching_staff_count': teaching_staff_count,
        'non_teaching_staff_count': non_teaching_staff_count,
        'k': k,
        'k4': k4,
        'k2': k2,
        "k1": k1,
        'pending_leave_count': pending_leave_count,
        'student_count': student_count,
        'classes_count': classes_count,
        'current_time': current_time,
        'registered_plan': all_schools.plan_id.name if all_schools else None,
    }
    return render(request, 'admin-template/adminsidebar.html', context)





def Leave_Management(request):
    k=MenuItem.objects.filter(parent_category=None)

    j=leavemanagement.objects.all()
    return render(request,'admin-template/Leave Management.html',{'k':k,'j':j})


def Leave_Management2(request):
    k1=leavestype.objects.all()
    k=MenuItem.objects.filter(parent_category=None)

    if request.method=="POST":
        leavetype=request.POST['leavetype']
        Noofleaves=request.POST['Noofleaves']
        leavecategory=request.POST['leavecategory']
        k3=leavestype(leavetype=leavetype,Noofleaves=Noofleaves,leavecategory=leavecategory)
        k3.save()
    return render(request,'admin-template/Leave Management2.html',{'k1':k1,'k':k})



def Leave_type_edit(request,id):
    if request.method=="GET":
        k=MenuItem.objects.filter(parent_category=None)
        k1=leavestype.objects.get(id=id)
        return render(request,"admin-template/Leave_type_update.html",{'k1':k1,'k':k})

def Leave_type_update(request,id):
    if request.method=="POST":
       
        leavetype=request.POST['leavetype']
        Noofleaves= request.POST['Noofleaves']
        leavecategory= request.POST['leavecategory']

    
        k=leavestype.objects.get(id=id)
       
        k.leavetype=leavetype
        k.Noofleaves=Noofleaves
        k.leavecategory=leavecategory
        

        k.save()
        return redirect("/Leave_Management2/")
    return render(request,"admin-template/Leave_type_update.html")


def Leave_type_delete(request,id):
    if request.method=="GET":
        k=leavestype.objects.get(id=id)
        k.delete()
        return redirect("/Leave_Management2/")
    # return render(request,"admin-template/leavedatadelete.html")  

def admin_attendance(request):
    j=Attendancemenu.objects.all()
    k=MenuItem.objects.filter(parent_category=None)

    return render(request,'admin-template/teacher_attendance.html',{'j':j,'k':k})   

def Teacher_leaves_view(request):
    k=MenuItem.objects.filter(parent_category=None)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    p=leave.objects.filter(user_type=2)
    k2=leave.objects.filter(user_type=2,read=0)

    pending_leave_count = leave.objects.filter(is_status=0,user_type=2,read=0).count()

    k3=leavestype.objects.all()
    return render(request,'admin-template/view_teacher_apply_leave.html',{'k2':k2,'p':p,'k':k,'k3':k3,'pending_leave_count':pending_leave_count})     

def Student_leaves_view(request):
    k=MenuItem.objects.filter(parent_category=None)    
    p=leave.objects.filter(user_type=3)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    k4=leave.objects.filter(user_type=3,read=0)
    pending_leave_count = leave.objects.filter(is_status=0,user_type=3,read=0).count()

    k3=leavestype.objects.all()

    # items_per_page = 1 


    # paginator = Paginator(k4, items_per_page)

    # page = request.GET.get('page')

    # try:
    #     k4 = paginator.page(page)
    # except PageNotAnInteger:
    #     k4 = paginator.page(1)
    # except EmptyPage:
    #     k4 = paginator.page(paginator.num_pages)

    return render(request,'admin-template/view_student_apply_leave.html',{'p':p,'k':k,'k3':k3,'k4':k4,'pending_leave_count':pending_leave_count})

def leave_approve(request,id):
    k2=leave.objects.get(id=id)
    k2.is_status=1
    k2.save()
    return HttpResponseRedirect(reverse("Teacher_leaves_view"))

def leave_disapprove(request,id):
    k2=leave.objects.get(id=id)
    k2.is_status=2
    k2.save()

    return HttpResponseRedirect(reverse("Teacher_leaves_view"))


def leave_approve1(request,id):
    k2=leave.objects.get(id=id)
    k2.is_status=1
    k2.save()
    return HttpResponseRedirect(reverse("Student_leaves_view"))

def leave_disapprove1(request,id):
    k2=leave.objects.get(id=id)
    k2.is_status=2
    k2.save()

    return HttpResponseRedirect(reverse("Student_leaves_view"))


def mark_all_as_read(request):
    leave.objects.all().update(read=True)
    return HttpResponseRedirect('/sidenavbar') 

    
    
def mark_as_read(request, leave_id):
    leave_obj = get_object_or_404(leave, id=leave_id)
    leave_obj.read = True
    leave_obj.save()
    return HttpResponseRedirect('/Teacher_leaves_view')
    
def mark_as_read1(request, leave_id):
    leave_obj = get_object_or_404(leave, id=leave_id)
    leave_obj.read = True
    leave_obj.save()
    return HttpResponseRedirect('/Student_leaves_view')     

from .models import teacherattendance
def Teacher_Attendance_display(request):
    k=MenuItem.objects.filter(parent_category=None)

    k1=teacherattendance.objects.all()
    return render(request, "admin-template/Teacher_Attendance_display.html",{'k':k,'k1':k1})


def create_Teacher_shifts(request):

    k4=different_shifts.objects.all()
    k6=Teachers.objects.all()
    if request.method=="POST":
        name=request.POST.get('shift_name')
        weekly_off=request.POST.get('weekly_off')
        in_time=request.POST.get('in_time')
        late_mark_time=request.POST.get('late_mark_time')
        out_time=request.POST.get('out_time')
        half_daytime=request.POST.get('half_daytime')
        first_name=request.POST.get('facult_name')
        shift_instance=get_object_or_404(different_shifts,name=name)
        name_instance=get_object_or_404(Teachers,first_name=first_name)
        k=Teacher_Shifts(shift_name=shift_instance,weekly_off=weekly_off,in_time=in_time,late_mark_time=late_mark_time,out_time=out_time,half_daytime=half_daytime,facult_name=name_instance)
        k.save()
    return render(request, "admin-template/create_Teacher_shifts.html",{'k4':k4,'k6':k6,})
          
              

def create_Teacher_shifts_display(request):
    if request.method=="GET":
        k=Teacher_Shifts.objects.all()
        return render(request,'admin-template/create_Teacher_shifts_display.html',{'k':k})
    

def create_Teacher_shifts_edit(request,id):
    if request.method=="GET":
        k=Teacher_Shifts.objects.get(id=id)
        return render(request,"admin-template/create_Teacher_shifts_edit.html",{'k':k})



def create_Teacher_shifts_update(request,id):
    if request.method=="POST":       
        shift_name=request.POST['shift_name']
        weekly_off= request.POST['weekly_off'] 
        in_time= request.POST.get('in_time')   
        late_mark_time= request.POST.get('late_mark_time')    
        out_time= request.POST.get('out_time')
        half_daytime= request.POST.get('half_daytime')  
        facult_name= request.POST['facult_name']    
        k=Teacher_Shifts.objects.get(id=id)       
        k.shift_name=shift_name
        k.weekly_off=weekly_off
        k.in_time=in_time
        k.late_mark_time=late_mark_time
        k.out_time=out_time
        k.half_daytime=half_daytime
        k.facult_name=facult_name
        k.save()
        return redirect("/create_Teacher_shifts_display/")
    return render(request,"admin-template/create_Teacher_shifts_edit.html")



def create_Teacher_shifts_delete(request,id):
    if request.method=="GET":
        k=Teacher_Shifts.objects.get(id=id)
        k.delete()
        return HttpResponse("data is deleted")
    return render(request,"admin-template/create_Teacher_shifts_delete.html")  

from django.shortcuts import get_object_or_404

from django.shortcuts import get_object_or_404
from django.contrib import messages 

def compose_message12(request):  
    k=MenuItem.objects.filter(parent_category=None) 
    scc=Schools.objects.filter(usernumber=request.user.id).first() 
    k1=Teachers.objects.filter(schoolid=scc) 
    k3=Student.objects.filter(schoolid=scc) 
    k5=Student.objects.filter(student_class=1,schoolid=scc) 
    k6=Student.objects.filter(student_class=2,schoolid=scc) 
    k7=Student.objects.filter(student_class=3,schoolid=scc) 
    k8=Student.objects.filter(student_class=4,schoolid=scc) 
    k9=Student.objects.filter(student_class=5,schoolid=scc) 
    k10=Student.objects.filter(student_class=6,schoolid=scc) 
    k11=Student.objects.filter(student_class=7,schoolid=scc) 
    k12=Student.objects.filter(student_class=8,schoolid=scc) 
    k4=Student.objects.filter(student_class=9,schoolid=scc) 
 
    k13=Student.objects.filter(student_class=10,schoolid=scc) 
    k14=Student.objects.filter(student_class=11,schoolid=scc)  
    k15=Student.objects.filter(student_class=12,schoolid=scc)        
 
    if request.method == "POST":  
        MessageType = request.POST.get('MessageType') 
        Message = request.POST.get('Message')    

        if MessageType and Message:    
            if 'all_teachers' in request.POST: 
                for teacher in k1:              
                   k2 = compose_message(teachername=teacher,schoolid=scc, MessageType=MessageType, Message=Message)
                   k2.save()    


         
            if 'all_students' in request.POST:   
                for student in k3:     
                    k2 = compose_message(studentname=student,schoolid=scc, MessageType=MessageType, Message=Message)
                    k2.save()  


                
                    
            if '1st_class' in request.POST:      
                for student in k5:   
                    k2 = compose_message(studentname=student,schoolid=scc, MessageType=MessageType, Message=Message)
                    k2.save()   
                    


            if '2nd_class' in request.POST:   
                for student in k6:  
                    k2 = compose_message(studentname=student,schoolid=scc, MessageType=MessageType, Message=Message)
                    k2.save()               



            if '3rd_class' in request.POST:   
                for student in k7:  
                    k2 = compose_message(studentname=student,schoolid=scc, MessageType=MessageType, Message=Message)
                    k2.save()   


    
            if '4th_class' in request.POST:   
                for student in k8:  
                    k2 = compose_message(studentname=student,schoolid=scc, MessageType=MessageType, Message=Message)
                    k2.save()   



            if '5th_class' in request.POST:   
                for student in k9:  
                    k2 = compose_message(studentname=student,schoolid=scc, MessageType=MessageType, Message=Message)
                    k2.save()   


        
            if '6th_class' in request.POST:   
                for student in k10:  
                    k2 = compose_message(studentname=student,schoolid=scc, MessageType=MessageType, Message=Message)
                    k2.save()  

            
            if '7th_class' in request.POST:   
                for student in k11:  
                    k2 = compose_message(studentname=student,schoolid=scc, MessageType=MessageType, Message=Message)
                    k2.save() 

            
            if '8th_class' in request.POST:   
                for student in k12:  
                    k2 = compose_message(studentname=student,schoolid=scc, MessageType=MessageType, Message=Message)
                    k2.save()  


            if '9th_class' in request.POST:   
                for student in k4:   
                    k2 = compose_message(studentname=student,schoolid=scc, MessageType=MessageType, Message=Message)
                    k2.save() 
        
            
            if '10th_class' in request.POST:   
                for student in k13:   
                    k2 = compose_message(studentname=student,schoolid=scc, MessageType=MessageType, Message=Message)
                    k2.save()                                            
            

        
            if '11th_class' in request.POST:   
                for student in k14:  
                    k2 = compose_message(studentname=student,schoolid=scc, MessageType=MessageType, Message=Message)
                    k2.save()    

                
        
            if '12th_class' in request.POST:                     
                for student in k15:                                                     
                    k2 = compose_message(studentname=student,schoolid=scc, MessageType=MessageType, Message=Message)
                    k2.save()                                        
            messages.success(request,"Data is inserted for selected categories")
            return redirect('/compose_message12')  
        else:
            messages.error(request," Please Select  the Type Field")                                         
 
        

    return render(request, 'admin-template/composemessage.html', {'k': k, 'k1': k1, 'k3': k3,'k4':k4,'k5':k5,'k6':k6,'k7':k7,'k8':k8,'k9':k9,'k10':k10,'k11':k11,'k12':k12,'k13':k13,'k14':k14,'k15':k15})  





def teachdata(request):
    data = Schools.objects.filter(usernumber=request.user.id).first()
    data1=data.id
    plans=Teachers.objects.filter(schoolid=data1)
    return render(request,'admin-template/teacherdata.html',{'plans':plans})



def teachercount(request):
    k=MenuItem.objects.filter(parent_category=None)  
    sch = Schools.objects.filter(usernumber=request.user.id).first()
    plans = Teachers.objects.filter(schoolid=sch)
    teca=Teacher_Class_sub.objects.all()
    # teacher_class_subs = Teacher_Class_sub.objects.filter(teacher__in=teachers).order_by('teacher__id')
    # grouped_data = []

    # for teacher, entries in groupby(teacher_class_subs, key=attrgetter('teacher')):
    #     entries_by_subject = {}
    #     for entry in entries:
    #         subject_name = entry.subject.name
    #         if subject_name not in entries_by_subject:
    #             entries_by_subject[subject_name] = []
    #         entries_by_subject[subject_name].append(entry)

    #     grouped_data.append({
    #         'teacher': teacher,
    #         'entries_by_subject': entries_by_subject,
    #     })

    return render(request, 'admin-template/count.html',{'plans': plans,'k':k,'teca':teca})



def alldata(request):
    data = Schools.objects.filter(usernumber=request.user.id).first()
    plans=Student.objects.filter(schoolid=data)
    k = MenuItem.objects.filter(parent_category=None)
    return render(request, 'admin-template/all.html', {'plans':plans,'k':k})



# from django.shortcuts import get_object_or_404

# def assign_subjects_classes(request):
#     k=MenuItem.objects.filter(parent_category=None)  
#     sch = Schools.objects.filter(usernumber=request.user.id).first()
#     school_count = Schools.objects.filter(usernumber=request.user.id).count()

#     teachers = Teachers.objects.filter(schoolid=sch)
#     subjects = Subject.objects.filter(school_id=sch)
#     classes = cls_name.objects.filter(school_id=sch)
#     message = ''

#     if request.method == 'POST':
#         teacher_id = request.POST['teacher']
#         subject_id = request.POST['subject']
#         class_ids = request.POST.getlist('classes')

#         teacher = Teachers.objects.get(id=teacher_id)
#         subject = Subject.objects.get(id=subject_id)

#         for class_id in class_ids:
#             class_name = get_object_or_404(cls_name, id=class_id)

#             Teacher_Class_sub.objects.create(
#                 teacher=teacher,
#                 class_name=class_name,
#                 subject=subject,
#                 school_id=sch
#             )
#         message = 'Successfully Submitted.'
#     return render(request, 'admin-template/assign_subjects_classes.html', {'teachers': teachers, 'subjects': subjects, 'classes': classes,'message':message,'k':k,'school_count':school_count})


from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Schools, cls_name, Subject, Teachers, Teacher_Class_sub, MenuItem

def assign_subjects_classes(request):
    k = MenuItem.objects.filter(parent_category=None)
    sch = Schools.objects.filter(usernumber=request.user.id).first()
    school_count = Schools.objects.filter(usernumber=request.user.id).count()

    teachers = Teachers.objects.filter(schoolid=sch)
    classes = cls_name.objects.filter(school_id=sch)
    message = ''

    if request.method == 'POST':
        teacher_id = request.POST['teacher']
        subject_id = request.POST['subject']
        class_ids = request.POST.getlist('classes')

        teacher = Teachers.objects.get(id=teacher_id)
        subject = Subject.objects.get(id=subject_id)

        for class_id in class_ids:
            class_name = get_object_or_404(cls_name, id=class_id)
            Teacher_Class_sub.objects.create(
                teacher=teacher,
                class_name=class_name,
                subject=subject,
                school_id=sch
            )
        message = 'Successfully Submitted.'

    return render(request, 'admin-template/assign_subjects_classes.html', {
        'teachers': teachers,
        'classes': classes,
        'message': message,
        'k': k,
        'school_count': school_count
    })

def get_subjects_for_class(request, class_id):
    subjects = Subject.objects.filter(class_name__id=class_id)
    data = [{'id': subject.id, 'name': subject.name} for subject in subjects]
    return JsonResponse(data, safe=False)

# from django.http import JsonResponse
# from .models import Subject

# def get_subjects_for_class(request, class_id):
#     subjects = Subject.objects.filter(class_name__id=class_id)
#     data = [{'id': subject.id, 'name': subject.name} for subject in subjects]
#     return JsonResponse(data, safe=False)

# views.py
   
from itertools import groupby  
from operator import attrgetter
from django.shortcuts import render
from .models import Teacher_Class_sub, Teachers  

def view_teacher_sub_class(request):
    k=MenuItem.objects.filter(parent_category=None)  
    sch = Schools.objects.filter(usernumber=request.user.id).first()
    teachers = Teachers.objects.filter(schoolid=sch)
    
    teacher_class_subs = Teacher_Class_sub.objects.filter(teacher__in=teachers).order_by('teacher__id')
    grouped_data = []

    for teacher, entries in groupby(teacher_class_subs, key=attrgetter('teacher')):
        entries_by_subject = {}
        for entry in entries:
            subject_name = entry.subject.name
            if subject_name not in entries_by_subject:
                entries_by_subject[subject_name] = []
            entries_by_subject[subject_name].append(entry)

        grouped_data.append({
            'teacher': teacher,
            'entries_by_subject': entries_by_subject,
        })

    return render(request, 'admin-template/view_teacher_sub_class.html',{'grouped_data': grouped_data,'k':k})

# from django.shortcuts import render, redirect
# from .models import Subject, cls_name, Schools

# def addsubject(request):
#     k=MenuItem.objects.filter(parent_category=None)  
#     sch = Schools.objects.filter(usernumber=request.user.id).first()
#     message = ''

#     if request.method == "POST":
#         name = request.POST.get('name')
#         sub = Subject(name=name, school_id=sch)
#         sub.save()
#         message = 'Added Subject Successfully.'
        

#     return render(request, 'admin-template/addSubject.html',{'message':message,'k':k})

# def addclass(request):
#     k=MenuItem.objects.filter(parent_category=None)  
#     school = Schools.objects.filter(usernumber=request.user.id).first()
#     message = ''
#     if request.method == "POST":
#         classes = request.POST.get('classes')
#         if cls_name.objects.filter(classes=classes, school_id=school).exists():
#             message = 'Error: This class already exists.'
#         else:
#             k1 = cls_name(classes=classes)
#             k1.school_id = Schools.objects.filter(usernumber=request.user.id).first()
#             k1.save()
#             message = 'Added Class Successfully.'

#     return render(request, 'admin-template/addClass.html',{'message':message,'k':k}) 


# from django.shortcuts import render, redirect
# from .models import Subject, Schools, cls_name
# from .models import Schools, cls_name, Subject 


# def addsubject(request):
#     k = MenuItem.objects.filter(parent_category=None)  
#     schools = Schools.objects.filter(usernumber=request.user.id).first()
#     classes = cls_name.objects.filter(school_id=schools)
#     message = ''

#     if request.method == "POST":
#         name = request.POST.get('name')
#         selected_class_ids = request.POST.getlist('classes') 

#         if name and selected_class_ids:
#             for class_id in selected_class_ids:
#                 selected_class = cls_name.objects.get(id=class_id)
#                 if Subject.objects.filter(name=name, class_name=selected_class).exists():
#                     message = f'Subject "{name}" is already assigned to class "{selected_class.classes}".'
#                     break  
#             else:
#                 subject = Subject.objects.create(name=name, school_id=schools)
#                 for class_id in selected_class_ids:
#                     selected_class = cls_name.objects.get(id=class_id)
#                     subject.class_name.add(selected_class)  
#                 message = 'Added Subject Successfully.'
#        
#     return render(request, 'admin-template/addSubject.html', {'message': message, 'classes': classes, 'k': k})



# from django.shortcuts import render, redirect
# from .models import Subject, Schools, cls_name
# from .models import Schools, cls_name, Subject 


# def addsubject(request):
#     k = MenuItem.objects.filter(parent_category=None)  
#     schools = Schools.objects.filter(usernumber=request.user.id).first()
#     classes = cls_name.objects.filter(school_id=schools)
#     existing_subjects = Subject.objects.all()  # Retrieve existing subjects
#     message = ''

#     if request.method == "POST":
#         name = request.POST.get('name')
#         selected_class_ids = request.POST.getlist('classes') 

#         if name and selected_class_ids:
#             for class_id in selected_class_ids:
#                 selected_class = cls_name.objects.get(id=class_id)
#                 if Subject.objects.filter(name=name, class_name=selected_class).exists():
#                     message = f'Subject "{name}" is already assigned to class "{selected_class.classes}".'
#                     break  
#             else:
#                 subject = Subject.objects.create(name=name, school_id=schools)
#                 for class_id in selected_class_ids:
#                     selected_class = cls_name.objects.get(id=class_id)
#                     subject.class_name.add(selected_class)  
#                 message = 'Added Subject Successfully.'

#     return render(request, 'admin-template/addSubject.html', {'message': message, 'classes': classes, 'k': k, 'existing_subjects': existing_subjects})



from django.shortcuts import render, redirect
from .models import Schools, cls_name, Subject 


def addsubject(request):
    k = MenuItem.objects.filter(parent_category=None)  
    schools = Schools.objects.filter(usernumber=request.user.id).first()
    classes = cls_name.objects.filter(school_id=schools)
    existing_subjects = Subject.objects.all()  # Retrieve existing subjects
    message = ''

    if request.method == "POST":
        name = request.POST.get('name')
        existing_subject_id = request.POST.get('existing_subject')
        selected_class_ids = request.POST.getlist('classes')

        if not existing_subject_id and (not name or not selected_class_ids):
            message = 'Name and at least one class must be provided.'
        else:
            if name and Subject.objects.filter(name=name, school_id=schools).exists():
                message = f'Subject "{name}" already exists.'
            else:
                if existing_subject_id:
                    subject = Subject.objects.get(id=existing_subject_id)
                else:
                    subject = Subject.objects.create(name=name, school_id=schools)
                
                for class_id in selected_class_ids:
                    selected_class = cls_name.objects.get(id=class_id)
                    subject.class_name.add(selected_class)
                
                message = 'Added Subject Successfully.'

    return render(request, 'admin-template/addSubject.html', {'message': message, 'classes': classes, 'k': k, 'existing_subjects': existing_subjects})


def addclass(request):
    k=MenuItem.objects.filter(parent_category=None)  
    school = Schools.objects.filter(usernumber=request.user.id).first()
    message = ''
    if request.method == "POST":
        classes = request.POST.get('classes')
        if cls_name.objects.filter(classes=classes, school_id=school).exists():
            message = 'Error: This class already exists.'
        else:
            k1 = cls_name(classes=classes)
            k1.school_id = Schools.objects.filter(usernumber=request.user.id).first()
            k1.save()
            message = 'Added Class Successfully.'

    return render(request, 'admin-template/addClass.html',{'message':message,'k':k}) 


def class_wise(request):
    k=MenuItem.objects.filter(parent_category=None)

    second_table_data = Schools.objects.filter(usernumber=request.user.id)
    third_table_data = Student.objects.filter(schoolid__in=second_table_data)
    
    class_1_to_4_students = third_table_data.filter(className__in=['1', '2', '3', '4'])
    class_5_to_8_students = third_table_data.filter(className__in=['5', '6', '7', '8'])
    class_9_to_12_students = third_table_data.filter(className__in=['9', '10', '11', '12'])
    
    count_class_1_to_4 = class_1_to_4_students.count()
    count_class_5_to_8 = class_5_to_8_students.count()
    count_class_9_to_12 = class_9_to_12_students.count()
    
    return render(request, 'admin-template/classes_wise.html', {'k':k,'class_1_to_4_students': class_1_to_4_students,'class_5_to_8_students': class_5_to_8_students,'class_9_to_12_students': class_9_to_12_students,'count_class_1_to_4': count_class_1_to_4,'count_class_5_to_8': count_class_5_to_8,'count_class_9_to_12': count_class_9_to_12})

def classes1to4(request):
    k=MenuItem.objects.filter(parent_category=None)
    second_table_data = Schools.objects.filter(usernumber=request.user.id)
    third_table_data = Student.objects.filter(schoolid__in=second_table_data)
       
    class1students = third_table_data.filter(className__in=['1'])
    class2students = third_table_data.filter(className__in=['2'])
    class3students = third_table_data.filter(className__in=['3'])
    class4students = third_table_data.filter(className__in=['4'])
    count_class1students=class1students.count()
    count_class2students=class2students.count()
    count_class3students=class3students.count()
    count_class4students=class4students.count()
    return render(request, 'admin-template/class1to4.html', {'k':k,'count_class1students':count_class1students,'count_class2students':count_class2students,'count_class3students':count_class3students,'count_class4students':count_class4students})

def class1(request):
    k=MenuItem.objects.filter(parent_category=None)

    second_table_data = Schools.objects.filter(usernumber=request.user.id)
    third_table_data = Student.objects.filter(schoolid__in=second_table_data)
    class1students = third_table_data.filter(className__in=['1'])
    return render(request,'admin-template/class.html',{'class1students':class1students,'k':k})

def class2(request):
    k=MenuItem.objects.filter(parent_category=None)

    second_table_data = Schools.objects.filter(usernumber=request.user.id)
    third_table_data = Student.objects.filter(schoolid__in=second_table_data)
    class2students = third_table_data.filter(className__in=['2'])
    return render(request,'admin-template/class.html',{'class2students':class2students,'k':k})

def class3(request):
    k=MenuItem.objects.filter(parent_category=None)

    second_table_data = Schools.objects.filter(usernumber=request.user.id)
    third_table_data = Student.objects.filter(schoolid__in=second_table_data)
    class3students = third_table_data.filter(className__in=['3'])
    return render(request,'admin-template/class.html',{'class3students':class3students,'k':k})

def class4(request):
    k=MenuItem.objects.filter(parent_category=None)

    second_table_data = Schools.objects.filter(usernumber=request.user.id)
    third_table_data = Student.objects.filter(schoolid__in=second_table_data)
    class4students = third_table_data.filter(className__in=['4'])
    return render(request,'admin-template/class.html',{'class4students':class4students,'k':k})

def classes5to8(request):
    k=MenuItem.objects.filter(parent_category=None)
   
    second_table_data = Schools.objects.filter(usernumber=request.user.id)
    third_table_data = Student.objects.filter(schoolid__in=second_table_data)
   
    class5students = third_table_data.filter(className__in=['5'])
    class6students = third_table_data.filter(className__in=['6'])
    class7students = third_table_data.filter(className__in=['7'])
    class8students = third_table_data.filter(className__in=['8'])
    count_class5students=class5students.count()
    count_class6students=class6students.count()
    count_class7students=class7students.count()
    count_class8students=class8students.count()
    return render(request, 'admin-template/class5to8.html', {'k':k,'count_class5students':count_class5students,'count_class6students':count_class6students,'count_class7students':count_class7students,'count_class8students':count_class8students})

def class5(request):
    k=MenuItem.objects.filter(parent_category=None)
    second_table_data = Schools.objects.filter(usernumber=request.user.id)
    third_table_data = Student.objects.filter(schoolid__in=second_table_data)
    class5students = third_table_data.filter(className__in=['5'])
    return render(request,'admin-template/class.html',{'class5students':class5students,'k':k})

def class6(request):
    k=MenuItem.objects.filter(parent_category=None)

    second_table_data = Schools.objects.filter(usernumber=request.user.id)
    third_table_data = Student.objects.filter(schoolid__in=second_table_data)
    class6students = third_table_data.filter(className__in=['6'])
    return render(request,'admin-template/class.html',{'class6students':class6students,'k':k})

def class7(request):
    k=MenuItem.objects.filter(parent_category=None)

    second_table_data = Schools.objects.filter(usernumber=request.user.id)
    third_table_data = Student.objects.filter(schoolid__in=second_table_data)
    class7students = third_table_data.filter(className__in=['7'])
    return render(request,'admin-template/class.html',{'class7students':class7students,'k':k})

def class8(request):
    k=MenuItem.objects.filter(parent_category=None)

    second_table_data = Schools.objects.filter(usernumber=request.user.id)
    third_table_data = Student.objects.filter(schoolid__in=second_table_data)
    class8students = third_table_data.filter(className__in=['8'])
    return render(request,'admin-template/class.html',{'class8students':class8students,'k':k})
   
        
def classes9to12(request):
    k=MenuItem.objects.filter(parent_category=None)

    
    second_table_data = Schools.objects.filter(usernumber=request.user.id)
    third_table_data = Student.objects.filter(schoolid__in=second_table_data)

    class9students = third_table_data.filter(className__in=['9'])
    class10students = third_table_data.filter(className__in=['10'])
    class11students = third_table_data.filter(className__in=['11'])
    class12students = third_table_data.filter(className__in=['12'])
    count_class9students=class9students.count()
    count_class10students=class10students.count()
    count_class11students=class11students.count()
    count_class12students=class12students.count()
    return render(request, 'admin-template/class9to12.html', {'k':k,'count_class9students':count_class9students,'count_class10students':count_class10students,'count_class11students':count_class11students,'count_class12students':count_class12students})

def class9(request):
    k=MenuItem.objects.filter(parent_category=None)

    second_table_data = Schools.objects.filter(usernumber=request.user.id)
    third_table_data = Student.objects.filter(schoolid__in=second_table_data)
    class9students = third_table_data.filter(className__in=['9'])
    return render(request,'admin-template/class.html',{'class9students':class9students,'k':k})

def class10(request):
    k=MenuItem.objects.filter(parent_category=None)

    second_table_data = Schools.objects.filter(usernumber=request.user.id)
    third_table_data = Student.objects.filter(schoolid__in=second_table_data)
    class10students = third_table_data.filter(className__in=['10'])
    return render(request,'admin-template/class.html',{'class10students':class10students,'k':k})

def class11(request):
    k=MenuItem.objects.filter(parent_category=None)

    second_table_data = Schools.objects.filter(usernumber=request.user.id)
    third_table_data = Student.objects.filter(schoolid__in=second_table_data)
    class11students = third_table_data.filter(className__in=['11'])
    return render(request,'admin-template/class.html',{'class11students':class11students,'k':k})

def class12(request):
    k=MenuItem.objects.filter(parent_category=None)

    second_table_data = Schools.objects.filter(usernumber=request.user.id)
    third_table_data = Student.objects.filter(schoolid__in=second_table_data)
    class12students = third_table_data.filter(className__in=['12'])
    return render(request,'admin-template/class.html',{'class12students':class12students,'k':k})


from django.shortcuts import render
from .models import Teachers
from django.http import HttpResponseRedirect

def staff_management(request):
    k=MenuItem.objects.filter(parent_category=None)
    return render(request,'admin-template/staff_management.html',{'k':k})

def teaching_staff(request):
    k=MenuItem.objects.filter(parent_category=None)
    sch = Schools.objects.filter(usernumber=request.user.id).first()
    plans = Teachers.objects.filter(schoolid=sch,staff_type='Teaching')
    teca=Teacher_Class_sub.objects.all()
    return render(request,'admin-template/Teaching_staff.html',{'plans':plans,'teca':teca,'k':k})

def non_teaching_staff(request):
    k=MenuItem.objects.filter(parent_category=None)
    sch = Schools.objects.filter(usernumber=request.user.id).first()
    t1 = Teachers.objects.filter(schoolid=sch,staff_type='Non-Teaching')
    return render(request,'admin-template/Non_Teaching_Staff.html',{'t1':t1,'k':k})



def get_teachers_count(request):
    sch = Schools.objects.filter(usernumber=request.user.id).first()
    teachers_count = Teachers.objects.filter(schoolid=sch).count()
    teaching_staff_count = Teachers.objects.filter(schoolid=sch, staff_type='Teaching').count()
    non_teaching_staff_count = Teachers.objects.filter(schoolid=sch, staff_type='Non-Teaching').count()
    return teachers_count, teaching_staff_count, non_teaching_staff_count

def get_student_class_count(request):
    sch = Schools.objects.filter(usernumber=request.user.id).first()
    student_count = Student.objects.filter(schoolid=sch).count()
    classes_count = cls_name.objects.filter(school_id=sch).count()
    return student_count,classes_count






from .models import Student 
from django.db.models import IntegerField, ExpressionWrapper
from django.db.models.functions import Length

from django.shortcuts import get_object_or_404 
from django.shortcuts import render, redirect
from .models import Student, cls_name, Schools
from django.contrib import messages

def class_form(request):
    sch = Schools.objects.filter(usernumber=request.user.id).first() 
    k = MenuItem.objects.filter(parent_category=None) 

    if request.method == 'POST':  
        amount = request.POST.get('amount') 
        class_name = request.POST.get('student_class')
        terms = request.POST.get('terms')           
        term1 = request.POST.get('term1')           
        term2 = request.POST.get('term2')           
        term3 = request.POST.get('term3')           

        students_in_class = Student.objects.filter(className__school_id=sch, className__classes=class_name)
    
        for student_obj in students_in_class: 
            student_first_name = student_obj.first_name  
            student_student_class = student_obj.student_class 

            k1 = fee_payment(          
                amount=amount, 
                schoolid=sch,
                student_class=student_obj, 
                terms=terms,
                first_name=student_first_name,
                s_class=student_student_class,
                term1=term1,
                term2=term2,
                term3=term3 
            )   
            k1.save()    

  
        messages.success(request, 'Payment is successful')
        return redirect('class_form')  

    student_classes = cls_name.objects.filter(school_id=sch).order_by('classes')
    return render(request, "admin-template/class_form.html", {'k': k, 'student_classes': student_classes})
              
def Fee_pay(request):
    k = MenuItem.objects.filter(parent_category=None)
    sch = Schools.objects.filter(usernumber=request.user.id).first()

    if request.method == "GET":
        ob = Student.objects.filter(schoolid=sch).values("className").distinct()
        ob1 = fee_payment.objects.all()
        return render(request, "admin-template/Feepayment.html", {'ob': ob, 'k': k, 'ob1': ob1})

    


    
# from django.shortcuts import render
# from .models import Student, fee_payment 

# def Fees_std_details(request, student_class):
#     ob = Student.objects.values("student_class").distinct() 
#     k = MenuItem.objects.filter(parent_category=None)
                       
#     mn = fee_payment.objects.filter(student_class__student_class=student_class)
#     mns= fee_payment.objects.filter(student_class__student_class=student_class).first() 
#     tem=mns.terms 

#     ob1 = fee_payment.objects.all() 
#     st = mn.first()  
#     ter = st.terms if st else None  

#     if request.method == "GET":      
#         md = Student.objects.filter(student_class=student_class)                                                     
#         return render(request, "admin-template/details.html", {'ter': ter,'tem':tem, 'md': md, 'ob': ob, 'k': k, 'mn': mn, 'st': st, 'ob1': ob1})
from .models import Student, fee_payment 
from decimal import Decimal

def Fees_std_details(request, student_class):
    sch = Schools.objects.filter(usernumber=request.user.id).first()
    ob = Student.objects.filter(schoolid=sch).values("student_class").distinct()

    k = MenuItem.objects.filter(parent_category=None)
                       
    # Filter fee_payment objects by both student_class and school_id
    mn = fee_payment.objects.filter(student_class__student_class=student_class, student_class__schoolid=sch)
    mns = mn.first()  
    tem = mns.terms if mns else None  

    ob1 = fee_payment.objects.all() 
    st = mn.first()  
    ter = st.terms if st else None  
    
    if request.method == "GET":      
        
        md = Student.objects.filter(student_class=student_class, schoolid=sch)
        
        # Calculate the balance for each fee payment
        for payment in mn:
            payment.balance = Decimal(payment.amount) - Decimal(payment.amountpaid)
            payment.save()
                                                  
        return render(request, "admin-template/details.html", {'ter': ter, 'tem': tem, 'md': md, 'ob': ob, 'k': k, 'mn': mn, 'st': st, 'ob1': ob1})



from django.shortcuts import render 
from .models import fee_payment 

def class_form1(request):
    k = MenuItem.objects.filter(parent_category=None)    


    payments = fee_payment.objects.select_related('student_class', 'schoolid').all() 

    return render(request, "admin-template/fee_payment_table.html", {'k': k, 'payments': payments}) 



from django.shortcuts import render, get_object_or_404, redirect 
from .models import fee_payment, Student 

def update_fee_payment(request, payment_id):
    payment = get_object_or_404(fee_payment, id=payment_id) 

    if request.method == 'POST': 
        payment.amount = request.POST.get('amount') 
        payment.terms = request.POST.get('terms')
        payment.save()   

        return redirect('class_form1')  

    return render(request, 'admin-template/update_fee_payment.html', {'payment': payment})





def delete_fee_payment(request, payment_id):                
    payment = get_object_or_404(fee_payment, id=payment_id) 

    if request.method == 'POST':                           
        payment.delete()              

        return redirect('class_form1') 
    

from django.shortcuts import render, redirect
from django.http import JsonResponse
from datetime import datetime
from .models import Schools, cls_name, Subject, Teacher_Class_sub, Teachers, ZoomMeeting

def create_meeting(request):
    school = Schools.objects.filter(usernumber=request.user.id).first()

    class_levels = cls_name.objects.filter(school_id=school)
    subjects = Subject.objects.filter(school_id=school)

    teachers = []  

    if request.method == 'POST':
        class_level_id = request.POST.get('class_level')
        subject_id = request.POST.get('subject')

        if class_level_id and subject_id:
            teacher_class_subs = Teacher_Class_sub.objects.filter(
                class_name_id=class_level_id,
                subject_id=subject_id,
                school_id=school.id
            )

            teacher_ids = teacher_class_subs.values_list('teacher_id', flat=True)

            teachers = Teachers.objects.filter(id__in=teacher_ids)

            selected_teacher_id = request.POST.get('teacher')
            meeting_date = request.POST.get('meeting_date')
            starttime = request.POST.get('starttime')
            endtime = request.POST.get('endtime')
            meeting_link = request.POST.get('meeting_link')  

            try:
                start_datetime = datetime.combine(datetime.strptime(meeting_date, '%Y-%m-%d').date(),
                                                  datetime.strptime(starttime, '%H:%M').time())
                end_datetime = datetime.combine(datetime.strptime(meeting_date, '%Y-%m-%d').date(),
                                                datetime.strptime(endtime, '%H:%M').time())

                if end_datetime <= start_datetime:
                    error_message = "End time must be after start time."
                elif not meeting_link:
                    error_message = "Meeting link is required."
                elif not selected_teacher_id:
                    error_message = "Please select a teacher."
                else:
                    meeting = ZoomMeeting.objects.create(
                        school=school,
                        class_name_id=class_level_id,
                        subject_name_id=subject_id,
                        Teacher_name_id=selected_teacher_id,
                        meeting_date=meeting_date,
                        starttime=starttime,
                        endtime=endtime,
                        meeting_link=meeting_link,
                    )
                    meeting.save()
                    return redirect('meeting_list1')
            except ValueError:
                error_message = "Invalid date or time format."
        else:
            error_message = "Please select both class and subject."
    else:
        error_message = None

    context = {
        'school': school,
        'class_levels': class_levels,
        'subjects': subjects,
        'teachers': teachers,
        'error_message': error_message,
    }

    if request.GET.get('class_level') and request.GET.get('subject'):
        class_level_id = request.GET.get('class_level')
        subject_id = request.GET.get('subject')

        teacher_class_subs = Teacher_Class_sub.objects.filter(
            class_name_id=class_level_id,
            subject_id=subject_id
        ).values('teacher_id')
        teacher_ids = teacher_class_subs.values_list('teacher_id', flat=True)
        teachers = Teachers.objects.filter(id__in=teacher_ids).values('id', 'first_name', 'last_name')

        return JsonResponse({'teachers': list(teachers)})
    else:
        return render(request, 'admin-template/meetings.html', context)

from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, ZoomMeeting
from django.shortcuts import render, redirect
from .models import Schools, cls_name, Subject, Teachers, ZoomMeeting

def meeting_list1(request):
    # Retrieve the school associated with the current user
    school = Schools.objects.filter(usernumber=request.user.id).first()
    
    if school:
        # If school is found, retrieve meetings associated with that school
        meetings = ZoomMeeting.objects.filter(school=school)
    else:
        # If school is not found, return an empty queryset
        meetings = ZoomMeeting.objects.none()

    context = {
        'meetings': meetings,
    }

    return render(request, 'admin-template/meeting_list1.html', context)



