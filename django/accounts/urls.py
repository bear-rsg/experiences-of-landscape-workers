from django.urls import path, include
from . import views

urlpatterns = [

    # Authentication views
    # More info: https://docs.djangoproject.com/en/3.1/topics/auth/default/#module-django.contrib.auth.views
    path('', include('django.contrib.auth.urls')),


    path('profile/', views.AccountProfileTemplateView.as_view(), name='account-profile'),
    path('create/', views.AccountCreateView.as_view(), name='account-create'),

]
