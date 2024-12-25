from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_api.views import UserViewSet, AndroidAppViewSet, ScreenshotViewSet, CustomTokenObtainPairView

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')
router.register('apps', AndroidAppViewSet, basename='app')
router.register('screenshots', ScreenshotViewSet, basename='screenshot')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
