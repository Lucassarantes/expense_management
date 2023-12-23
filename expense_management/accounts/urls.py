from django.urls import path
from .views import CustomLoginAPIView

urlpatterns = [
#     #path("/", views.home),
#     #path("logout", views.logout_view)
#      path(
#         "google_sso/", include("django_google_sso.urls", namespace="django_google_sso")
#     ),
    path('api/login/', CustomLoginAPIView.as_view(), name='api-login'),
]
