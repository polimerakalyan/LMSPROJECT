from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.from django.contrib.auth.models import AbstractUser
from django.db import models

from django.db import models
from django.utils import timezone
class shift_names(models.Model):
    name=models.CharField(max_length=100)
    start_time=models.TimeField(default=datetime.now)
    end_time=models.TimeField(default=datetime.now)
class CustomUser(AbstractUser):
    user_type_data = ((1, "HOD"), (2, "Teachers"), (3, "Student"))
    user_type = models.CharField(default=1, choices=user_type_data, max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    shift = models.ForeignKey(shift_names, on_delete=models.CASCADE, blank=True, null=True)
    def save_login_record(self):
    
        login_record = EmployeeLoginLogout(employee=self, login_time=datetime.now,shift=self.shift)
        login_record.save()

    def save_logout_record(self):
        latest_login_record = EmployeeLoginLogout.objects.filter(employee=self).latest('login_time')
        latest_login_record.logout_time = datetime.now
        latest_login_record.save()

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class OAuthCredentials(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE,default='')
    token = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=255)
    token_uri = models.CharField(max_length=255)
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)


    @classmethod
    def from_authorized_user_info(cls, user_info):
        return cls.objects.create(
            token=user_info['token'],
            refresh_token=user_info['refresh_token'],
            token_uri=user_info['token_uri'],
            client_id=user_info['client_id'],
            client_secret=user_info['client_secret']
        )
class EmployeeLoginLogout(models.Model):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shift = models.ForeignKey(shift_names, on_delete=models.CASCADE)
    login_time = models.DateTimeField(default=datetime.now)
    logout_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.login_time}"

    def get_total_duration(self):
        if self.logout_time:
            duration = self.logout_time - self.login_time
            seconds = duration.total_seconds()
            hours, remainder = divmod(seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"
        else:
            return None


class PricingPlan(models.Model):
    name = models.CharField(max_length=100)
    price_monthly = models.DecimalField(max_digits=10, decimal_places=2)
    price_yearly = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name  


    
class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()

class Schools(models.Model):
    
    organizationname = models.CharField(max_length=100)
    registrationno = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    first_name=models.CharField(max_length=100,default="")
    last_name=models.CharField(max_length=100,default="")

    email = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='images/')  # Make sure to create a 'images' folder in your MEDIA_ROOT
    phoneno = models.BigIntegerField()
    strength = models.CharField(max_length=100,default="")
    password = models.CharField(max_length=100, default="")
    confirm_password=models.CharField(max_length=100,default="")
    usernumber = models.OneToOneField(CustomUser, on_delete=models.CASCADE,blank=True, null=True,)
    plan_id=models.ForeignKey(PricingPlan, on_delete=models.CASCADE, blank=True, null=True)



class meta:
    db_table="Schools"

class Class(models.Model):
    name = models.CharField(max_length=120)
    school_id=models.ForeignKey(Schools,on_delete=models.CASCADE , blank=True, null=True,)
    
    

class cls_name(models.Model):
    school_id=models.ForeignKey(Schools,on_delete=models.CASCADE , blank=True, null=True,)
    classes = models.CharField(max_length=200)
    
    def __str__(self):
        return self.classes   
        
# class Student(models.Model):
#     GENDER_CHOICES = [
#         ('male', 'Male'),
#         ('female', 'Female'),
#         ('other', 'Other'),
#     ]
#     username = models.CharField(max_length=255,default="")
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#     confirm_password = models.CharField(max_length=255)
#     registration_date = models.DateField()
#     student_class = models.CharField(max_length=20,default='')
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
#     mobile_number = models.CharField(max_length=10)
#     parents_name = models.CharField(max_length=255)
#     parents_mobile_number = models.CharField(max_length=10)
#     date_of_birth = models.DateField()
#     address = models.TextField()
#     mystudent=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True, null=True)
#     schoolid=models.ForeignKey(Schools,on_delete=models.CASCADE,blank=True, null=True)
#     className=models.ForeignKey(cls_name,on_delete=models.CASCADE,blank=True, null=True)
#     shift=models.ForeignKey(shift_names,on_delete=models.CASCADE,blank=True, null=True)



#     class Meta:
#         db_table = 'Student'



