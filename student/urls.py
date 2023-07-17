from django.urls import path,include
from . import views
app_name = "student"
urlpatterns = [
   path('master',views.student_master,name='master'),
   path('home',views.student_home,name='home'),
   path('courses',views.student_courses,name='courses'),
   path('schedule',views.student_schedule,name='schedule'),
   path('task',views.student_task,name='task'),
   path('reviews',views.student_reviews,name='reviews'),
   path('logout',views.student_logout,name='logout'),
   path('profile',views.student_profile,name='profile'),
   
]
