from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request,'INS/home.html')


def services_view(request):
    return render(request,'INS/services.html')



def gallery_view(request):
    return render(request,'INS/gallery.html')



def conatct_view(request):
    return render(request,'INS/contact.html')



def feedback_view(request):
    return render(request,'INS/feedback.html')


def mail_view(request):
    return render(request,'INS/mail.html')