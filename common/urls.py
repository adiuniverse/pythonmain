from django.urls import path,include
from . import views
app_name = "common"
urlpatterns = [
   path('index',views.common_index,name='index'),
   path('about/',views.common_about,name='about'),
   path('contact',views.common_contact,name='contact'),
   path('courses',views.common_courses,name='courses'),
   path('index',views.common_index,name='index'),
   path('team',views.common_team,name='team'),
   path('testimonial',views.common_testimonial,name='testimonial'),
   path('404',views.common_404,name='404'),
   path('commonmaster',views.common_commonmaster,name='commonmaster'),
   path('login',views.common_login,name='login'),
   path('techadminlogin',views.common_techadminlogin,name='techadminlogin'),
   path('techadminregister',views.common_techadminregister,name='techadminregister'),
   path('trainerlogin',views.common_trainerlogin,name='trainerlogin'),
   path('studentlogin',views.common_studentlogin,name='studentlogin'),
   path('studentregister',views.common_studentregister,name='studentregister'),
   path('trainerregister',views.common_trainerregister,name='trainerregister'),

]
