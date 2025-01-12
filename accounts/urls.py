from django.urls import path
from django.contrib.auth import views as auth_views  # BU YERDA IMPORT QILISH KERAK!
from .views import SignUpView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Django login view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Django logout view
    path('signup/', SignUpView.as_view(), name='signup'),  # Ro‘yxatdan o‘tish view
]
