from django.urls import path
from . views import *
from django.contrib.auth import views as auth
from .forms import CaptchaForm

urlpatterns = [
    path('',homeView,name='home'),
    path('detail/<int:id>/',detailView,name='detail'),
    path('update/<int:id>/',update_view,name='update'),
    path('delete/<int:id>/',delete_view,name='delete'),
    path('share/<int:id>/',share_view,name='share'),
    path('signup/',signupView,name='signup'),
    path('profile/',profileView,name='profile'),
    path('logout-user/',logoutView,name='logout-user'),
    path('login/', auth.LoginView.as_view(template_name='blogs/login.html', authentication_form=CaptchaForm), name='login'),
    path('logout/',auth.LogoutView.as_view(template_name='blogs/logout.html'),name='logout'),
    path('password_reset',auth.PasswordResetView.as_view(template_name='blogs/reset_password.html'),name='password_reset'),
    path('password_reset_done',auth.PasswordResetDoneView.as_view(template_name='blogs/reset_password_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>',auth.PasswordResetConfirmView.as_view(template_name='blogs/reset_password_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',auth.PasswordResetCompleteView.as_view(template_name='blogs/reset_password_complete.html'),name='password_reset_complete'),
]