# courses/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='course_list'),
    path('profile/', views.profile, name='profile'),
    path('courses/<course_id>/', views.course_detail, name='course_detail'),
    path('enroll/<int:course_id>/', views.enroll, name='enroll'),
    path('complete/<int:enrollment_id>/<int:lesson_id>/', views.lesson_complete, name='lesson_complete'),
     path('login1/', views.login1, name='login1'),
      path('signup/', views.signup, name='signup'),
        path('logout1/', views.logout1, name='logout1'),
]
