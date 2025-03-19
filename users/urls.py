from django.urls import path,include
from . import views


urlpatterns=[
    path('',views.landing,name='landing'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('profile/',views.profilef,name='profile'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('logout/',views.logout,name='logout'),
]