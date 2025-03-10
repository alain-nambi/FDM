from django.urls import path
from .views import MissionListView

urlpatterns = [
  #  path('', HomeView.as_view(), name='home'),
    path('', MissionListView.as_view(), name='missions'),
    
]
