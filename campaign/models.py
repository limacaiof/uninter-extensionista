from django.db import models


# Create your models here.
class Campaign(models.Model):
    class Meta:
        db_table = "campaigns"

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image_path = models.ImageField(
        upload_to='uploads/',
        blank=False,
        default='static/img/default/campaign-thumbnail.jpg'
    )
    how_help = models.TextField(max_length=500)
    votes = models.IntegerField(default=0)
    limit_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
