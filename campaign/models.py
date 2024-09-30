from django.db import models
from django.db.models import Q
from django.utils import timezone


# Create your models here.
class Campaign(models.Model):
    class Meta:
        db_table = "campaigns"

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image_path = models.ImageField(
        upload_to='uploads/',
        blank=False,
        default='default/campaign-thumbnail.jpg'
    )
    how_help = models.TextField(max_length=500)
    votes = models.IntegerField(default=0)
    limit_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def search_by_term(query: str):
        return Campaign.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(how_help__icontains=query),
            limit_date__gte=timezone.now()
        ).order_by('-votes', '-id')

    def list_all():
        return Campaign.objects.filter(
            limit_date__gte=timezone.now()
        ).order_by('-votes', '-id')
