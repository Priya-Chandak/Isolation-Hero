from django.conf.urls import include, url
from . import views1
from . import views



urlpatterns = [

  url(r'^googleapi/(?P<id>[0-9]+)/$', views1.GoogleAPI.as_view()), 

  url(r'^setting/(?P<id>[0-9]+)/$', views.SettingAPIView.as_view()),
  url(r'^setting/$', views.SettingAPIListView.as_view()), 
  
  url(r'^level/(?P<id>[0-9]+)/$', views.LevelAPIView.as_view()),
  url(r'^level/$', views.LevelAPIListView.as_view()),

  url(r'^rule/(?P<id>[0-9]+)/$', views.RuleAPIView.as_view()),
  url(r'^rule/$', views.RuleAPIListView.as_view()),

  url(r'^userisolationlocation/(?P<id>[0-9]+)/$', views.UserIsolationLocationAPIView.as_view()),
  url(r'^userisolationlocation/$', views.UserIsolationLocationAPIListView.as_view()),

  url(r'^userlocationhistory/(?P<id>[0-9]+)/$', views.UserLocationHistoryAPIView.as_view()),
  url(r'^userlocationhistory/$', views.UserLocationHistoryAPIListView.as_view()),

  url(r'^userlevelscore/(?P<id>[0-9]+)/$', views.UserLevelScoreAPIView.as_view()),
  url(r'^userlevelscore/$', views.UserLevelScoreAPIListView.as_view()),

  url(r'^movementreason/(?P<id>[0-9]+)/$', views.MovementReasonAPIView.as_view()),
  url(r'^movementreason/$', views.MovementReasonAPIListView.as_view()),

  url(r'^usermovement/(?P<id>[0-9]+)/$', views.UserMovementAPIView.as_view()),
  url(r'^usermovement/$', views.UserMovementAPIListView.as_view()),

  url(r'^userdailystat/(?P<id>[0-9]+)/$', views.UserDailyStatAPIView.as_view()),
  url(r'^userdailystatlist/(?P<id>[0-9]+)/$', views.UserDailyStatAPIListView.as_view()),

  url(r'^checkuserexists/(?P<email_id>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/$', views.UserExistsOrNotAPIView.as_view()),

  url(r'^userscore/(?P<id>[0-9]+)/$', views.UserScoreAPIListView.as_view()),
  url(r'^isolationlocationbyuser/(?P<id>[0-9]+)/$', views.UserwiseIsolcationLocationAPIListView.as_view()),

  url(r'^leaderboard/(?P<id>[0-9]+)/$', views.LeaderboardView.as_view()),

  url(r'^bonuspointlink/(?P<id>[0-9]+)/$', views.BonusPointLinkAPIView.as_view()),
  url(r'^bonuspointlink/$', views.BonusPointLinkListView.as_view()),

  url(r'^bonuspointlinkclicked/(?P<user_id>[0-9]+)/(?P<bonus_point_link_id>[0-9]+)/$', views.UserClickedBonusLinkOrNotAPIView.as_view()),

  url(r'^uservisitbonuspoint/(?P<id>[0-9]+)/$', views.UserVisitBonusPointAPIView.as_view()),
  url(r'^uservisitbonuspoint/$', views.UserVisitBonusPointListView.as_view()),

  url(r'^activebonuspointlink/(?P<user_id>[0-9]+)/$', views.ActiveBonusLinksAPIView.as_view()),

  url(r'^instruction/(?P<id>[0-9]+)/$', views.InstructionAPIView.as_view()),
  url(r'^instruction/$', views.InstructionAPIListView.as_view()),

  url(r'^userprofile/(?P<id>[0-9]+)/$', views.UserProfileAPIView.as_view()),
  url(r'^userprofile/$', views.UserProfileAPIListView.as_view()),

]
