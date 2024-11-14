# app_name = 'users'
from django.urls import path
from.views import *
urlpatterns = [
    path('',Login.as_view(),name='login'),
    path('clientregistration/',Clientregistration.as_view(),name='clientregistration'),
    path('logout/',Logout.as_view(),name='logout'),
    path('admin_homepage/',Adminhome.as_view(),name='admin_homepage'),
    path('trainer_homepage/',Trainerhome.as_view(),name='trainer_homepage'),
    path('client_homepage/',Clienthome.as_view(),name='client_homepage'),
    path('userloginapi/', UserLoginapi.as_view(), name='userloginapi'),


    path('user_signup/', Clientregistration.as_view(), name='usersignup'),
    path('forgotpassword/', ForgotPassword.as_view(), name='forgotpassword'),
    path('changepassword/', PasswordChange.as_view(), name='changepassword'),

    path('forgotpasswordapi/', ForgotPasswordAPIView.as_view(), name='forgotpasswordapi'),
    path('changepasswordapi/', PasswordChangeAPIView.as_view(), name='changepasswordapi'),
    path('changeprofilepasswordapi/',ProfilePasswordChange.as_view()),
    path('changeprofileplanapi/', ProfilePlanChange.as_view()),

]