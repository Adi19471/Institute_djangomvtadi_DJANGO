from django.shortcuts import render

from .models import CourseDetailes,Contact, Email
from .forms import ContactForm



from django.core.mail import message, send_mail
from InstuiteProject import settings  
from django.shortcuts import HttpResponse
from InstuiteProject.settings import EMAIL_HOST_USER
#-------------------------------------------------------------------------------------------------------------
def home_view(request):
    return render(request,'INS/home.html')


def services_view(request):
    course_data = CourseDetailes.objects.all()
    print(course_data)

    context = {
        'course':course_data
    }
    return render(request,'INS/services.html',context)



def gallery_view(request):
    return render(request,'INS/gallery.html')



def conatct_view(request):

    if request.method =="POST":
        fm = ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm = ContactForm()
    return render(request,'INS/contact.html',{'fm':fm})



def feedback_view(request):
    return render(request,'INS/feedback.html')


def mail_view(request):

   if request.method =="POST":

       sub = request.POST.get('name')
       to = request.POST.get('email')
       msg = request.POST.get('ms')

       email = Email(name=sub,email=to,message=msg)

       email.save()
       email = send_mail(sub,msg,EMAIL_HOST_USER,[to])

       print(email)
       if email:
           return HttpResponse("sent")
       else:
           return HttpResponse("Not sent")
   return render(request,'INS/mail.html')





