from django.urls import path
from . import views

app_name = 'ocr'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('doc/<int:pk>', views.DocView.as_view(), name='doc')
]