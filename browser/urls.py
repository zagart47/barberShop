from django.conf.urls.static import static
from django.urls import path

from barberShop import settings
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('barbers/', barbers, name='barbers'),
    path('barbers/<int:barber_id>/', barber_details, name='barberdetails'),
    path('service/', service, name='service'),
    path('contacts/', contacts, name='contacts'),
    path('enroll/', enroll, name='enroll'),
    path('gallery/', gallery, name='gallery'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)