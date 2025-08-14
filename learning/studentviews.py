from django.shortcuts import render ,get_object_or_404 ,redirect 
from . models import *

from datetime import datetime, timedelta
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render

def student_sidebar(request):

    login=Student.objects.get(mystudent=request.user.id)  

    k5=compose_message.objects.filter(studentname=login)  

    k4=leave.objects.filter(admin=request.user.id,read1=0)   

    leave_count = leave.objects.filter(admin=request.user.id,read1=0).count() 
    k = studentnav.objects.filter(parent_category=None)                                    
    
    k1=compose_message.objects.filter(studentname=login,read1=0)  


    k7=compose_message.objects.filter(studentname=login,read1=0)    

    message_count = compose_message.objects.filter(studentname=login,read1=0).count() 

    total_count=  leave_count+ message_count; 

    current_time = timezone.now()  # Get the current time in UTC


    
    return render(request,'student-template/student_sidebar.html',{'k':k,'k4':k4,'leave_count':leave_count,'k5':k5,'k1':k1,'k7':k7,'message_count':message_count,'total_count':total_count,'current_time':current_time})

    
def student_applyforleave(request):
    k2=leave.objects.filter(admin=request.user.id)
    # k2=leave.objects.all()
    k = studentnav.objects.filter(parent_category=None)

    k1=leavestype.objects.all()
    adminid=CustomUser.objects.get(id=request.user.id)
    pending_leave_count = leave.objects.filter(is_status=0,admin=request.user.id).count()
    approved_leave_count = leave.objects.filter(is_status=1,admin=request.user.id).count()
    disapproved_leave_count = leave.objects.filter(is_status=2,admin=request.user.id).count()

    if request.method == "POST":
        Leave_Type=request.POST.getlist('Leave_Type')
        Reason=request.POST.get('Reason')
        from_date_str = request.POST.get('from_date')
        to_date_str = request.POST.get('to_date')

        from_date = datetime.strptime(from_date_str, '%Y-%m-%dT%H:%M')
        to_date = datetime.strptime(to_date_str, '%Y-%m-%dT%H:%M')

        days_difference = (to_date - from_date).days

        for Leave_Type, from_date_str, to_date_str in zip(Leave_Type, from_date_str,to_date_str):
            if Leave_Type and from_date_str and to_date_str:
                Leave_instance = leavestype.objects.get(id=Leave_Type)
                k3=leave(Leave_Type=Leave_instance,Reason=Reason,from_date=from_date,to_date=to_date,admin=adminid,user_type=3,days_difference=days_difference)
                k3.save()

    return render(request,'student-template/student_apply_leave.html',{'k':k,'k1':k1,'k2':k2,'pending_leave_count':pending_leave_count,'approved_leave_count':approved_leave_count,'disapproved_leave_count':disapproved_leave_count})

def mark_all_as_read2(request):
    leave.objects.filter(admin=request.user.id).update(read1=True)
    return HttpResponseRedirect('/student_sidebar') 
    
def student_mark_as_read(request, leave_id):
    leave_obj = get_object_or_404(leave, id=leave_id)
    leave_obj.read1 = True
    leave_obj.save()
    return HttpResponseRedirect('/student_sidebar')




from .models import teachermenu
def student_showmessage(request):
    # login=Teachers.objects.get(admin=request.user.id)
    # k2=compose_message.objects.filter(teachername=login)
    # leave_count = compose_message.objects.count()

    k=studentnav.objects.filter(parent_category=None)
    k2=compose_message.objects.filter(studentname__mystudent=request.user.id)
    for message in k2:
        if message.MessageType == "0":
            message.ShortMessage = message.Message
        if message.MessageType == "1":
            message.ShortMessage = message.Message
        if message.MessageType == "2":
            message.ShortMessage = message.Message
        if message.MessageType == "3":
            message.ShortMessage = message.Message 
    




    return render(request,'student-template/student_showmessage.html',{'k2':k2,'k':k})

def student_all_messages_as_read(request):   
    login=Student.objects.get(mystudent=request.user.id)
                                
    compose_message.objects.filter(studentname=login).update(read1=True)
    return HttpResponseRedirect('/student_sidebar')
def student_messages_mark_as_read(request, compose_message_id):
    compose_message_obj = get_object_or_404(compose_message, id=compose_message_id)
    compose_message_obj.read1 = True
    compose_message_obj.save()
    return HttpResponseRedirect('/student_showmessage')   

def general_instructions(request):
    k=studentnav.objects.filter(parent_category=None)
    p=instruction_headings.objects.all()
    q=instructions11.objects.all()
    return render(request,"student-template/general_instructions.html",{'k':k,'p':p,'q':q})

