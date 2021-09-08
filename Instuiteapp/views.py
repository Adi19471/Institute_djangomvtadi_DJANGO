from django.shortcuts import render

from .models import CourseDetailes

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
    return render(request,'INS/contact.html')



def feedback_view(request):
    return render(request,'INS/feedback.html')


def mail_view(request):
    return render(request,'INS/mail.html')