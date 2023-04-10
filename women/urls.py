from django.urls import path,include,re_path
from .views import WomenApiList,WomenApiDelete,WomenApiUpdate

from rest_framework import routers



urlpatterns = [
    path('women/', WomenApiList.as_view()),
    path('women/update/<int:pk>', WomenApiUpdate.as_view()),
    path('women/delete/<int:pk>', WomenApiDelete.as_view()),
    path('women/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]