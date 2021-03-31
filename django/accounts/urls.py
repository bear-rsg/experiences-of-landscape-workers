from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    # Authentication views

    # Override login view to set it to redirect to home if user already logged in
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),

    # Include all default auth urls
    path('', include('django.contrib.auth.urls')),
    # More info: https://docs.djangoproject.com/en/3.1/topics/auth/default/#module-django.contrib.auth.views

    # Custom views
    path('profile/', views.AccountProfileTemplateView.as_view(), name='account-profile'),
    path('create/', views.AccountCreateView.as_view(), name='account-create'),
    path('create/success/', views.AccountCreateSuccessTemplateView.as_view(), name='account-create-success'),

]
