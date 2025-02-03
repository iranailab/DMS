from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    vocabulary_id = models.CharField(max_length=100, blank=True, null=True)  # Optional reference to a vocabulary
    display_name = models.CharField(max_length=200)  # Display-friendly name
    name = models.CharField(max_length=100, unique=True)  # Unique identifier
    state = models.CharField(max_length=10,
        choices=[('active', 'Active'), ('deleted', 'Deleted')],
        default='active')  # Status (e.g., 'active', 'deleted')

    def __str__(self):
        return self.display_name or self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)  # Unique category name
    title = models.CharField(max_length=200, blank=True)  # Display name
    description = models.TextField(blank=True, null=True)  # Explanation of category
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True)  # Nested categories
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)  # Track updates
    state = models.CharField(max_length=20, choices=[("active", "Active"), ("deleted", "Deleted")], default="active")
    image_url = models.URLField(blank=True, null=True)  # Optional image for the category

    def __str__(self):
        return self.title or self.name


class Organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)  # Unique identifier
    title = models.CharField(max_length=200, blank=True)  # Display name
    description = models.TextField(blank=True, null=True)  # Description
    image_url = models.URLField(blank=True, null=True)  # Organization logo
    website = models.URLField(blank=True, null=True)  # Organization website
    email = models.EmailField(blank=True, null=True)  # Contact email
    created = models.DateTimeField(auto_now_add=True)
    state = models.CharField(max_length=20, choices=[("active", "Active"), ("deleted", "Deleted")], default="active")

    def __str__(self):
        return self.title or self.name

class Dataset(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)  # Unique dataset name 
    title = models.CharField(max_length=255)  # Human-readable title
    description = models.TextField(blank=True, null=True)  # Long text description
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # The creator of the dataset
    tags = models.ManyToManyField(Tag, related_name='datasets', blank=True)  # Tags associated with dataset
    category = models.ForeignKey(Category, related_name='datasets', on_delete=models.SET_NULL, null=True, blank=True)  # Category reference

    created = models.DateTimeField(auto_now_add=True)  # Auto-set when created
    updated = models.DateTimeField(auto_now=True)  # Auto-set on update
    version = models.CharField(max_length=50, blank=True, null=True)  # Dataset version
    license = models.CharField(max_length=255, blank=True, null=True)  # License type
    visibility = models.CharField(
        max_length=10,
        choices=[('public', 'Public'), ('private', 'Private')],
        default='private'
    )  # Public/private dataset

    author = models.CharField(max_length=255, blank=True, null=True)  # Author name
    author_email = models.EmailField(blank=True, null=True)  # Author contact
    maintainer = models.CharField(max_length=255, blank=True, null=True)  # Maintainer name
    maintainer_email = models.EmailField(blank=True, null=True)  # Maintainer contact

    extras = models.JSONField(blank=True, null=True)  # Additional metadata as JSON

    def __str__(self):
        return self.title
