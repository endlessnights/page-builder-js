from django.db import models

class PageComponent(models.Model):
    COMPONENT_TYPES = (
        ('image_gallery', 'Image Gallery'),
        ('title', 'Title'),
        ('text', 'Text'),
    )
    component_type = models.CharField(max_length=50, choices=COMPONENT_TYPES)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)
    in_container = models.BooleanField(default=False)
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']
