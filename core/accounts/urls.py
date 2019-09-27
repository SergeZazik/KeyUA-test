from django.urls import path

from core.accounts.views import RegistrationView

app_name = 'registration'
urlpatterns = [
    path('', RegistrationView.as_view(), name="join")
]
