from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('skills/', skills, name='skills'), 
    path('projects/', projects, name='projects'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.BASE_DIR / 'static')
