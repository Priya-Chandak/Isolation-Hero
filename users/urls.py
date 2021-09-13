from django.conf.urls import include, url
from api import views
from django.urls import path, re_path
from rest_auth.registration.views import VerifyEmailView, RegisterView
from rest_framework_jwt.views import verify_jwt_token
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token

urlpatterns = [
  path('rest-auth/', include('rest_auth.urls')),
  path('rest-auth/registration/', include('rest_auth.registration.urls')),
  url(r'^api-token-auth/', obtain_jwt_token),
  url(r'^api-token-refresh/', refresh_jwt_token),
  url(r'^api-token-verify/', verify_jwt_token),
  re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', VerifyEmailView.as_view(),
    name='account_confirm_email'),
  re_path(r'^account-confirm-email/', VerifyEmailView.as_view(),
     name='account_email_verification_sent'),    
]