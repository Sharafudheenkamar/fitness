
from django.urls import path
from .views import *
from django import views

urlpatterns = [
    path('clientviewprofile/',client_viewprofile),
    path('client_viewtrainers/', Clientviewtrainers.as_view(), name='admin_viewtrainers'),
    path('client_viewposturevideo/', client_viewposturevideo),

    path('clientregistration/',UserprofileCreateAPIView.as_view(),name='clientregistration'),
    path('clientregistration/<int:pk>', UserprofileCreateAPIView.as_view(), name='clientregistrationupdate'),
    path('clientlisttrainersapi/',Viewtrainers.as_view()),
    path('clientlistvideoesapi/',Viewvideoes.as_view()),
    path('clientlistvideoebyidapi/<str:data>/<str:id>',Viewvideobyid.as_view()),
    path('clientlikevideoebyidapi/<str:data>/<str:id>/<str:status>', Likevideoes.as_view()),
    # path('clientlikevideoebyidapi/<str:data>', Likevideoes.as_view()),
    path('like/<int:video_id>/<int:user_id>', LikeVideoAPIView.as_view(), name='like-video'),
    path('unlike/<int:video_id>/<int:user_id>', UnlikeVideoAPIView.as_view(), name='unlike-video'),
    path('clientlikecommentvideoebyapi/<str:data>/<str:id>',Clientlikecommentvideobyapi.as_view()),
    path('clientcommentvideoebyidapi/', Commentvideoes.as_view()),
    path('clientlistvideoesbycategoryapi/<str:data>',Viewvideoesbycategory.as_view()),
    path('clientlistdietapi/', Viewdiet.as_view()),
    path('clientlistdietbycategoryapi/<str:data>', Viewdietbycategory.as_view()),
    path('clientchallengelistapiview/', Viewchallengesapiview.as_view()),
    path('clienttaskapiview/', Viewtaskapiview.as_view()),
    path('clientfeedbackapiview/', Viewfeedbackapiview.as_view()),
    path('clientcomplaintapiview/', Viewcomplaintapiview.as_view()),
    path('clientcomplaintapiview/<int:data>', Viewcomplaintapiview.as_view()),

    path('user_viewposture_post/', user_viewposture),
       # path('user_payment_post/', views.user_payment_post),
    # path('user_viewdietplan_post/', views.user_viewdietplan_post),

    # path('user_sendcomplaint_post/',views.user_sendcomplaint_post),
    path('user_viewprofile/', user_viewprofile),
    # path('user_viewposture/', views.user_viewposture),
    # path('user_playvideo/', views.user_playvideo),

    path('user_sentfeedback/', user_sentfeedback),
    path('user_sentfeedback_post/', user_sentfeedback_post),
    path('user_viewdietplan/', user_viewdietplan),
    # path('user_sendquery/', views.user_sendquery),
    path('user_payment/', user_payment),
    path('user_sentcomplaint/', user_sentcomplaint),
    path('user_viewcomplaintreply/', user_viewcomplaintreply),
    path('user_sendcomplaint_post/',user_sendcomplaint_post),

    path('user_changepwd/', user_changepwd),
    path('user_changepwd_post/', user_changepwd_post),
    # path('user_logout/', views.user_logout),

    # path('user_view_trainer/', views.user_view_trainer),
    # path('user_view_trainer_post/', views.user_view_trainer_post),
    path('rating/<id>', rating),
    path('rating_post/<int:id>/', rating_post, name='rating_post'),

    path('chat/<toid>', chat),
    path('chat_send/<msg>/<tid>', chat_send),
    path('chat_view/<tid>', chat_view),

    path('chat1/<toid>', chat1),
    path('chat_send1/<msg>/<tid>', chat_send2),
    path('chat_view1/<tid>', chat_view2),
    path('trainerchat/<fromid>/<toid>', ChatView.as_view()),
    path('trainerchatpost/', ChatViewPOST.as_view(), name='send_message'),
    path('view_chat_history/', view_chat_history, name='view_chat_history'),
    path('user_payment_post/', user_payment_post),
    path('user_payment/', user_payment),
    path('user_homepage/', user_homepage),
]

