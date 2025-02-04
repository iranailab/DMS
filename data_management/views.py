from django.shortcuts import render
from rest_framework import viewsets
from .models import Dataset, Tag, Category, Organization, Resource, License
from .serializers import DatasetSerializer, TagSerializer, CategorySerializer, OrganizationSerializer, ResourceSerializer, LicenseSerializer, ResourceFormatSerializer


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

class ResourceFormatViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = ResourceFormatSerializer
