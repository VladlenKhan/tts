from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('certificate/',certificate,name='certificate'),
    path('complaint/', complaint, name='complaint'),
]