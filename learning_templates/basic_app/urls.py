from django.urls import path
from . import views

#for template tagging
app_name = 'basicapp'           #this is the name represented in the {% %}   in html

urlpatterns = [
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative')
]
