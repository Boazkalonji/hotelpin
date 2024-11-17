from django.contrib import admin

from django.contrib import admin
from . models import *




admin.site.site_header = 'HOTEL PIN'
admin.site.site_title = 'hotelpin'
admin.site.register(Categories)
admin.site.register(Chambres)
admin.site.register(Comptes)
admin.site.register(Reservations)
admin.site.register(Message)
