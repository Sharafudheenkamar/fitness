app_name = 'adminfitness'
from django.urls import path
from .views import *
urlpatterns = [
    path('admin_homepage/',Admin_homepage.as_view(),name='admin_homepage'),
    path('admin_addtrainers_post/', Adminaddtrainers.as_view(),name='admin_addtrainers_post'),
    path('admin_viewtrainers/', Adminviewtrainers.as_view(),name='admin_viewtrainers'),
    path('admin_viewtrainer_post/', admin_viewtrainer_post),
    path('admin_deletetrainer/<str:data>', Admindeletetrainers.as_view(),name='admin_deletetrainer'),
    path('admin_updatetrainers/<str:data>',Adminupdatetrainers.as_view(),name='admin_updatetrainers_post'),
    path('admin_viewtrainers_post/', admin_viewtrainers_post),

    path('admin_addcategory/', Admin_Category.as_view(),name='admin_addcategory'),
    path('admin_viewcategory/', Adminviewcategory.as_view(),name='admin_viewcategory'),
    path('admin_viewcategorypost/', Adminviewcategorypost.as_view(),name='admin_viewcategorypost'),
    path('admin_editcategory/<cid>', Admineditcategory.as_view(),name='admin_editcategory'),
    # path('admin_viewusercomplaint/', views.admin_viewusercomplaint),
    path('admin_deletecategory/<id>',Admindeletecategory.as_view(),name='admin_deletecategory'),#

    path('admin_viewcategory_post/', admin_viewcategory_post),
    path('admin_viewuser/', admin_viewuser),
    path('admin_viewuser_post/', admin_viewuser_post),
    path('admin_viewusercomplaint/',admin_viewusercomplaint),
    path('admin_viewusercomplaint_post/', admin_viewusercomplaint_post),
    path('admin_usercomplaintreply_post/', admin_usercomplaintreply_post),
    path('admin_usercomplaintreply/<id>', admin_usercomplaintreply),
    path('admin_viewfeedback/', admin_viewfeedback),
    path('admin_viewfeedback_post/', admin_viewfeedback_post),
    path('admin_viewpayment/', admin_viewpayment),
    path('admin_trainerviewposturevideo/<tid>', admin_trainerviewposturevideo),
    path('admin_viewposturevideo/<tid>', admin_viewposturevideo),
    path('admin_changepwd/', admin_changepwd),
    path('admin_changepwd_post/', admin_changepwd_post),
    path('admin_logout/', admin_logout),
    path('admin_viewsubscription/',Adminviewsubscriptions.as_view()),
    path('admin_viewsubscriptionpost/',Adminviewsubscriptionspost.as_view()),
    path('admin_addsubscription/',Adminaddsubscriptions.as_view(),name='adminaddsubscription'),
    path('admin_updatesubscription/<int:data>', Adminupdatesubscriptions.as_view(), name='adminupdatesubscription'),
    path('admin_deletesubscription/<int:data>', Admindeletesubscriptions.as_view(), name='admindeletesubscription'),
    path('admin_viewchallenges/', admin_viewchallenges),
    path('admin_viewtasks/', admin_viewtasks),
    path('admin_viewusermoredetails/<int:id>', admin_viewusermoredetails),

]