from django.urls import path
from account.views import SendPasswordResetEmailView, UserChangePasswordView, UserLoginView, UserProfileView, UserRegistrationView, UserPasswordResetView, UserDetailsView
urlpatterns = [
    path('api/register/', UserRegistrationView.as_view(), name='register'),
    path('api/user-details/', UserDetailsView.as_view(), name='user-details'),
    path('api/login/', UserLoginView.as_view(), name='login'),
    path('api/profile/', UserProfileView.as_view(), name='profile'),
    path('api/changepassword/', UserChangePasswordView.as_view(), name='changepassword'),
    path('api/send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('api/reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),

]