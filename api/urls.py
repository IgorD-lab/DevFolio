from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    # Generate token on login submission 
    TokenObtainPairView,
    # Generate refresh token
    TokenRefreshView,
)

urlpatterns = [
    # Simple JSON urls 
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path('', views.getRoutes),
    path('projects', views.getProjects),
    path('projects/<str:pk>/', views.getProject),
    path('projects/<str:pk>/vote/', views.projectVote),
]