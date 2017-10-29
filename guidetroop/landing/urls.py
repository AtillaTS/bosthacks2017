from django.conf.urls import url, include
from landing.views import HomeView

urlpatterns = [
    url(r'^', HomeView.as_view(), name='landing'),
]
