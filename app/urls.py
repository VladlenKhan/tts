from django.urls import path
from .views import *
urlpatterns = [
    path('',home,name='home'),
    path('certificate/',certificate,name='certificate'),
    path('complaint/', complaint, name='complaint'),
    path('application/', application_view, name='application_form'),
    path('feedback/', feedback_form, name='feedback_form'),
    path('price-list/', price_list, name='price_list'),
    path('agreement/', agreement, name='agreement'),
]