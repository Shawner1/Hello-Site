from django.urls import path
from helloapp.views import HelloWorldView

urlpatterns = [
    # helloapp/
    path('', HelloWorldView.as_view(), name='hello_world'),
]