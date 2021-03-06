from django.urls import path, re_path
from . import views as ds_views


urlpatterns = [
    path("drone_register/", ds_views.AircraftRegisterList.as_view(), name="sign_drone_list"),    
    path("drone_register/<uuid:pk>", ds_views.AircraftRegisterDetail.as_view(), name="sign_drone"),    

    path("register_drone/<uuid:pk>", ds_views.RegisterDrone.as_view(), name="register_drone"),    
    
    path("all_permissions/", ds_views.FlyDronePermissionApplicationList.as_view(), name="download_artefact"),    
    path("apply_permission/<uuid:pk>", ds_views.FlyDronePermissionApplicationDetail.as_view(), name="apply_permission"),
    path("download_permission_artefact/<uuid:pk>", ds_views.DownloadFlyDronePermissionArtefact.as_view(), name="download_artefact"),  
    
    path("uin_applications/", ds_views.UINApplicationList.as_view(), name="list_uins"),    
    path("uin_applications/<uuid:pk>", ds_views.FlyDronePermissionApplicationDetail.as_view(), name="uin_detail") , 
    path("submit_uin_application/<uuid:pk>", ds_views.SubmitUINApplication.as_view(), name="submit_uin_application"),   
]