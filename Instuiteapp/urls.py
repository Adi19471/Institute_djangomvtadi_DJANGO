from django.urls import path
from Instuiteapp import views 

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',views.home_view,name="home"),
    path('ser/',views.services_view,name="services"),
    path('gal/',views.gallery_view,name="gallery"),
    path('con/',views.conatct_view,name="contact"),
    path('feed/',views.feedback_view,name="feedback"),
    path('mail/',views.mail_view,name="mail"),

]
if settings.DEBUG:
    
    urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns  += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



