from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

from accounts import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signin/", views.SignInView.as_view(), name="signin"),
    path("signout/", views.signout, name="signout"),
]
#urlpatterns += [re_path(r'^profile/(?P<username>[\w.@+-]+)/$', views.ProfileView.as_view(), name='profile'),]
urlpatterns += [path('profile/', views.ProfileView.as_view(), name='profile'),]
urlpatterns += [re_path(r'^profile/edit/(?P<pk>\d+)/$', views.EditProfileView.as_view(), name='edit-profile'),]
urlpatterns += [re_path(r'^profile/change_password/(?P<pk>\d+)/$', views.ChangePasswordView.as_view(), name='change-passw'),]
urlpatterns += [re_path(r'^profile/delete_user/(?P<pk>\d+)/$', views.DeleteProfileView.as_view(), name='delete-user'),]
urlpatterns += [path('reset_password/', views.ResetPasswordView.as_view(), name='reset-password'),]
urlpatterns += [path('reset_password/done/', 
                    auth_views.PasswordResetDoneView.as_view(template_name='reset/password_reset_mail_sent.html'),
                    name='email-sent'),]
urlpatterns += [path('password_reset_confirm/<uidb64>/<token>/', 
                    auth_views.PasswordResetConfirmView.as_view(template_name='reset/confirm_password_reset.html', success_url=reverse_lazy('accounts:complete-reset')),
                    name='confirm-reset'),]   
urlpatterns += [path('password_reset/complete/',
                    auth_views.PasswordResetCompleteView.as_view(template_name='reset/password_reset_complete.html'),
                    name='complete-reset'),]