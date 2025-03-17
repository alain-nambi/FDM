from django.urls import path
from .views import MissionListView, HistoryView

urlpatterns = [
  #  path('', HomeView.as_view(), name='home'),
    path('', MissionListView.as_view(), name='missions'),
    path('history',HistoryView.as_view(),name='history'),
   # path('', MissionExpenseCreateView.as_view(), name='index'),
]
