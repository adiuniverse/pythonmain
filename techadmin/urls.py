from django.urls import path,include
from . import views
app_name = "techadmin"
urlpatterns = [
   path('master',views.techadmin_master,name='master'),
   path('home',views.techadmin_home,name='home'),
   path('addtrainers',views.techadmin_addtrainers,name='addtrainers'),
   path('liststudents',views.techadmin_liststudents,name='liststudents'),
   path('schedulebatch',views.techadmin_schedulebatch,name='schedulebatch'),
   path('addcourse',views.techadmin_addcourse,name='addcourse'),
   path('viewschedule',views.techadmin_viewschedule,name='viewschedule'),
   path('viewtrainers',views.techadmin_viewtrainers,name='viewtrainers'),
   path('viewcourse',views.techadmin_viewcourse,name='viewcourse'),
   path('status',views.techadmin_status,name='status'),
   path('logout',views.techadmin_logout,name='logout'),
  
]
