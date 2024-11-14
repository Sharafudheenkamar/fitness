app_name = 'trainer'
from django.urls import path
from .views import *

urlpatterns = [
    path('trainer_addposture_post/', trainer_addposture_post),
    path('trainer_viewposture_post/', trainer_viewposture_post),
    path('trainer_editposture_post/', trainer_editposture_post),
    path('trainer_deletetposture/<id>', trainer_deletetposture),
    path('trainer_viewuser_post/', trainer_viewuser_post),
    path('trainer_adddietplan_post/', trainer_adddietplan_post),
    path('trainer_viewdietplan_post/', trainer_viewdietplan_post),
    path('trainer_changepwd_post/', trainer_changepwd_post),

    path('trainer_viewprofile/', trainer_viewprofile),
    path('trainer_addposture/', trainer_addposture),
    path('trainer_viewposture/', trainer_viewposture),
    path('trainer_playvideo/', trainer_playvideo),
    path('trainer_editposture/<id>', trainer_editposture),
    path('trainer_viewuser/', trainer_viewuser),
    path('trainer_viewusermoredetails/<id>', trainer_viewusermoredetails),
    path('trainer_adddietplan/', trainer_adddietplan),
    path('trainer_viewdietplan/', trainer_viewdietplan),
    path('trainer_editdietplan/<id>', trainer_editdietplan),
    path('trainer_editdietplan_post/', trainer_editdietplan_post),
    path('trainer_deletetdiet/<id>', trainer_deletetdiet),
    path('trainer_querychat/', trainer_querychat),
    path('trainer_changepwd/', trainer_changepwd),
    path('trainer_changepwd_post/', trainer_changepwd_post),
    path('trainer_logout/', trainer_logout),
    path('trainer_homepage/', trainer_homepage),

    path('trainer_addchallenge/', Traineraddchallenges.as_view()),
    path('trainer_viewchallenge/', Trainerviewchallenges.as_view()),
    path('trainer_viewchallengepost/', Trainerviewchallengespost.as_view()),
    path('trainer_editchallenge/<data>', Trainerupdatechallenges.as_view()),
    path('trainer_deletetchallenge/<data>', Trainerdeletechallenges.as_view()),

    path('trainer_addtask/', Traineraddtask.as_view()),
    path('trainer_viewtask/', Trainerviewtask.as_view()),
    path('trainer_viewtaskpost/', Trainerviewtaskpost.as_view()),
    path('trainer_edittask/<data>', Trainerupdatetask.as_view()),
    path('trainer_deletetask/<data>', Trainerdeletetask.as_view()),
    path('trainer_deletetask/trainer_viewuser/', Trainerdeletetask.as_view()),

    # api
    path('traineradddiet/', Viewdietapiview.as_view()),
    path('traineradddiet/<int:data>', Viewdietapiview.as_view()),
    path('trainerviewuserapi/',Viewuserprofileapiview.as_view()),
    # path('trainerviewuserapi/<int:data>',Viewtrainerprofileapiview.as_view()),
    path('trainerregistration/<int:pk>',UserprofileCreateAPIView.as_view()),
    path('traineraddposture/',Viewposture.as_view()),
    path('traineraddposture/<int:id>',Viewposture.as_view()),
    path('trainerputposture/<int:id>', Viewputposture.as_view()),
    path('trainerdeleteposture/<int:id>', Viewdeleteposture.as_view()),
    path('traineraddtask/', Viewtask.as_view()),
    path('traineraddtask/<int:id>', Viewtask.as_view()),
    path('traineraddchallenges/', Viewchallenges.as_view()),
    path('traineraddchallenges/<int:id>', Viewchallenges.as_view()),
    path('trainerchatapi/<fromid>/<toid>',ChatAPIView.as_view()),
    path('trainerchatapipost/',ChatAPIViewPOST.as_view()),
    path('trainerchat/<fromid>/<toid>', ChatView.as_view()),
    path('trainerchatpost/', ChatViewPOST.as_view(),name='send_message'),
    path('view_chat_history/', view_chat_history, name='view_chat_history'),
    path('viewcategorylist/',viewcategorylist.as_view(),name='viewcategorylist'),

    path('viewdata/',Viewdata.as_view(),name='viewdata')

]