
from django.contrib import admin
from django.urls import path, include

from myapp import views

urlpatterns = [
    path('login/',views.login),
    path('logout/',views.logout),
    path('admin_home/',views.admin_home),
    path('change_password/',views.change_password),
    path('complaint/',views.complaint),
    path('disease_edit/<id>',views.disease_edit),
    path('disease_view/',views.disease_view),
    path('disease_delete/<id>',views.disease_delete),
    path('disease/',views.disease),
    path('doctor_edit/<id>',views.doctor_edit),
    # path('doctor/',views.doctor),
    path('send_replay/<id>',views.send_replay),
    path('view_doctor/',views.view_doctor),
    path('view_feedback/',views.view_feedback),
    path('VIEW_USER/',views.VIEW_USER),
    path('add_remedies/',views.add_remedies),
    path('view_symptoms/',views.view_symptoms),
    path('symptoms_delete/<id>',views.symptoms_delete),
    path('SYMPTOMS_edit/<id>',views.SYMPTOMS_edit),
    path('symptoms_edit_post/',views.symptoms_edit_post),
    path('view_review/',views.view_review),
    path('approve_doctor/<id>',views.approve_doctor),
    path('reject_doctor/<id>',views.reject_doctor),
    # path('terminate_doctor/<id>',views.terminate_doctor),
    path('terminate-doctor/<int:review_id>/',views. terminate_doctor, name='terminate_doctor'),

    path('login_post/',views.login_post),
    path('forgot/',views.forgot),
    path('forgot_post/',views.forgot_post),
    path('change_password_post/', views.change_password_post),
    path('complaint_post/', views.complaint_post),
    path('disease_edit_post/',views.disease_edit_post),
    path('disease_view_post/', views.disease_view_post),
    path('disease_post/', views.disease_post),

    path('doctor_signup/',views.doctor_signup),
    path('edit_profile/',views.edit_profile),
    path('edit_profile_post/',views.edit_profile_post),


    path('doctor_edit_post/',views.doctor_edit_post),
    path('doctor_post/',views.doctor_post),
    path('send_reply_post/',views.send_reply_post),
    path('view_doctor_post/',views.view_doctor_post),
    path('view_feedback_post/',views. view_feedback_post),
    path('view_user_post/',views.view_user_post),

    path('doctor_home/', views.doctor_home),
   
    path('add_schedule/', views.add_schedule),
    path('add_shedule_post/', views.add_shedule_post),
    path('doctor_disease_view/', views.doctor_disease_view),
    path('doctor_change_password/', views.doctor_change_password),
    path('edit_shedule/<id>', views.edit_shedule),
    path('view_appointment/<id>', views.view_appointment),
    path('view_schedule/', views.view_schedule),
    path('view_profile/', views.view_profile),
    path('deletedoctor/<id>', views.deletedoctor),
    path('doctor_view_symptoms/<id>',views.doctor_view_symptoms),

    path('doctors_disease_view_post/', views.doctors_disease_view_post),
    path('doctors_change_password_post/', views.doctors_change_password_post),
    path('edit_shedule_post/', views.edit_shedule_post),
    path('view_appointment_post/', views.view_appointment_post),
    path('view_schedule_post/', views.view_schedule_post),
    path('view_reviews/', views.view_reviews),
    path('view_review_post/', views.view_review_post),
    path('delete_schedule/<id>',views.delete_schedule),

    # Android
    path('and_login/', views.and_login),
    path('and_signup/', views.and_signup),
    path('user_changepassword/', views.user_changepassword),
    path('and_view_doctors/', views.and_view_doctors),
    path('and_view_doctors_search/', views.and_view_doctors_search),
    path('and_view_doctors_home/', views.and_view_doctors_home),
    path('and_view_schedules/', views.and_view_schedules),
    path('and_take_appointment/', views.and_take_appointment),
    path('and_view_appointments_today/', views.and_view_appointments_today),
    path('and_view_appointments/', views.and_view_appointments),
    path('and_view_profile/', views.and_view_profile),
    path('and_edit_profile/', views.and_edit_profile),
    path('and_send_feedback/', views.and_send_feedback),
    path('and_send_complaint/', views.and_send_complaint),
    path('and_view_complaints/', views.and_view_complaints),
    path('and_view_diseases/', views.and_view_diseases),
    path('file_upload/', views.and_file_upload),

    path('chat/<id>',views.chat),
    path('chat_view/',views.chat_view),
    path('chat_send/<msg>',views.chat_send),
    path('User_sendchat/',views.User_sendchat),
    path('User_viewchat/',views.User_viewchat),

    path('User_appointmentsend_review/',views.User_appointmentsend_review),
    path('User_send_review/',views.User_send_review),
    path('User_view_review/',views.User_view_review),

    path('user_changepassword/',views.user_changepassword),
    path('user_view_profile/',views.user_view_profile),
    path('user_view_doctor/',views.user_view_doctor),
    path('view_doctor_schedule/',views.view_doctor_schedule),
    path('take_appointment/',views.take_appointment),
    path('send_feedback/',views.send_feedback),
    path('view_appointments/',views.view_appointments),
    path("predict_symptoms/",views.predict_symptoms),

    # path("predict_skin/",views.predict_skin),

]