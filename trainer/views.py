from django.shortcuts import render
from . models import AddStudent
from .models import AddBatch
from . models import AddTask
from . models import AddstudentBatch
# Create your views here.

def trainer_master(request):
    return render(request,'teach/master.html')
def trainer_home(request):
    return render(request,'teach/home.html')


def trainer_addstudents(request):

    if request.method == 'POST':
        s_name = request.POST['fname']
        s_age = request.POST['age']
        s_address = request.POST['address']
        s_phone = request.POST['phonenumber']
        s_gender = request.POST['gender']
        s_education = request.POST['education']
        s_course = request.POST['course']
        s_courseid = request.POST['courseid']
        s_duration = request.POST['duration']
        s_email = request.POST['email']
        s_username = request.POST['username']
        s_password = request.POST['password']

        new_student = AddStudent(name = s_name, age = s_age, address = s_address,
                                phone = s_phone, gender = s_gender, education = s_education,
                                course = s_course, duration = s_duration, email = s_email,
                                username = s_username, password = s_password, course_id = s_courseid )
        new_student.save()
    return render(request,'teach/addstudents.html')



def trainer_batch(request):
    return render(request,'teach/batch.html')


def trainer_addbatch(request):

    if request.method == 'POST':
        b_name = request.POST['name']
        b_course = request.POST['course']
        b_duration = request.POST['duration']

        new_batch = AddBatch(name = b_name, course = b_course, duration = b_duration)
        new_batch.save()
    return render(request,'teach/addbatch.html')


def trainer_viewbatch(request):
    batch_data = AddBatch.objects.all
    return render(request,'teach/viewbatch.html',{'batch_list':batch_data })



def trainer_assigntaskbatch(request):

    if request.method == 'POST':
        t_name = request.POST['name']
        t_task = request.POST['task']
        t_description = request.POST['description']
        t_date = request.POST['date']

        new_task = AddTask(name = t_name, task = t_task, description = t_description, date = t_date)
        new_task.save()
    return render(request,'teach/assigntaskbatch.html')




def trainer_viewtask(request):

    task_data = AddTask.objects.all()

    return render(request,'teach/viewtask.html',{'task_list':task_data})

def trainer_addstudentsbatch(request):

    if request.method == 'POST':
        s_name = request.POST['sname']
        b_name = request.POST['bname']
        b_id = request.POST['bid']
        new_batch = AddstudentBatch(s_name = s_name, b_name = b_name, b_id = b_id)
        new_batch.save()
    return render(request,'teach/addstudentsbatch.html')

def trainer_viewstudentbatch(request):
    studentbatch_data = AddstudentBatch.objects.all()
    return render(request,'teach/viewstudentbatch.html',{'studentbatch_list':studentbatch_data})
def trainer_timesheet(request):
    return render(request,'teach/timesheet.html')
def trainer_logout(request):
    return render(request,'teach/logout.html')
def trainer_profile(request):
    return render(request,'teach/profile.html')
                   
               
           
                
               
           
                
           
            
           
               
           
           
           
       