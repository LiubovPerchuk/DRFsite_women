from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView)

from women.views import WomenAPIList, WomenAPIUpdate, WomenAPIDestroy
# from rest_framework import routers


# router = routers.DefaultRouter()
# router.register(r"women", WomenViewSet, basename="women")
# router = routers.SimpleRouter()
# router.register(r"women", WomenViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/drf-auth/", include("rest_framework.urls")),
    path("api/v1/women/", WomenAPIList.as_view()),
    path("api/v1/women/<int:pk>/", WomenAPIUpdate.as_view()),
    path("api/v1/womendelete/<int:pk>/", WomenAPIDestroy.as_view()),
    path("api/v1/auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),
    path("api/v1/token/", TokenObtainPairView.as_view(),
         name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(),
         name="token_refresh"),
    path("api/v1/token/verify/", TokenVerifyView.as_view(),
         name="token_verify"),

    # path("api/v1/womenlist/", WomenViewSet.as_view({"get": "list"})),
    # path("api/v1/womenlist/<int:pk>/", WomenViewSet.as_view({"put ": "update"})),
    # path("api/v1/womenlist/", WomenAPIList.as_view()),
    # path("api/v1/womenlist/<int:pk>/", WomenAPIUpdate.as_view()),
    # path("api/v1/womendetail/<int:pk>/", WomenAPIDetailView.as_view()),
]
