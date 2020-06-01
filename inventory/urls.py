from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name='index'),
    path('display_desktops/',display_desktops,name='display_desktops'),
    path('display_laptops/',display_laptops,name='display_laptops'),
    path('display_mobiles/',display_mobiles,name='display_mobiles'),

    path('add_laptop/',add_laptop,name='add_laptop'),
    path('add_desktop/',add_desktop,name='add_desktop'),

    path('edit_laptop/(?p<pk>)\d+)',edit_laptop,name='edit_laptop'),
    path('edit_desktop/(?p<pk>)\d+)',edit_desktop,name='edit_desktop'),



    path('delete_laptop/(?p<pk>)\d+)',delete_laptop,name='delete_laptop'),
    path('delete_desktop/(?p<pk>)\d+)',delete_desktop,name='delete_desktop'),







    
]