from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    username = models.CharField(max_length=255,default="")
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    registration_date = models.DateField()
    student_class = models.CharField(max_length=20,default='')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    mobile_number = models.CharField(max_length=10)
    parents_name = models.CharField(max_length=255)
    parents_mobile_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    address = models.TextField()
    mystudent = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    schoolid = models.ForeignKey(Schools, on_delete=models.CASCADE, blank=True, null=True)
    className = models.ForeignKey(cls_name, on_delete=models.SET_NULL, null=True, blank=True)
    shift = models.ForeignKey(shift_names, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'Student'


class HomeNav(models.Model):
    nav_name = models.CharField(max_length=200, db_index=True)
    nav_url=models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    
 
    class Meta:
        ordering = ['order']
        db_table="learnapp_homenav"
    
    def __str__(self):
        return self.nav_name

# Create your models here.

 

class different_shifts(models.Model):
    name=models.CharField(max_length=500)



class Teachers(models.Model):
    admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE , blank=True, null=True,)
    organizationname = models.CharField(max_length=100)
    registrationno = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    first_name=models.CharField(max_length=100,default="")
    last_name=models.CharField(max_length=100,default="")
    experiance=models.CharField(max_length=100,default="")
    gender = models.CharField(max_length=100,default="")
    designation=models.CharField(max_length=100,default='')
    department=models.CharField(max_length=100,default='')
    dob=models.DateField(default=datetime.now)
    qualification=models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100)
    phoneno = models.CharField(max_length=100,default='')
    password = models.CharField(max_length=100, default="")
    confirm_password=models.CharField(max_length=100,default="")
    course1=models.CharField(max_length=100,default="")
    subject1=models.CharField(max_length=100,default="")
    shift_name=models.ForeignKey(different_shifts,on_delete=models.CASCADE,default="")
    schoolid=models.ForeignKey(Schools,on_delete=models.CASCADE,blank=True, null=True,)
    photo=models.ImageField(upload_to="images/",default=None)
    staff_type=models.CharField(max_length=100,default='')


    class meta:
        db_table="Teachers" 




class Teacher_Shifts(models.Model):
    shift_name=models.ForeignKey(different_shifts,on_delete=models.CASCADE , blank=True, null=True)
    weekly_off=models.CharField(max_length=100)
    in_time=models.TimeField(datetime.now)
    late_mark_time=models.TimeField(datetime.now)
    out_time=models.TimeField(datetime.now)
    half_daytime=models.TimeField(datetime.now)
    facult_name=models.ForeignKey(Teachers,on_delete=models.CASCADE , blank=True, null=True)


# @receiver(post_save,sender=CustomUser)
# def create_user_profile(sender,instance,created,**kwargs):
#     if created:
#         if instance.user_type==1:
#             AdminHOD.objects.create(admin=instance)
#         if instance.user_type==2:
#             Staffs.objects.create(admin=instance,address="")
#         if instance.user_type==3:
#             Students.objects.create(admin=instance,address="",profile_pic="",gender="")

# @receiver(post_save,sender=CustomUser)
# def save_user_profile(sender,instance,**kwargs):
#     if instance.user_type==1:
#         instance.adminhod.save()
#     if instance.user_type==2:
#         instance.staffs.save()
#     if instance.user_type==3:
#         instance.students.save()



class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    icon = models.CharField(max_length=100,default="")
    parent_category = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)


# class Student(models.Model):
#     GENDER_CHOICES = [
#         ('male', 'Male'),
#         ('female', 'Female'),
#         ('other', 'Other'),
#     ]
#     username=models.CharField(max_length=224,default='')
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#     confirm_password = models.CharField(max_length=255)
#     registration_date = models.DateField()
#     student_class = models.CharField(max_length=20)
#     gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
#     mobile_number = models.CharField(max_length=10)
#     parents_name = models.CharField(max_length=255)
#     parents_mobile_number = models.CharField(max_length=10)
#     date_of_birth = models.DateField()
#     address = models.TextField()
#     mystudent=models.ForeignKey(CustomUser,on_delete=models.CASCADE,blank=True,null=True)

#     class Meta:
#         db_table = 'Student'

