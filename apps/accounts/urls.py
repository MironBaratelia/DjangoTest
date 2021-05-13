from django.urls import include, path, reverse_lazy
from django_registration.backends.one_step.views import RegistrationView

from .forms import *
from .views import *

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path(
        'register/',
        RegistrationView.as_view(
            form_class=RegisterForm, success_url=reverse_lazy('index'),
        ),
        name='register',
    ),
    path('', include('django_registration.backends.one_step.urls')),
    path('', include('django.contrib.auth.urls')),
]