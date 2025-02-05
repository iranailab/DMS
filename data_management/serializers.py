from rest_framework import serializers

from .models import Dataset, Tag, Category, Organization, Resource, License, ResourceFormat, Membership, Tracking
from django.contrib.auth.models import User


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


class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = ['tracking_type', 'dataset', 'organization', 'category', 'timestamp']


class DatasetSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    organization = OrganizationSerializer(read_only=True)
    resources = ResourceSerializer(many=True, read_only=True)
    license = LicenseSerializer(read_only=True)

    class Meta:
        model = Dataset
        fields = '__all__'

    def validate_organization(self, value):
        """Ensure the user is a member of the selected organization."""
        user = self.context['request'].user
        if not Membership.objects.filter(user=user, organization=value).exists():
            raise serializers.ValidationError("You are not a member of this organization.")
        return value
    
    def to_representation(self, instance):
        """Customize response to show only user's organizations when creating a dataset."""
        data = super().to_representation(instance)
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            user_organizations = Organization.objects.filter(membership__user=request.user)
            data['available_organizations'] = [
                {"id": org.id, "name": org.name} for org in user_organizations
            ]
        return data

class ResourceFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceFormat
        fields = '__all__'


class MembershipSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())

    class Meta:
        model = Membership
        fields = '__all__'

    def validate(self, data):
        """Ensure only organization owners can add new members."""
        request = self.context['request']
        user = request.user
        organization = data['organization']

        # Check if the requesting user is an owner of the organization
        if not Membership.objects.filter(user=user, organization=organization, role='owner').exists():
            raise serializers.ValidationError("Only organization owners can add members.")
        
        return data