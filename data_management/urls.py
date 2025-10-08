from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    DatasetViewSet, TagViewSet, CategoryViewSet, OrganizationViewSet,
    ResourceViewSet, LicenseViewSet, MembershipViewSet, TrackingViewSet,
    track_dataset_view, track_dataset_download, track_organization_view, track_category_view
)

# Create a router and register viewsets
router = DefaultRouter()
router.register(r'datasets', DatasetViewSet)
router.register(r'tags', TagViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'resources', ResourceViewSet)
router.register(r'licenses', LicenseViewSet)
router.register(r'memberships', MembershipViewSet)
router.register(r'tracking', TrackingViewSet, basename='tracking')

# Define app-level URLs
urlpatterns = [
    path('track/dataset/<int:dataset_id>/view/', track_dataset_view, name='track_dataset_view'),
    path('track/dataset/<int:dataset_id>/download/', track_dataset_download, name='track_dataset_download'),
    path('track/organization/<int:organization_id>/view/', track_organization_view, name='track_organization_view'),
    path('track/category/<int:category_id>/view/', track_category_view, name='track_category_view'),
] + router.urls
