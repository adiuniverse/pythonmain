from django.shortcuts import render
from . models import Teachers
from . models import Course
from . models import Batch
from trainer . models import AddStudent
# Create your views here.
def techadmin_master(request):
    return render(request,'tech/master.html')
def techadmin_home(request):
    return render(request,'tech/home.html')  


def techadmin_addtrainers(request):
    msg = ""
    if request.method == 'POST':
        t_name = request.POST['fname']
        t_phone = request.POST['phonenumber']
        t_address = request.POST['address']
        t_gender = request.POST['gender']
        t_email = request.POST['email']
        t_username = request.POST['username']
        t_password = request.POST['password']
        t_experience = request.POST['experience']
        new_teachers = Teachers(name = t_name, phone = t_phone, address = t_address, gender = t_gender,
                                email = t_email, username = t_username, password = t_password,
                                experience = t_experience)
        new_teachers.save()
        msg = "Successfully Added The Trainer"
    return render(request,'tech/addtrainers.html', {'message':msg}) 



def techadmin_liststudents(request):
    student_data = AddStudent.objects.all()
    return render(request,'tech/liststudents.html',{'student_list':student_data})  


def techadmin_schedulebatch(request):

    if request.method == 'POST':
        b_name = request.POST['name']
        b_day = request.POST['day']
        b_start = request.POST['start']
        b_end = request.POST['end']
        new_batch = Batch(name = b_name, day = b_day, start = b_start, end = b_end)
        new_batch.save()
    return render(request,'tech/schedulebatch.html')




def techadmin_addcourse(request):
    msg = ""
    if request.method == 'POST':
        cs_name = request.POST['fname']
        cs_duration = request.POST['duration']
        cs_price = request.POST['payment']
        cs_image = request.FILES['file']

        course = Course(name = cs_name, duration = cs_duration, price = cs_price, image = cs_image)
        course.save()
        msg = "Course Added Successfully"
    return render(request,'tech/addcourse.html',{'message':msg})  


def techadmin_viewschedule(request):
    batch_data = Batch.objects.all()
    return render(request,'tech/viewschedule.html',{'batch_list':batch_data})       
    
 
def techadmin_viewtrainers(request):
    trainer_data = Teachers.objects.all()
    return render(request,'tech/viewtrainers.html',{'trainer_list' : trainer_data})  

def techadmin_viewcourse(request):
    course_data = Course.objects.all()
    return render(request,'tech/viewcourse.html',{'course_list' : course_data}) 

def techadmin_status(request):
    return render(request,'tech/status.html')  
def techadmin_logout(request):
    return render(request,'tech/logout.html')  
                                                                                                                                                                           