from django.urls import path,include
from . import views
app_name = "trainer"
urlpatterns = [
   path('master',views.trainer_master,name='master'),
   path('home',views.trainer_home,name='home'),
   path('addstudents',views.trainer_addstudents,name='addstudents'),
   path('batch',views.trainer_batch,name='batch'),
   path('addbatch',views.trainer_addbatch,name='addbatch'),
   path('viewbatch',views.trainer_viewbatch,name='viewbatch'),
   path('assigntaskbatch',views.trainer_assigntaskbatch,name='assigntaskbatch'),
   path('viewtask',views.trainer_viewtask,name='viewtask'),
   path('addstudentsbatch',views.trainer_addstudentsbatch,name='addstudentsbatch'),
   path('viewstudentbatch',views.trainer_viewstudentbatch,name='viewstudentbatch'),
   path('timesheet',views.trainer_timesheet,name='timesheet'),
   path('logout',views.trainer_logout,name='logout'),
   path('profile',views.trainer_profile,name='profile'),
   
   
]
