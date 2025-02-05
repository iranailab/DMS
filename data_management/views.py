from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Dataset, Tag, Category, Organization, Resource, License, Membership
from .serializers import MembershipSerializer, DatasetSerializer, TagSerializer, CategorySerializer, OrganizationSerializer, ResourceSerializer, LicenseSerializer, ResourceFormatSerializer


class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer


class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    def get_permissions(self):
        """Set permissions based on action type."""
        if self.action in ['list', 'retrieve']:  # Allow everyone to see datasets
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]  # Require login for other actions
    
    def get_queryset(self):
        """Filter datasets based on user authentication."""
        user = self.request.user
        if user.is_authenticated:
            user_organizations = Organization.objects.filter(membership__user=user)
            return Dataset.objects.filter(models.Q(private=False) | models.Q(organization__in=user_organizations))
        return Dataset.objects.filter(private=False)  # Anonymous users see only public datasets

class ResourceFormatViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = ResourceFormatSerializer


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Allow users to see only their own memberships."""
        return Membership.objects.filter(user=self.request.user)