class lms(models.Model):
    image1=models.ImageField(upload_to="images/")
    image2=models.ImageField(upload_to="images/")
    image3=models.ImageField(upload_to="images/")
    image4=models.ImageField(upload_to="images/")
    image5=models.ImageField(upload_to="images/")
    
    class Meta:
        db_table="lms"



# class Teachers(models.Model):
#     admin=models.OneToOneField(CustomUser,on_delete=models.CASCADE , blank=True, null=True,)

#     organizationname = models.CharField(max_length=100)
#     registrationno = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)
#     username = models.CharField(max_length=100)
#     first_name=models.CharField(max_length=100,default="")
#     last_name=models.CharField(max_length=100,default="")
#     experiance=models.CharField(max_length=100,default="")
#     gender = models.CharField(max_length=100,default="")
#     designation=models.CharField(max_length=100,default='')
#     department=models.CharField(max_length=100,default='')
#     qualification=models.CharField(max_length=100,default='')
#     email = models.CharField(max_length=100)
#     image1 = models.ImageField(upload_to='images/',default='')  # Make sure to create a 'images' folder in your MEDIA_ROOT
#     phoneno = models.CharField(max_length=100,default='')
#     password = models.CharField(max_length=100, default="")
#     confirm_password=models.CharField(max_length=100,default="")
#     course1=models.CharField(max_length=100,default="")
#     subject1=models.CharField(max_length=100,default="")



#     class meta:
#         db_table="Teachers" 

class Subject(models.Model):
    school_id = models.ForeignKey(Schools, on_delete=models.CASCADE, blank=True, null=True)
    class_name = models.ManyToManyField(cls_name, related_name='subjects')
    name = models.CharField(max_length=120)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
  
    
 
    
    
