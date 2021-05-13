from django.contrib import admin
from django.urls import path, include

from apps.chat.views import *

urlpatterns = [
    path('', index_view, name='index'),
    path('apps.chat/<int:section_id>/', SectionView.as_view(), name='chat'),

]
