from django.urls import path
from .views import MissionListView, HistoryView, RegisterView , CustomLoginView ,CustomLogoutView,EditMissionView,GeneratePDFView,ExportMissionsPDFView,ExportMissionExcelView, CreateTechnicianView
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MissionListView.as_view(), name='missions'),
    path('history/',HistoryView.as_view(),name='history'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('edit_mission/<int:mission_id>/', EditMissionView.as_view(), name='edit_mission'),
    path('mission/validate/', views.ValidateMissionView.as_view(), name='validate_mission'),
    path('mission/refuse/', views.RefuseMissionView.as_view(), name='refuse_mission'),
    path('mission/<int:mission_id>/download_pdf/', GeneratePDFView.as_view(), name='download_pdf'),
    path('export/pdf/', ExportMissionsPDFView.as_view(), name='export_pdf'),
    path('missions/<int:mission_id>/export-excel/', ExportMissionExcelView.as_view(), name='export_mission_excel'),
    path('missions/<int:mission_id>/export-csv/', views.ExportMissionCSVView.as_view(), name='export_mission_csv'),
    path('missions/<int:mission_id>/export-docx/', views.ExportMissionDocxView.as_view(), name='export_mission_docx'),
    path('mission/<int:mission_id>/upload-file/', views.UploadMissionFileView.as_view(), name='upload_mission_file'),
     path('technicians/create/', CreateTechnicianView.as_view(), name='create_technician'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)