from django.contrib import admin
from .models import Dataset, Tag, Category, Organization, Resource, License


# Register models with customized admin views
admin.site.register(Dataset)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Organization)
admin.site.register(Resource)
admin.site.register(License)
