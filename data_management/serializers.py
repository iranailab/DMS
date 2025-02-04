from rest_framework import serializers
from .models import Dataset, Tag, Category, Organization, Resource, License, ResourceFormat


class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class ResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resource
        fields = '__all__'


class DatasetSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    organization = OrganizationSerializer(read_only=True)
    resources = ResourceSerializer(many=True, read_only=True)
    license = LicenseSerializer(read_only=True)

    class Meta:
        model = Dataset
        fields = '__all__'

class ResourceFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceFormat
        fields = '__all__'
