"""
URL configuration for learning project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from learning import views,adminviews,studentviews,teacherviews
from learning.views import StudentFormListCreateView, TimeTableView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('learning.urls')),
    path('',views.homepage, name="homepage"),
    path('carousel_insert/',views.carousel_insert),
    path('card_insert/',views.card_insert),
    path('content_image_insert/',views.content_image_insert),
    path('student-form/', StudentFormListCreateView.as_view(), name='student-form-list-create'),

    path('TimeTableView/',TimeTableView.as_view(),name='TimeTableView'),
    # path('login-form/', LoginView.as_view(), name='login-form-list-create'),
    # path('adminA/', views.adminA, name='adminA'),
    path('password/', views.password, name='password'),
    path('adminB/', views.adminB, name='adminB'),
    path('doLogin/',views.doLogin,name="doLogin"),
    path('logout1/',views.logout1,name="logout1"),
    path('attendance_stu/',views.attendance_stu,name="attendance_stu"),
    path('class_students/<int:class_id>/', views.class_students, name='class_students'),
 path('combined/<int:id>/', views.CombinedView.as_view(), name='combined'),
    path('students_view/',views.students_view,name="students_view"),


    
    path('new_home1/',views.new_home1,name='new_home1'),
    path('sidenavbar/',adminviews.sidenavbar,name='sidenavbar'),
    path('Employ_home/',views.Employ_home,name='Employ_home'),
    path('navheader/',views.navheader,name='navheader'),

    path('studentregform/', views.studentregform, name='studentregform'),
    path('allstudents/',views.allstudents,name='allstudents'),

    path('reg/', views.reg),
    path('data/', views.data),
    path('home/', views.home),
    path('edit/<int:id>/',views.edit, name="edit"),
    path('update/<int:id>',views.update, name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    # path('regform/', views.regform, name='regform'),
    path('view_profile/<int:organization_id>/', views.view_profile, name='view_profile'),
    path('new_home/', views.new_home, name='new_home'),
    path('retrieve/', views.retrieve, name='retrieve'),
     
    path('register/', views.register, name='register'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('edit_teacher/<int:id>/',views.edit_teacher,name='edit_teacher'),
    path('teacher_read/',views.teacher_read,name='teacher_read'),
    path('teacher_delete/<int:id>/',views.teacher_delete,name='teacher_delete'),
    # path('teacherside/',views.teacherside,name='teacherside'),

    path('upload/', views.upload_file, name='upload_file'),
    path('download_file/<int:id>/', views.download_file, name='download_file'),
    path('upload_2/<int:id>/', views.upload_2, name='upload_2'),
    path('subjectnames/', views.subjectnames, name='subjectnames'),
    path('logout_view/',views.logout_view,name="logout_view"),

     # path('add_subject_names/', views.add_subject_names, name='add_subject_names'),
    # path('chapters/<int:subject_id>/', views.chapters, name='chapters'),
    # path('regform1/',views.regform1),
    # path('home1/',views.home),
    # path('subject/<int:subid>',views.subject),
    # path('chapter/<int:id>/<int:subid>',views.chapter),
    path('reg1/',views.reg1),
    path('display2/',views.display2),
    path('inserted/',views.inserted),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete"),
    # path('class12/',views.class12,name="class12"),
    # path('class11/',views.class11,name="class11"),
    # path('class10/',views.class10,name="class10"),
    # path('class9/',views.class9,name="class9"),
    # path('class8/',views.class8,name="class8"),
    # path('class7/',views.class7,name="class7"),
    # path('class6/',views.class6,name="class6"),
    # path('class5/',views.class5,name="class5"),
    # path('class4/',views.class4,name="class4"),
    # path('class3/',views.class3,name="class3"),
    # path('class2/',views.class2,name="class2"),
    # path('class1/',views.class1,name="class1"),


    path('logoupload/',views.logoupload,name="logoupload"),
    path('logoform/',views.logoform,name="logoform"),
    path('examhome/',views.examhome),
    path('examdisplay/',views.examdisplay),
    path('examinserte/',views.examinserte),
    path('examedit/<int:id>',views.examedit,name="examedit"),
    path('examupdate/<int:id>',views.examupdate,name="examupdate"),
    path('examdelete/<int:id>',views.examdelete,name="examdelete"),
# carl_______________________________________

    path('examhome2/',views.examhome2),
    path('examinsert2/',views.examinsert2),
    path('examedit2/<int:id>',views.examedit2,name="examedit2"),
    path('examupdate2/<int:id>',views.examupdate2,name="examupdate2"),
    path('examdelete/<int:id>',views.examdelete,name="examdelete"),

# cards_________________________________________________
    path('examhome3/',views.examhome3),
    path('examinsert3/',views.examinsert3),
    path('examedit3/<int:id>',views.examedit3,name="examedit3"),
    path('examupdate3/<int:id>',views.examupdate3,name="examupdate3"),
    path('examdelete3/<int:id>',views.examdelete3,name="examdelete3"),

    # path('regform_sub/',views.regform_sub),
    # path('home_sub/',views.home_sub),
    # path('subjects1/<int:subid>',views.subjects1),
    # path('chapter1/<int:id>/<int:subid>/<int:classid>',views.chapter1),
    # path('chapter1/<int:id>/<int:subid>',views.chapter1),
    # path('sub1/<int:classid>',views.sub1),
    # path('serve_pdf/<int:document_id>/', views.serve_pdf, name='serve_pdf'),

    path('homenavbarinsert/',views.homenavbarinsert,name="homenavbarinsert"),
      
    path('teacherregister/', views.teacherregister, name='teacherregister'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_subject/', views.add_subject, name='add_subject'),
    path('edit_teacher/<int:id>/',views.edit_teacher,name='edit_teacher'),
    path('teacher_read/',views.teacher_read,name='teacher_read'),
    path('teacher_delete/<int:id>/',views.teacher_delete,name='teacher_delete'),
    # path('teacher_sidebar/',teacherviews.teacher_sidebar,name='teacher_sidebar'),
    # path('student_sidebar/',views.student_sidebar,name='student_sidebar'),

    path('regform_sub/',views.regform_sub),
    path('home_sub/',views.home_sub),
    path('subject/<int:subid>',views.subject),
    path('chapter/<int:id>/<int:subid>/<int:classid>',views.chapter),
    # path('chapter1/<int:id>/<int:subid>',views.chapter1),
    path('sub/<int:classid>',views.sub),
    path('serve_pdf/<int:document_id>/', views.serve_pdf, name='serve_pdf'),

    path('insert_fee/',views.insert_fee),
    path('table_fee/',views.table_fee),
    path('display_fee/',views.display_fee),
    path('edit/<int:id>',views.edit,name="edit"),
    path('update_fee/<int:id>',views.update_fee,name="update_fee"),
    path('delete_fee/<int:id>',views.delete_fee,name="delete_fee"),
    
    path('crinsert_fee/',views.crinsert_fee),
    path('crtable_fee/',views.crtable_fee),
    path('credit_fee/<int:id>',views.credit_fee,name="credit_fee"),
    path('crupdate_fee/<int:id>/',views.crupdate_fee,name="crupdate_fee"),
    path('crdelete_fee/<int:id>',views.crdelete_fee,name="crdelete_fee"),
    
    
    path('cardinsert_fee/',views.cardinsert_fee),
    path('cardtable/',views.cardtable),
    path('cardedit/<int:id>',views.cardedit,name="cardedit"),
    path('cardupdate_fee/<int:id>',views.cardupdate_fee,name="cardupdate_fee"),
    path('carddelete_fee/<int:id>',views.carddelete_fee,name="carddelete_fee"),

    path('staff_sms/', views.staff_sms, name='staff_sms'),
    # path('display_staff_data/', views.display_staff_data, name='display_staff_data'),
    path('fea_staff/', views.fea_staff, name='fea_staff'),
    path('importance_staff/', views.importance_staff, name='importance_staff'),
    path('prob_staff/', views.prob_staff, name='prob_staff'),
    path('staffmanagement/', views.staffmanagement, name='staffmanagement'),
    
    path('attendmanagecontentapi/',views.attendmanagecontentapi.as_view(),name="attendmanagecontentapi"),
    path('amcarouselapi/',views.amcarouselapi.as_view(),name="amcarouselapi"),
    path('amcardsapi/',views.amcardsapi.as_view(),name="amcardsapi"),
    path('attendmanagedisplay/',views.attendmanagedisplay),
    path('attendmanagecurd/',views.attendmanagecurd),
    path('attendcontentinsert/',views.attendcontentinsert),
    path('attendcontentedit/<int:id>',views.attendcontentedit,name="attendcontentedit"),
    path('attendcontentupdate/<int:id>',views.attendcontentupdate,name="attendcontentupdate"),
    path('deletecontent/<int:id>',views.deletecontent,name="deletecontent"),
    
    path('carouselinsert/',views.carouselinsert),
    path('carouseledit/<int:id>',views.carouseledit,name="carouseledit"),
    path('carouselupdate/<int:id>',views.carouselupdate,name="carouselupdate"),
    path('carouseldelete/<int:id>/', views.carouseldelete, name='carouseldelete'),
    
    path('cardinsert/',views.cardinsert),
    path('cardedit/<int:id>',views.cardedit,name="cardedit"),
    path('carupdate/<int:id>',views.carupdate,name="carupdate"),
    path('carddelete/<int:id>',views.carddelete,name="carddelete"),

    path('insert_paymentfeatures/',views.insert_paymentfeatures),
    path('crinsert_paymnetfeatures/',views.crinsert_paymentfeatures),
    path('cardinsert_paymentfeatures/',views.cardinsert_paymentfeatures),
    path('display_paymentfeatures/',views.display_paymentfeatures),
    path('table_paymentfeatures/',views.table_paymentfeatures),

    path('admission_home1/',views.admission_home1),
    path('admission_display/',views.admission_display),
    path('admission_insert1/',views.admission_insert1),
    path('admission_edit1/<int:id>',views.admission_edit1,name="admission_edit1"),
    path('admission_update1/<int:id>',views.admission_update1,name="admission_update1"),
    path('admission_delete1/<int:id>',views.admission_delete1,name="admission_delete1"),
    
    # content_______________
    path('admission_home2/',views.admission_home2),
    path('admission_insert2/',views.admission_insert2),
    path('admission_edit2/<int:id>',views.admission_edit2,name="admission_edit2"),
    path('admission_update2/<int:id>',views.admission_update2,name="admission_update2"),
    path('admission_delete2/<int:id>',views.admission_delete2,name="admission_delete2"),

    # cards_____________________________________________________________________________
    path('admission_home3/',views.admission_home3),
    path('admission_insert3/',views.admission_insert3),
    path('admission_edit3/<int:id>',views.admission_edit3,name="admission_edit3"),
    path('admission_update3/<int:id>',views.admission_update3,name="admission_update3"),
    path('admission_delete3/<int:id>',views.admission_delete3,name="admission_delete3"),

    path('contact/',views.contact,name="contact"),
    path('create-contact-info/', views.create_contact_info, name='create_contact_info'),
    path('view-contact-info/', views.view_contact_info, name='view_contact_info'),
    path('update-contact-info/<int:pk>/', views.update_contact_info, name='update_contact_info'),
    path('delete-contact-info/<int:pk>/', views.delete_contact_info, name='delete_contact_info'),
    path('contact/success/', views.success_page, name='success_page'),
    path('retrieve_contact_messages/', views.retrieve_contact_messages, name='retrieve_contact_messages'),
    path('reply_message/reply/<int:message_id>/', views.reply_message, name='reply_message'),
    path('adminA_Password_save/',views.adminA_Password_save,name="adminA_Password_save"),
    path('upload_image/',views.upload_image,name="upload_image"),

    path('importance_staff/insert/',views.importance_staff, name='importance_staff'),
    path('display_staff_imp_data/',views.display_staff_imp_data, name='display_staff_imp_data'),
    path('edit_staff_imp_data/<int:pk>/',views.edit_staff_imp_data, name='edit_staff_imp_data'),
    path('delete_staff_imp_data/<int:pk>/',views.delete_staff_imp_data, name='delete_staff_imp_data'),
    path('prob_staff/',views. prob_staff, name='prob_staff'),
    path('display_staff_prob_data/',views.display_staff_prob_data, name='display_staff_prob_data'),
    path('edit_staff_prob_data/<int:pk>/',views.edit_staff_prob_data, name='edit_staff_prob_data'),
    path('delete_staff_prob_data/<int:pk>/',views.delete_staff_prob_data, name='delete_staff_prob_data'),
    
    path('fea_staff/insert/',views. fea_staff, name='fea_staff'),
    path('display_fea_data/',views.display_fea_data, name='display_fea_data'),
    path('edit_fea_data/<int:pk>/',views.edit_fea_data, name='edit_fea_data'),
    path('delete_fea_data/<int:pk>/',views. delete_fea_data, name='delete_fea_data'),
    path('teachercount/',adminviews.teachercount,name='teachercount'),
    path('insert_card/',views.insert_library),
    path('crinsert_card1/',views.crinsert_cimage),
    path('cardinsert_card3/',views.cardinsert_card),
    path('display_display/',views.display_display),
    path('table_paymentfeatures/',views.table_library),

    path('alldata/',adminviews.alldata,name='alldata'),
    path('liveclasscontentapi/',views.liveclasscontentapi.as_view(),name="liveclasscontentapi"),
    path('lccarouselapi/',views.lccarouselapi.as_view(),name="lccarouselapi"),
    path('lccardsapi/',views.lccardsapi.as_view(),name="lccardsapi"),
    path('liveclassmanagedisplay/',views.liveclassmanagedisplay),
    path('livemanagecurd/',views.livemanagecurd),
    path('livecontentinsert/',views.livecontentinsert),
    path('livecontentedit/<int:id>',views.livecontentedit,name="livecontentedit"),
    path('livecontentupdate/<int:id>',views.livecontentupdate,name="livecontentupdate"),
    path('livecontentdelete/<int:id>',views.livecontentdelete,name="livecontentdelete"),
    
    path('livecarouselinsert/',views.livecarouselinsert),
    path('livecarouseledit/<int:id>',views.livecarouseledit,name="livecarouseledit"),
    path('livecarouselupdate/<int:id>',views.livecarouselupdate,name="livecarouselupdate"),
    path('livecarouseldelete/<int:id>/', views.livecarouseldelete, name='livecarouseldelete'),
    
    path('livecardinsert/',views.livecardinsert),
    path('livecardedit/<int:id>',views.livecardedit,name="livecardedit"),
    path('livecarupdate/<int:id>',views.livecarupdate,name="livecarupdate"),
    path('livecarddelete/<int:id>',views.livecarddelete,name="livecarddelete"),

    path('footer_view',views.footer_view),
    path('timetable_home1/',views.timetable_home1),
    path('timetable_display/',views.timetable_display),
    path('timetable_insert1/',views.timetable_insert1),
    path('timetable_edit1/<int:id>',views.timetable_edit1,name="timetable_edit1"),
    path('timetable_update1/<int:id>',views.timetable_update1,name="timetable_update1"),
    path('timetable_delete1/<int:id>',views.timetable_delete1,name="timetable_delete1"),

# content__________________________
    path('timetable_home2/',views.timetable_home2),
    path('timetable_insert2/',views.timetable_insert2),
    path('timetable_edit2/<int:id>',views.timetable_edit2,name="timetable_edit2"),
    path('timetable_update2/<int:id>',views.timetable_update2,name="timetable_update2"),
    path('timetable_delete2/<int:id>',views.timetable_delete2,name="timetable_delete2"),
# cards_____________________________________________________________________________
    path('timetable_home3/',views.timetable_home3),
    path('timetable_insert3/',views.timetable_insert3),
    path('timetable_edit3/<int:id>',views.timetable_edit3,name="timetable_edit3"),
    path('timetable_update3/<int:id>',views.timetable_update3,name="timetable_update3"),
    path('timetable_delete3/<int:id>',views.timetable_delete3,name="timetable_delete3"),

    path('admin_attendance/',adminviews.admin_attendance,name='admin_attendance'),
    path('Leave_Management/',adminviews.Leave_Management,name='Leave_Management'),
    path('Leave_Management2/',adminviews.Leave_Management2,name='Leave_Management2'),
    path('Leave_type_edit/<int:id>/',adminviews.Leave_type_edit,name='Leave_type_edit'),
    path('Leave_type_update/<int:id>/',adminviews.Leave_type_update,name='Leave_type_update'),
    path('Leave_type_delete/<int:id>/',adminviews.Leave_type_delete,name='Leave_type_delete'),
    path('Teacher_leaves_view/', adminviews.Teacher_leaves_view, name='Teacher_leaves_view'),
    path('Student_leaves_view/', adminviews.Student_leaves_view, name='Student_leaves_view'),

    path('leave_approve/<int:id>',adminviews.leave_approve,name="leave_approve"),
    path('leave_disapprove/<int:id>',adminviews.leave_disapprove,name="leave_disapprove"),
    path('leave_approve1/<int:id>',adminviews.leave_approve1,name="leave_approve1"),
    path('leave_disapprove1/<int:id>',adminviews.leave_disapprove1,name="leave_disapprove1"),
    path('mark_all_as_read/',adminviews.mark_all_as_read, name='mark_all_as_read'),
    path('mark_as_read/<int:leave_id>', adminviews.mark_as_read, name='mark_as_read'),
    path('mark_as_read1/<int:leave_id>', adminviews.mark_as_read1, name='mark_as_read1'),
    path('Teacher_Attendance_display/',adminviews.Teacher_Attendance_display,name='Teacher_Attendance_display'),
   
    path('logout_view/',views.logout_view,name="logout_view"),
    path('teacher_sidebar/',teacherviews.teacher_sidebar,name='teacher_sidebar'),
    path('teacher_applyforleave/', teacherviews.teacher_applyforleave, name='teacher_applyforleave'),
    path('mark_all_as_read1/', teacherviews.mark_all_as_read1, name='mark_all_as_read1'),
    path('teacher_mark_as_read/<int:leave_id>', teacherviews.teacher_mark_as_read, name='teacher_mark_as_read'),
    path('student_sidebar/',studentviews.student_sidebar,name='student_sidebar'),
    path('student_applyforleave/', studentviews.student_applyforleave, name='student_applyforleave'),
    path('mark_all_as_read2/', studentviews.mark_all_as_read2, name='mark_all_as_read2'),
    path('student_mark_as_read/<int:leave_id>', studentviews.student_mark_as_read, name='student_mark_as_read'),
    path('create_Teacher_shifts/',adminviews.create_Teacher_shifts,name='create_Teacher_shifts'),
    path('create_Teacher_shifts_display/',adminviews.create_Teacher_shifts_display,name='create_Teacher_shifts_display'),
    path('create_Teacher_shifts_edit/<int:id>',adminviews.create_Teacher_shifts_edit,name='create_Teacher_shifts_edit'),
    path('create_Teacher_shifts_update/<int:id>',adminviews.create_Teacher_shifts_update,name='create_Teacher_shifts_update'),
    path('create_Teacher_shifts_delete/<int:id>',adminviews.create_Teacher_shifts_delete,name='create_Teacher_shifts_delete'),
    path('compose_message12/',adminviews.compose_message12,name='compose_message12'),
    path('teacher_sidebar2/',teacherviews.teacher_sidebar2,name='teacher_sidebar2'),
    path('footer1/',views.footer1,name="footer1"),
    path('footer_data/',views.footer_data,name="footer_data"),
    path('student_showmessage/',studentviews.student_showmessage,name='student_showmessage'),
    path('teachdata/',adminviews.teachdata,name='teachdata'),
    # path('assign_subjects_classes/',adminviews.assign_subjects_classes,name='assign_subjects_classes'),
    path('assign_subjects_classes/',adminviews.assign_subjects_classes, name='assign_subjects_classes'),
    path('view_teacher_sub_class/',adminviews.view_teacher_sub_class,name='view_teacher_sub_class'),
    path('addsubject/',adminviews.addsubject,name='addsubject'),
    path('addclass/',adminviews.addclass,name='addclass'),
    path('classes1to4/',adminviews.classes1to4,name='classes1to4'),
    path('class_wise/',adminviews.class_wise,name='class_wise'),
    path('classes5to8/',adminviews.classes5to8,name='classes5to8'),
    path('classes9to12/',adminviews.classes9to12,name='classes9to12'),
    path('class1/',adminviews.class1,name='class1'),
    path('class2/',adminviews.class2,name='class2'),
    path('class3/',adminviews.class3,name='class3'),
    path('class4/',adminviews.class4,name='class4'),
    path('class5/',adminviews.class5,name='class5'),
    path('class6/',adminviews.class6,name='class6'),
    path('class7/',adminviews.class7,name='class7'),
    path('class8/',adminviews.class8,name='class8'),
    path('class9/',adminviews.class9,name='class9'),
    path('class10/',adminviews.class10,name='class10'),
    path('class11/',adminviews.class11,name='class11'),
    path('class12/',adminviews.class12,name='class12'),
    path('teaching_staff/',adminviews.teaching_staff,name='teaching_staff'), 
    path('non_teaching_staff/',adminviews.non_teaching_staff,name='non_teaching_staff'), 
    path('staff_management/',adminviews.staff_management,name='staff_management'),
    path('teacher_messages_mark_all_as_read/', teacherviews.teacher_messages_mark_all_as_read, name='teacher_messages_mark_all_as_read'),
    path('teacher_messages_mark_as_read/<int:compose_message_id>', teacherviews.teacher_messages_mark_as_read, name='teacher_messages_mark_as_read'),
    path('student_all_messages_as_read/', studentviews.student_all_messages_as_read, name='student_all_messages_as_read'),
    path('student_messages_mark_as_read/<int:compose_message_id>', studentviews.student_messages_mark_as_read, name='student_messages_mark_as_read'),

    path('dealing_subjects/',teacherviews.dealing_subjects,name='dealing_subjects'),
    path('Access_subjects/',teacherviews.Access_subjects,name='Access_subjects'),
    path('Set_quiz/<int:id>',teacherviews.Set_quiz,name="Set_quiz"),
    path('Not_set_quiz/<int:id>',teacherviews.Not_set_quiz,name="Not_set_quiz"),
    path('quiz/<int:id>',teacherviews.quiz,name='quiz'),
    path('time/<int:id>',teacherviews.time,name="time"),
    path('import_from_excel/<int:id>',teacherviews.import_from_excel,name="import_from_excel"),
    path('insert_exel/',teacherviews.insert_exel),
    path('serve_pdf/<int:document_id>/', teacherviews.serve_pdf, name='serve_pdf'),
    path('general_instructions/',studentviews.general_instructions,name= 'general_instructions'),   
    path('quiz_subjects/',studentviews.quiz_subjects,name='quiz_subjects'),
    path('std_quiz/',studentviews.std_quiz,name='std_quiz'),
    path('std_quiz1/<int:subject>',studentviews.std_quiz1,name='std_quiz1'),
    path('std_results/',teacherviews.std_results),
    path('ins/',views.ins,name='ins'),
    # path('create_meeting/', adminviews.create_meeting, name='create_meeting'),
    # path('generate_meeting_link/<int:class_id>/<int:subject_id>/<int:teacher_id>/', adminviews.generate_meeting_link, name='generate_meeting_link'),
    # path('meeting_list/', adminviews.meeting_list, name='meeting_list'),

    # path('generate_meet_link/',adminviews.generate_meet_link,name='generate_meet_link'),
    # path('generate-zoom-meeting-link/', adminviews.generate_zoom_meeting_link, name='generate_zoom_meeting_link'),
    # path('zoom/callback/', adminviews.zoom_callback_view, name='zoom_callback_view'),
    


    path('class_form/',adminviews.class_form,name='class_form'),
    path('Fee_pay/',adminviews.Fee_pay),                       
    path('Fees_std_details/<int:student_class>',adminviews.Fees_std_details,name="Fees_std_details"),

                 
    path('meeting/',adminviews.create_meeting,name='create_meeting'),
    path('meeting_list1/',adminviews.meeting_list1,name='meeting_list1'),
    path('teacher_meetings/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student_meetings/', views.student_dashboard, name='student_dashboard'),

   
    path('class_form1/',adminviews.class_form1,name='class_form1'),
    path('update_fee_payment/<int:payment_id>/', adminviews.update_fee_payment, name='update_fee_payment'),
    path('delete_fee_payment/<int:payment_id>/', adminviews.delete_fee_payment, name='delete_fee_payment'),
    
          

    path('studentfeepay_form/',studentviews.studentfeepay_form,name='studentfeepay_form'),
    path('studentpayfee_edit/<int:id>/',studentviews.studentpayfee_edit,name="studentpayfee_edit"),
    path('studentpayfee_update/<int:id>',studentviews.studentpayfee_update,name='studentpayfee_update'),
    

    path('pricing/',views.pricing,name='pricing'),
    path('add_feature/', views.add_feature, name='add_feature'),
    path('add_pricing_plan/', views.add_pricing_plan, name='add_plan'),

     path('pricing_table/', views.pricing_table, name='pricing_table'),
     path('regform/<int:plan_id>/', views.regform, name='regform'),

    path('addsubject1/', views.addsubject1, name='addsubject1'),
    path('manage_sub/', views.manage_sub, name='manage_sub'),
    path('sub_delete/<int:id>/', views.sub_delete, name='sub_delete'),
    path('subject_edit/<int:id>/', views.subject_edit, name='subject_edit'),
    path('subject_update/<int:id>/', views.subject_update, name='subject_update'),
    path('get-subjects-for-class/<int:class_id>/',adminviews.get_subjects_for_class, name='get_subjects_for_class'),
    path('create_meeting1/', views.create_meeting1, name='create_meeting1'),
    path('book/', views.book, name='book'),
    path('html/', views.html, name='html'),



 
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
