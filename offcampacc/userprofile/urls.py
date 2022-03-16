from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name = 'userprofile/login.html'), name= 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'userprofile/logout.html'), name= 'logout'),
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(template_name = 'userprofile/password_reset.html'), name= 'password_reset'),
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(template_name = 'userprofile/password_reset_done.html'), name= 'password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name = 'userprofile/password_reset_confirm.html'), name= 'password_reset_confirm'),
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name = 'userprofile/password_reset_complete.html'), name= 'password_reset_complet')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)