class Teacher_Class_sub(models.Model):
    teacher = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    class_name = models.ForeignKey(cls_name, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    school_id=models.ForeignKey(Schools,on_delete=models.CASCADE , blank=True, null=True,)
    is_control=models.BooleanField(default=False)

class Course(models.Model):
    name = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        
class teachersidebar(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    icon = models.CharField(max_length=100,default="")
    parent_category = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)


class UploadedFile(models.Model):
    file = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    subjectname=models.CharField(max_length=100,default="")
    chapter_no=models.CharField(max_length=100,default="")
    parent_category = models.ForeignKey('self', related_name='subdrop', blank=True, null=True, on_delete=models.CASCADE)
    urls=models.CharField(max_length=100,default="")
    def __str__(self):
        return self.subjectname

class admindrop(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    icon = models.CharField(max_length=100,default="")
    parent_category = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)



from django.db import models

# Create your models here.
class stdclass(models.Model):
    subjects=models.CharField(max_length=100)
    intro=models.CharField(max_length=100)
    description=models.TextField()
    subid=models.CharField(max_length=200)
    chaptername=models.CharField(max_length=100)
    chapterdis=models.TextField(default=None)
    pdf=models.FileField(upload_to='pdf_files/',default=None)
    classes=models.CharField(max_length=100,default=None)
    classid=models.CharField(max_length=200,default=None)
    
class Meta:
    db_table="stdclass"



class topics(models.Model):
    title=models.CharField(max_length=100)
    subtitle=models.CharField(max_length=100)
    content=models.TextField()
    subject1=models.TextField()
    subject2=models.TextField()
    subject3=models.TextField()
    subject4=models.TextField()
    subject5=models.TextField()
    subject6=models.TextField()
    subject7=models.TextField()
    subject8=models.TextField()
    subject9=models.TextField()
    subject10=models.TextField()
    subject11=models.TextField()
    subject12=models.TextField()
    subject13=models.TextField()
    subject14=models.TextField()
    subject15=models.TextField()
class Meta:
    db_table="topics"


class stdclass1(models.Model):
    subjects=models.CharField(max_length=100)
    intro=models.CharField(max_length=100)
    description=models.TextField()
    subid=models.IntegerField()
    chaptername=models.CharField(max_length=100)
    chapterdis=models.TextField(default=None)
    pdf=models.FileField(upload_to='pdf_files/',default=None)
    classes=models.CharField(max_length=100,default=None)
    classid=models.IntegerField(default=None)
    
class Meta:
    db_table="stdclass1"


class logo(models.Model):
    image1 = models.ImageField(upload_to='images/')
class Meta:
    db_table="logo"



class t_table(models.Model):
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    period_time = models.PositiveIntegerField() #minutes
    reces_break1 = models.PositiveIntegerField()
    reces_break2 = models.PositiveIntegerField(default=None)
    lunch_break = models.PositiveIntegerField()
    w_break1=models.IntegerField(default=None)
    w_break2=models.IntegerField(default=None)
    w_lunch=models.IntegerField(default=None)
class Meta:
    db_table = "t_table"


class studentnav(models.Model):
    nav_name = models.CharField(max_length=200, db_index=True)
    nav_url=models.CharField(max_length=100)
    icon = models.CharField(max_length=100,default="")
    parent_category = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    
 
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.nav_name


class applogo(models.Model):
    logo=models.ImageField(upload_to="images/")

    class meta:
        db_table="applogo"

class  examcont(models.Model):
    images=models.ImageField(upload_to="images/")
    heading=models.CharField(max_length=100)
    content=models.TextField(default="")
    image1=models.ImageField(upload_to="images/",default=None)
    heading1=models.TextField(default=None)
    content1=models.TextField(default=None)
class Meta:
    db_table="examcont"

class examcarl(models.Model):
    images=models.ImageField(upload_to="images/")
class Meta:
    db_table="examcarl" 


class examcards(models.Model):
    images=models.ImageField(upload_to="images/")
    field=models.TextField()
class Meta:
    db_table="examcards"

class fee(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    photo=models.ImageField(upload_to="images/")
    title1=models.CharField(max_length=100,default=None)
    content1=models.TextField(default=None)
    photo1=models.ImageField(upload_to="images/",default=None)
    title2=models.CharField(max_length=100,default="")
    content2=models.TextField(default="")
    photo2=models.ImageField(upload_to="images/",default="")
    title3=models.CharField(max_length=100,default="")
    content3=models.TextField(default="")
    photo3=models.ImageField(upload_to="images/",default="")
    
class Meta:
    db_table="fee"


class crfee(models.Model):
    image=models.ImageField(upload_to="images/",default=None)
class Meta:
    db_table="crfee"    
    
    
class cardfee(models.Model):
    cardtitle=models.CharField(max_length=100,default=None)
    cardcontent=models.TextField(default=None)
    cardphoto=models.ImageField(upload_to="images/",default=None)
class Meta:
    db_table="cardfee"


class staff(models.Model):
    heading=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    # discription=models.CharField(max_length=500)
class Meta:
    db_table="staff"
    
class staff_fea(models.Model):
    heading=models.CharField(max_length=100)
    paragraph2=models.CharField(max_length=600)
    # image=models.ImageField(upload_to='images/')
    discription=models.CharField(max_length=100)
    p1=models.CharField(max_length=400)
    # paragraph3=models.CharField(max_length=400)
class Meta:
    db_table="staff_fea"

class staff_imp(models.Model):
    main_heading=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    paragraph1=models.CharField(max_length=400)
    main_heading1=models.CharField(max_length=100,default=None)
    image2=models.ImageField(upload_to="images/",default=None)
    paragraph2=models.CharField(max_length=400)

class Meta:
    db_table="staff_ben"
    
class staff_prob(models.Model):
    heading=models.CharField(max_length=100)
    discription=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/",default=None)
class Meta:
    db_table="staff_fea"

class attendmanagecontent(models.Model):
    image1=models.ImageField(upload_to="images/")
    heading=models.TextField()
    content=models.TextField()
    image2=models.ImageField(upload_to="images/",default=None)
    heading1=models.TextField(default=None)
    content1=models.TextField(default=None)
class Meta:
    db_table="attendmanagecontent"
    
class attendmanagecarousel(models.Model):
    image2=models.ImageField(upload_to="images/")
class Meta:
    db_table="attendmanagecarousel"

class attendmanagecards(models.Model):
    image3=models.ImageField(upload_to="images/")
    field=models.TextField()
class Meta:
    db_table="attendmanagecards"

class paymentfeatures(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    photo=models.ImageField(upload_to="images/")
    title1=models.CharField(max_length=100,default=None)
    content1=models.TextField(default=None)
    photo1=models.ImageField(upload_to="images/",default=None)
    
class Meta:
    db_table="paymentfeatures"


class crpaymentfeatures(models.Model):
    image=models.ImageField(upload_to="images/",default=None)
class Meta:
    db_table="crpaymentfeatures"    
    
    
class cardpaymentfeatures(models.Model):
    cardtitle=models.CharField(max_length=100,default=None)
    cardcontent=models.TextField(default=None)
    cardphoto=models.ImageField(upload_to="images/",default=None)
class Meta:
    db_table="cardpaymentfeatures"

class admissioncarl(models.Model):
    images=models.ImageField(upload_to="images/")
    content=models.TextField()
  
class Meta:
    db_table="admissioncarl"


class admissioncont(models.Model):
    images=models.ImageField(upload_to="images/")
    heading=models.CharField(max_length=100)
    content=models.TextField()
    images1=models.ImageField(upload_to="images/",default=None)
    heading1=models.TextField(default=None)
    content1=models.TextField(default=None)
class Meta:
    db_table="admissioncont"


class admissioncards(models.Model):
    images=models.ImageField(upload_to="images/")
    heading=models.CharField(max_length=100)
    content=models.TextField()

class Meta:
    db_table="admissioncards"




class FooterLink(models.Model):
    label = models.CharField(max_length=100)
    url = models.URLField()

class FooterService(models.Model):
    label = models.CharField(max_length=100)
    url = models.URLField()

class ContactInfo(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()  



class SocialLink(models.Model):
      facebook_link = models.URLField(blank=True, null=True)
      twitter_link = models.URLField(blank=True, null=True)
      instagram_link = models.URLField(blank=True, null=True)
      youtube_link = models.URLField(blank=True, null=True)
      linkdin_link = models.URLField(blank=True, null=True)


class ContactInfo2(models.Model):
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    phone_hours = models.CharField(max_length=50)
    email_addresses = models.TextField()    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name 
    
class liveclasscontent(models.Model):
    image1=models.ImageField(upload_to="images/")
    heading=models.TextField()
    content=models.TextField()
    content1=models.CharField(max_length=400,default='')
class Meta:
    db_table="attendmanagecontent"
    
class liveclasscarousel(models.Model):
    image2=models.ImageField(upload_to="images/")
class Meta:
    db_table="attendmanagecarousel"

class liveclasscards(models.Model):
    image3=models.ImageField(upload_to="images/")
    field=models.TextField()
class Meta:
    db_table="attendmanagecards"
    
class timetablecont(models.Model):
    images=models.ImageField(upload_to="images/")
    heading=models.TextField()
    content=models.TextField()
    title1=models.CharField(max_length=100,default=None)
    content1=models.TextField(default=None)
    photo1=models.ImageField(upload_to="images/",default=None)

class Meta:
    db_table="attendmanagecont"
    
class timetablecarl(models.Model):
    images=models.ImageField(upload_to="images/")
    content=models.TextField()
class Meta:
    db_table="attendmanagecarl"

class timetablecards(models.Model):
    images=models.ImageField(upload_to="images/")
    heading=models.TextField()
    content=models.TextField()
class Meta:
    db_table="attendmanagecards"

class teachermenu(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    icon = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', related_name='children', blank=True, null=True, on_delete=models.CASCADE)
class leavestype(models.Model):
    leavetype=models.CharField(max_length=500)
    Noofleaves=models.CharField(max_length=500)
    leavecategory=models.CharField(max_length=500)

class leavemanagement(models.Model):
    title = models.CharField(max_length=500)
    Description = RichTextField( )    

class leave(models.Model):
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=True,blank=True)
    Leave_Type = models.ForeignKey(leavestype, on_delete=models.CASCADE,null=True,blank=True)
    Reason=RichTextField()
    from_date=models.DateField()
    to_date=models.DateField()
    today=models.DateTimeField(default=datetime.now)
    is_status=models.CharField(max_length=100,default="0")
    user_type=models.CharField(max_length=100,default="0")
    days_difference = models.IntegerField(null=True, blank=True)
    read = models.BooleanField(default=False)
    read1 = models.BooleanField(default=False)
    schoolid=models.ForeignKey(Schools,on_delete=models.CASCADE,blank=True, null=True,)



class meta:
        db_table="leave" 

from ckeditor.fields import RichTextField
class Attendancemenu(models.Model):
    name=models.CharField(max_length=500)
    urls=models.CharField(max_length=700)
    icon=models.CharField(max_length=200)

class compose_message(models.Model):
    teachername=models.ForeignKey(Teachers,on_delete=models.CASCADE , blank=True, null=True,)
    MessageType=models.CharField(max_length=100)
    Message=models.CharField(max_length=100) 
    date=models.DateTimeField(auto_now_add=True, blank=True)
    studentname=models.ForeignKey(Student,on_delete=models.CASCADE , blank=True, null=True,)
    schoolid=models.ForeignKey(Schools,on_delete=models.CASCADE,blank=True, null=True,)
    is_status=models.CharField(max_length=100,default="0") 
    read1 = models.BooleanField(default=False) 

class teacherattendance(models.Model):
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)    

class footer_content(models.Model):
    linkname=models.CharField(max_length=100)
    linkurl=models.CharField(max_length=100)
    order=models.CharField(max_length=100,default='')

    class Meta:
        db_table="footer_content"

class adminphoto(models.Model):
    image=models.ImageField(upload_to="images/") 

class admin_main(models.Model):
    name=models.CharField(max_length=100)
    url=models.CharField(max_length=100)

    class Meta:
        db_table="admin_main"  

class carousel_img(models.Model):
    image=models.ImageField(upload_to="images/")
class Meta:
    db_table="carousel_img"

class carditems(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=500)
    image=models.ImageField(upload_to="images/")
class Meta:
    db_table="carditems"

class content_image(models.Model):
    title1=models.CharField(max_length=100)
    content1=models.TextField()
    image1=models.ImageField(upload_to="images/",default=None)
    title2=models.CharField(max_length=100 ,default=None)
    content2=models.TextField(default=None)
    image2=models.ImageField(upload_to="images/",default=None)
    title3=models.CharField(max_length=100,default=None)
    content3=models.TextField(default=None)
    image3=models.ImageField(upload_to="images/",default=None)
    title4=models.CharField(max_length=100,default=None)
    content4=models.TextField(default=None)
    image4=models.ImageField(upload_to="images/",default=None)
class Meta:
    db_table="content_image"
    
          
class library(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    photo=models.ImageField(upload_to="images/")
    title1=models.CharField(max_length=100,default=None)
    content1=models.TextField(default=None)
    photo1=models.ImageField(upload_to="images/",default=None)
    
class Meta:
    db_table="library"


class cimage(models.Model):
    image=models.ImageField(upload_to="images/",default=None)
class Meta:
    db_table="cimage"    
    
    
class card(models.Model):
    cardtitle=models.CharField(max_length=100,default=None)
    cardcontent=models.TextField(default=None)
    cardphoto=models.ImageField(upload_to="images/",default=None)
class Meta:
    db_table="card"


from django.db import models

# Create your models here.
class Time(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    photo=models.ImageField(upload_to="images/")
    title1=models.CharField(max_length=100,default=None)
    content1=models.TextField(default=None)
    photo1=models.ImageField(upload_to="images/",default=None)

class Meta:
    db_table="Time"


class Timage(models.Model):
    image=models.ImageField(upload_to="images/",default=None)
class Meta:
    db_table="Timage"


class cards(models.Model):
    cardtitle=models.CharField(max_length=100,default=None)
    cardcontent=models.TextField(default=None)
    cardphoto=models.ImageField(upload_to="images/",default=None)
class Meta:
    db_table="cards"

class quiz_questions(models.Model):
    question=models.TextField(default=True)
    choice1=models.TextField(default=True)
    choice2=models.TextField(default=True)
    choice3=models.TextField(default=True)
    choice4=models.TextField(default=True)
    is_correct=models.TextField(default=True)
    class_name = models.ForeignKey(cls_name, on_delete=models.CASCADE,blank=True, null=True,)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,blank=True, null=True,)
       
   
class Meta:
    db_table="quiz_questions"

class instruction_headings(models.Model):
    image=models.ImageField(upload_to="images/")
    heading=models.CharField(max_length=100)
class Meta:
    db_table="instruction_headings"

class instructions11(models.Model):
    instr=models.CharField(max_length=100)
class Meta:
    db_table="instructions11"
class std_result(models.Model):
    questionstd=models.CharField(max_length=100,default=None,null=True)
    answer=models.CharField(max_length=100,default=None,null=True) 
    student=models.ForeignKey(Student,on_delete=models.CASCADE , blank=True, null=True,)
    classes=models.ForeignKey(cls_name,on_delete=models.CASCADE , blank=True, null=True,)
    subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE , blank=True, null=True,)   
class Meta:
    db_table="std_result"


class set_timer(models.Model):
    houres=models.IntegerField()
    minutes=models.IntegerField()
    secondes=models.IntegerField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,blank=True,null=True)
    class_name = models.ForeignKey(cls_name, on_delete=models.CASCADE,blank=True,null=True)
class Meta:
    db_table="set_timer"


class Excel(models.Model):
    exel=models.FileField(upload_to='pdf_files/',default=None,blank=True)
class Meta:
    db_table="Excel"

from django import forms
from ckeditor.widgets import CKEditorWidget

class MyForm(forms.Form):
    content = forms.CharField(widget=CKEditorWidget())
class Meta:
    db_table="MyForm"

class text(models.Model):
    details = models.TextField()


from django.db import models

class MeetLink(models.Model):
    link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)


    from django.db import models

class Meeting(models.Model):
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    meeting_link = models.URLField()

# class Meeting1(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#     meet_link = models.URLField()
#     # google_event_id = models.CharField(max_length=255, default="")

#     def __str__(self):
#         return self.title

from django.db import models

class Meeting1(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    meet_link = models.URLField()
    # google_event_id = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.title




class fee_payment(models.Model):    
    student_class = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True) 
    schoolid = models.ForeignKey(Schools, on_delete=models.CASCADE, blank=True, null=True)      
    terms = models.CharField(max_length=100, default="") 
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    first_name = models.CharField(max_length=255, default="") 
    s_class = models.CharField(max_length=255, default="")     
    term1 = models.CharField(max_length=100, default="") 
    term2 = models.CharField(max_length=100, default="")     
    term3 = models.CharField(max_length=100, default="") 
    amountpaid = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # New field


from django.db import models

class ZoomMeeting(models.Model):
    school =  models.ForeignKey(Schools, on_delete=models.CASCADE, blank=True, null=True)
    class_name = models.ForeignKey(cls_name, on_delete=models.CASCADE, blank=True, null=True)
    subject_name = models.ForeignKey(Subject, on_delete=models.CASCADE, blank=True, null=True)
    Teacher_name = models.ForeignKey(Teachers, on_delete=models.CASCADE, blank=True, null=True)
    
    meeting_date = models.DateField()
    starttime = models.TimeField(null=True, blank=True)
    endtime = models.TimeField(null=True, blank=True)
    meeting_link = models.URLField()
    mystudent = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)

# class hero(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField(max_length=100)
#     image=models.ImageField(upload_to="images/")

# models.py

from django.db import models





class pricing_head(models.Model):
    title = models.TextField()
    content = models.TextField()

class Meta:
    db_table = "pricing_head"

class pricing_body(models.Model):
    title = models.TextField()
    content = models.TextField()
    icon = models.CharField(max_length=100,default="None")

class Meta:
    db_table = "pricing_body"

from django.db import models

class plans(models.Model):
    plan=models.CharField(max_length=100)
    amt=models.IntegerField()
    features=models.CharField(max_length=100)
class Meta:
    db_table="plans"

class plans1(models.Model):
    plan1=models.CharField(max_length=100)
    amt1=models.IntegerField()
    features1=models.CharField(max_length=100)
class Meta:
    db_table="plans1"

class plans2(models.Model):
    plan2=models.CharField(max_length=100)
    amt2=models.IntegerField()
    features2=models.CharField(max_length=100)
class Meta:
    db_table="plans2"



# models.py
from django.db import models


class Feature(models.Model):
    name = models.CharField(max_length=100)
    plan = models.ForeignKey(PricingPlan, related_name='features', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

