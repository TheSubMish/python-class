from django.urls import path

from .views import ChangePasswordAPI,LoginView,ForgetPasswordView,VerifyOtpView

# from .views
urlpatterns = [
    # path('user/',UserView.as_view({"get":"list","post":"create"})),
    # path('user/<int:pk>/',UserView.as_view()),
    path('login/',LoginView.as_view()),
    path('changepassword/',ChangePasswordAPI.as_view()),
    path('forgetpassword/',ForgetPasswordView.as_view()),
    path('verifyotp/',VerifyOtpView.as_view()),

]