from django.contrib import admin
from django.urls import path
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('skills/', skills, name='skills'), 
]
