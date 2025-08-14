from .models import *


def adminprofilepiic(request):
        adminimge=adminphoto.objects.first()
        return{'adminimge':adminimge}


def notify(request):
        k1=leave.objects.filter(read=0)
        k2=leave.objects.filter(user_type=2,read=0)
        k4=leave.objects.filter(user_type=3,read=0)
        pending_leave_count = leave.objects.filter(is_status=0,read=0).count()
        return{'pending_leave_count':pending_leave_count,'k1':k1,'k2':k2,'k4':k4}







