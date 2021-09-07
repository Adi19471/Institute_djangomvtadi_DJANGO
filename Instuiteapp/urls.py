from django.urls import path
from Instuiteapp import views 


urlpatterns = [
    path('',views.home_view,name="home"),
    path('ser/',views.services_view,name="services"),
    path('gal/',views.gallery_view,name="gallery"),
    path('con/',views.conatct_view,name="contact"),
    path('feed/',views.feedback_view,name="feedback"),
    path('mail/',views.mail_view,name="mail"),

]