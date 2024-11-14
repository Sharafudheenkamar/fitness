"""
URL configuration for Fitnesspro project.

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
from django.urls import path
from myapp import views


urlpatterns = [
    path('login/', views.login),

    path('login_post/',views.login_post),
    path('admin_addtrainers_post/', views.admin_addtrainers_post),
    path('admin_viewtrainers_post/', views.admin_viewtrainers_post),
    path('admin_deletetrainer/<id>', views.admin_deletetrainer),
    path('admin_updatetrainers_post/', views.admin_updatetrainers_post),

    path('forget_password/', views.forget_password),
    path('forget_password_post/', views.forget_password_post),
    # path('admin_viewuser/', views.admin_viewuser),
    path('admin_viewuser_post/', views.admin_viewuser_post),
    # path('admin_viewusermoredetails_post/', views.admin_viewusermoredetails_post),
    path('admin_addcategory_post/', views.admin_addcategory_post),
    path('admin_editcategory_post/', views.admin_editcategory_post),
    path('admin_viewcategory_post/', views.admin_viewcategory_post),
    path('admin_deletecategory/<id>', views.admin_deletecategory),
    path('admin_viewusercomplaint_post/', views.admin_viewusercomplaint_post),
    path('admin_usercomplaintreply_post/', views.admin_usercomplaintreply_post),
    path('admin_viewfeedback_post/', views.admin_viewfeedback_post),
    path('admin_viewposturevideo_post/', views.admin_viewposturevideo_post),
    path('admin_viewpayment_post/', views.admin_viewpayment_post),
    path('admin_changepwd_post/', views.admin_changepwd_post),

    path('trainer_addposture_post/', views.trainer_addposture_post),
    path('trainer_viewposture_post/', views.trainer_viewposture_post),
    path('trainer_editposture_post/', views.trainer_editposture_post),
    path('trainer_deletetposture/<id>', views.trainer_deletetposture),
    path('trainer_viewuser_post/', views.trainer_viewuser_post),
    path('trainer_adddietplan_post/', views.trainer_adddietplan_post),
    path('trainer_viewdietplan_post/', views.trainer_viewdietplan_post),
    path('trainer_changepwd_post/', views.trainer_changepwd_post),

    path('user_signup_post/', views.user_signup_post),
    path('user_viewposture_post/', views.user_viewposture_post),
    path('user_viewcomplaintreply_post/', views.user_viewcomplaintreply_post),
    path('user_sentfeedback_post/', views.user_sentfeedback_post),
    path('user_payment_post/', views.user_payment_post),
    path('user_viewdietplan_post/', views.user_viewdietplan_post),
    path('user_changepwd_post/', views.user_changepwd_post),
    path('user_sendcomplaint_post/',views.user_sendcomplaint_post),

    path('admin_addtrainers/',views.admin_addtrainers),
    path('admin_viewtrainers/',views.admin_viewtrainers),
    path('admin_updatetrainers/<tid>',views.admin_updatetrainers),
    path('admin_viewuser/',views.admin_viewuser),
    path('admin_viewusermoredetails/<id>',views.admin_viewusermoredetails),
    path('admin_addcategory/',views.admin_addcategory),
    path('admin_viewcategory/',views.admin_viewcategory),
    path('admin_editcategory/<cid>',views.admin_editcategory),
    path('admin_viewusercomplaint/',views.admin_viewusercomplaint),
    path('admin_usercomplaintreply/<id>', views.admin_usercomplaintreply),
    path('admin_viewfeedback/', views.admin_viewfeedback),
    path('admin_viewpayment/', views.admin_viewpayment),
    path('admin_viewposturevideo/<tid>', views.admin_viewposturevideo),
    path('admin_changepwd/', views.admin_changepwd),
    path('admin_logout/', views.admin_logout),
    path('admin_homepage/', views.admin_homepage),


    path('trainer_viewprofile/', views.trainer_viewprofile),
    path('trainer_addposture/', views.trainer_addposture),
    path('trainer_viewposture/', views.trainer_viewposture),
    path('trainer_playvideo/', views.trainer_playvideo),
    path('trainer_editposture/<id>', views.trainer_editposture),
    path('trainer_viewuser/', views.trainer_viewuser),
    path('trainer_viewusermoredetails/<id>', views.trainer_viewusermoredetails),
    path('trainer_adddietplan/', views.trainer_adddietplan),
    path('trainer_viewdietplan/', views.trainer_viewdietplan),
    path('trainer_editdietplan/<id>', views.trainer_editdietplan),
    path('trainer_editdietplan_post/', views.trainer_editdietplan_post),
     path('trainer_deletetdiet/<id>', views.trainer_deletetdiet),
    path('trainer_querychat/', views.trainer_querychat),
    path('trainer_changepwd/', views.trainer_changepwd),
    path('trainer_logout/', views.trainer_logout),
    path('trainer_homepage/', views.trainer_homepage),

    path('user_signup/', views.user_signup),
    path('user_viewprofile/', views.user_viewprofile),
    path('user_viewposture/', views.user_viewposture),
    path('user_playvideo/', views.user_playvideo),
    path('user_sentcomplaint/', views.user_sentcomplaint),
    path('user_viewcomplaintreply/', views.user_viewcomplaintreply),
    path('user_sentfeedback/', views.user_sentfeedback),
    path('user_viewdietplan/', views.user_viewdietplan),
    path('user_sendquery/', views.user_sendquery),
    path('user_payment/', views.user_payment),
    path('user_changepwd/', views.user_changepwd),
    path('user_logout/', views.user_logout),
    path('user_homepage/', views.user_homepage),
    path('user_view_trainer/', views.user_view_trainer),
    path('user_view_trainer_post/', views.user_view_trainer_post),
    path('rating/<id>', views.rating),
    path('rating_post/', views.rating_post),



    path('chat/<toid>', views.chat),
    path('chat_send/<msg>/<tid>', views.chat_send),
    path('chat_view/<tid>', views.chat_view),

    path('chat1/<toid>', views.chat1),
    path('chat_send1/<msg>/<tid>', views.chat_send2),
    path('chat_view1/<tid>', views.chat_view2),

]
