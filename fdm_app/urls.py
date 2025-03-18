from django.urls import path
from .views import MissionListView, HistoryView, RegisterView , CustomLoginView ,CustomLogoutView

urlpatterns = [
    path('', MissionListView.as_view(), name='missions'),
    path('history/',HistoryView.as_view(),name='history'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    
    
]
