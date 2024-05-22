from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('take_test/', views.take_test, name='take_test'),
    path('submit_test/', views.submit_test, name='submit_test'),
    path('result_page/', views.result_page, name='result_page'),
    path('login/', auth_view.LoginView.as_view(template_name='first/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='first/logout.html'), name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
