from django.urls import re_path
from drones import views
from drones.v2 import views as v2_views


app_name = 'api-root'

urlpatterns = [
    re_path(r'^vehicle-categories/$', v2_views.DroneCategoryList.as_view(), name=v2_views.DroneCategoryList.name),
    re_path(r'^vehicle-categories/(?P<pk>[0-9]+)$', views.DroneCategoryDetail.as_view(), name=views.DroneCategoryDetail.name),
    re_path(r'^vehicles/$', v2_views.DroneList.as_view(), name=v2_views.DroneList.name),
    re_path(r'^vehicles/(?P<pk>[0-9]+)$', views.DroneDetail.as_view(), name=views.DroneDetail.name),
    re_path(r'^pilots/$', v2_views.PilotList.as_view(), name=v2_views.PilotList.name),
    re_path(r'^pilot/(?P<pk>[0-9]+)$', views.PilotDetail.as_view(), name=views.PilotDetail.name),
    re_path(r'^competitions/$', v2_views.CompetitionList.as_view(), name=v2_views.CompetitionList.name),
    re_path(r'^competition/(?P<pk>[0-9]+)$', views.CompetitionDetail.as_view(), name=views.CompetitionDetail.name),
    re_path(r'^$', v2_views.ApiRootVersion2.as_view(), name=v2_views.ApiRootVersion2.name),
]