def quiz_subjects(request):
    current_student = Student.objects.get(mystudent=request.user)
    qu = Teacher_Class_sub.objects.filter(class_name=current_student.class_name,is_correct=1,school_id=current_student.schoolid)
    return render(request, 'student-template/quiz_subjects.html', {'qu': qu})


def std_quiz(request):
    k = studentnav.objects.filter(parent_category=None)
    current_student = Student.objects.get(mystudent=request.user)
    # ob = Teacher_Class_sub.objects.filter(class_name=current_student.className)
    ob= Teacher_Class_sub.objects.filter(class_name=current_student.className,is_control=1,school_id=current_student.schoolid)

    return render(request, "student-template/ssu.html", {'ob': ob,'k':k})


def std_quiz1(request,subject):
    k = studentnav.objects.filter(parent_category=None)
    current_student = Student.objects.get(mystudent=request.user)
    obb = quiz_questions.objects.filter(class_name=current_student.className,subject_id=subject)
    mn=set_timer.objects.filter(class_name=current_student.className,subject_id=subject)
   
    if request.method == "POST":
        try:
            for question in obb:
                answer = request.POST.get('answer{}'.format(question.id))
                result = std_result(questionstd=question.question, answer=answer,student=current_student,classes=current_student.className,subject_id_id=subject)
                result.save()
            return HttpResponse('Submited Successfully..!!')
        except Exception as e:
            return HttpResponse(f'Error: {str(e)}')
    return render(request, "student-template/ssu1.html", {'obb': obb,'k':k,'mn':mn}) 
    


def studentfeepay_form(request):
   k = studentnav.objects.filter(parent_category=None) 
   sch = Student.objects.filter(mystudent=request.user.id).first() 
   fee_payments = fee_payment.objects.filter(student_class=sch)
    
   # Calculate balance for each fee payment
   for payment in fee_payments:
       # Convert empty strings to 0
       term1 = float(payment.term1) if payment.term1 else 0
       term2 = float(payment.term2) if payment.term2 else 0
       term3 = float(payment.term3) if payment.term3 else 0
        # Perform calculations
       total_paid = round(term1 + term2 + term3)
       remaining_balance = int(total_paid)
       
       # If the remaining balance for term 3 is less than 1, set it to 0
       if remaining_balance < 1:
           remaining_balance = 0

       payment.balance = remaining_balance
    
   return render(request, "student-template/studentfeepay_form.html", {'k': k, 'fee_payments': fee_payments})
    


def studentpayfee_edit(request,id):
    k = studentnav.objects.filter(parent_category=None) 
    if request.method=="GET":
        u=fee_payment.objects.get(id=id)
        return render(request,"student-template/studentfee_update.html",{'u':u,'k':k}) 





from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone  # Import timezone module
from .models import fee_payment, studentnav
from .models import Student

def studentpayfee_update(request, id):
    k = studentnav.objects.filter(parent_category=None)
    sch = Student.objects.filter(mystudent=request.user.id).first()

    if request.method == "POST":
        form_data = request.POST
        term1 = float(form_data.get('term1', 0))
        term2 = float(form_data.get('term2', 0))
        term3 = float(form_data.get('term3', 0))
        amountpaid = float(form_data.get('amountpaid', 0))

        # Retrieve the fee payment object
        u = get_object_or_404(fee_payment, id=id)

        original_term1 = u.term1
        original_term2 = u.term2
        original_term3 = u.term3

        # Update the terms based on the amount paid
        remaining_amount = amountpaid

        if remaining_amount >= term1:
            remaining_amount -= term1
            term1 = 0
        else:
            term1 -= remaining_amount
            remaining_amount = 0

        if remaining_amount >= term2:
            remaining_amount -= term2
            term2 = 0
        else:
            term2 -= remaining_amount
            remaining_amount = 0

        term3 -= remaining_amount

        # Update the fee payment object with the new term values
        u.term1 = term1
        u.term2 = term2
        u.term3 = term3

        # Convert u.amountpaid to Decimal if it's a string
        if isinstance(u.amountpaid, str):
            u.amountpaid = float(u.amountpaid)

        # Update the amount paid
        u.amountpaid += amountpaid

        # Update payment date to current time
        u.transaction_datetime = timezone.now()

        u.save(update_fields=['term1', 'term2', 'term3', 'amountpaid', 'transaction_datetime'])

        return redirect("studentfeepay_form")

    return render(request, 'studentfee_update.html')  # render requires the request object and template name