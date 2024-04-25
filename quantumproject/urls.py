from django.contrib import admin
from django.urls import path
from quantum import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("about/", views.about, name="about"),
    path("enroll/", views.enroll, name="enroll"),
    path("contactus/", views.contactus, name="contactus"),
    path("lowerschool/", views.lowerschool, name="lowerschool"),
    path("middleschool/", views.middleschool, name="middleschool"),
    path("highschool/", views.highschool, name="highschool"),
    path("formsubmitted/", views.formsubmitted, name="formsubmitted"),
    path('lower_school_registration/', views.lower_school_registration, name='lower_school_registration'),
    path('middle_school_registration/', views.middle_school_registration, name='middle_school_registration'),
    path('high_school_registration/', views.high_school_registration, name='high_school_registration'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('contact_homepage/', views.contact_homepage, name='contact_homepage'),


]