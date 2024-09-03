from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

# Маршруты для личного кабинета
urlpatterns = [path('account/save-report/', views.save_report, name='save_report'),
               path('account/start-detection/', views.start_detection, name='start_detection'),
               path('account/upload-image/', views.upload_image, name='upload_image'),
               path('account/', views.account, name='account'),
               path('logout/', login_required(auth_views.LogoutView.as_view()), name='logout'),
               path('login/', auth_views.LoginView.as_view(), name='login'),
               path('', views.home, name='home',)]