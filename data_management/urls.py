from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DatasetViewSet, TagViewSet, CategoryViewSet, OrganizationViewSet, ResourceViewSet, LicenseViewSet, MembershipViewSet

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'datasets', DatasetViewSet)
router.register(r'tags', TagViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'resources', ResourceViewSet)
router.register(r'licenses', LicenseViewSet)
router.register(r'memberships', MembershipViewSet)

# Define app-level URLs
urlpatterns = [
    path('', include(router.urls)),  # Include all API endpoints
]