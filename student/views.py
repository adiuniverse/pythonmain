from django.shortcuts import render
from techadmin . models import Course
from techadmin . models import  Batch
from common . models import Student
from trainer . models import AddTask
from trainer . models import AddStudent

# Create your views here.
def student_master(request):
    return render(request,'study/master.html')

def student_home(request):
    return render(request,'study/home.html')

def student_courses(request):
   course_data = Course.objects.all()
   student_data = Student.objects.get(id = request.session['student'])
   courses_data = AddStudent.course_id
   context = {
              'student_list':student_data,
              'course_list':course_data}
   
   return render(request,'study/courses.html',{'course_list':course_data})  

def student_schedule(request):
    schedule_data = Batch.objects.all()
    return render(request,'study/schedule.html',{'schedule_list':schedule_data}) 

def student_task(request):
    task_data = AddTask.objects.all()
    return render(request,'study/task.html',{'task_list':task_data})   

def student_reviews(request):
    return render(request,'study/reviews.html')   

def student_logout(request):
    return render(request,'study/logout.html')

def student_profile(request):
    return render(request,'study/profile.html')                                                                                                                                                              