from django.urls import re_path
from . import views


urlpatterns = [
    re_path(r'^drone-categories/$', views.DroneCategoryList.as_view(), name=views.DroneCategoryList.name),
    re_path(r'^category/(?P<pk>[0-9]+)$', views.DroneCategoryDetail.as_view(), name=views.DroneCategoryDetail.name),
    re_path(r'^drones/$', views.DroneList.as_view(), name=views.DroneList.name),
    re_path(r'^drone/(?P<pk>[0-9]+)$', views.DroneDetail.as_view(), name=views.DroneDetail.name),
    re_path(r'^pilots/$', views.PilotList.as_view(), name=views.PilotList.name),
    re_path(r'^pilot/(?P<pk>[0-9]+)$', views.PilotDetail.as_view(), name=views.PilotDetail.name),
    re_path(r'^competitions/$', views.CompetitionList.as_view(), name=views.CompetitionList.name),
    re_path(r'^competition/(?P<pk>[0-9]+)$', views.CompetitionDetail.as_view(), name=views.CompetitionDetail.name),
    re_path(r'^$', views.APIRoot.as_view(), name=views.APIRoot.name),
]
