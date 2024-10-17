from .views import send_email,user_viewset,login
# from .views import login,create_user,send_email

from django.urls import path, include




urlpatterns=[
    #path('', include(router.urls)),
    # path('create_user',create_user),
    path('login',login),
    path('send_email',send_email),
]