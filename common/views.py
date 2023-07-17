from django.shortcuts import render,redirect
from .models import Techadmin
from .models import Trainer
from .models import Student
from .models import Contact

# Create your views here.
def common_index(request):
    return render(request,'client/index.html')
def common_about(request):
    return render(request,'client/about.html')   


def common_contact(request):
    if request.method == 'POST':
        c_name = request.POST['name']
        c_email = request.POST['email']
        c_subject = request.POST['subject']
        c_message = request.POST['message']
        new_contact = Contact(name = c_name, email = c_email, subject = c_subject,
                             message = c_message )
        new_contact.save()
    return render(request,'client/contact.html')



def common_courses(request):
    return render(request,'client/courses.html')
def common_team(request):
    return render(request,'client/team.html')
def common_testimonial(request):
    return render(request,'client/testimonial.html')
def common_404(request):
    return render(request,'client/404.html')
def common_commonmaster(request):
    return render(request,'client/commonmaster.html')  
def common_login(request):
    return render(request,'client/login.html') 


def common_techadminlogin(request):
    msg = ""
    if request.method == 'POST':
        t_username = request.POST['username']
        t_password = request.POST['password'] 

        try:

            techadmin = Techadmin.objects.get(username = t_username, password = t_password)
            request.session['techadmin'] = techadmin.id
            return redirect('techadmin:home')

        except Exception as e:
            print(e)
            msg = "Techadmin Login Successfully"
    return render(request,'client/techadminlogin.html',{'message':msg}) 




def common_techadminregister(request):
    if request.method == 'POST':
        t_name = request.POST['fname']
        t_username = request.POST['username']
        t_password = request.POST['password']

        new_techadmin = Techadmin(name = t_name, username = t_username, password = t_password)
        new_techadmin.save()
    return render(request,'client/techadminregister.html')    



def common_trainerlogin(request):
    msg = ""
    if request.method == 'POST':
        t_username = request.POST['username']
        t_password = request.POST['password']
        try:

             trainer = Trainer.objects.get(username = t_username, password = t_password)
             request.session['trainer'] = trainer.id
             return redirect('trainer:home')

        except Exception as e:
            print(e)
            msg = "Trainer Login Successfully"
    return render(request,'client/trainerlogin.html',{'message':msg})   


def common_studentlogin(request):
    msg = ""
    if request.method == 'POST':
        s_username = request.POST['username']
        s_password = request.POST['password']
        try:
            student = Student.objects.get(username = s_username, password = s_password)
            request.session['student'] = student.id
            return redirect('student:home')
        except Exception as e:
            print(e)
            msg = "Student Login Successfully"
    return render(request,'client/studentlogin.html',{'message':msg}) 



def common_studentregister(request):
    
    if request.method == 'POST':
        s_name = request.POST['fname']
        s_email = request.POST['email']
        s_address = request.POST['address']
        s_phone = request.POST['phonenumber']
        s_gender = request.POST['gender']
        s_username = request.POST['username']
        s_password = request.POST['password']

        new_student = Student(name = s_name, email= s_email, address = s_address, phone = s_phone,
                             gender = s_gender, username = s_username, password =s_password)
        new_student.save()
    return render(request,'client/studentregister.html')




def common_trainerregister(request):

    if request.method == 'POST':
        t_name = request.POST['fname']
        t_email = request.POST['email']
        t_address = request.POST['address']
        t_phone = request.POST['phonenumber']
        t_gender = request.POST['gender']
        t_username = request.POST['username']
        t_password = request.POST['password']

        new_trainer = Trainer(name = t_name, email = t_email, address = t_address, phone = t_phone, gender = t_gender,
                               username = t_username, password = t_password)
        new_trainer.save()
    return render(request,'client/trainerregister.html')          
                        
                       
                     
      








