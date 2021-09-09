from django.shortcuts import render

from .models import CourseDetailes,Contact
from .forms import ContactForm
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
    return render(request,'INS/mail.html')