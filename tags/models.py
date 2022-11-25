from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.contenttypes.models import ContentType


# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    # what tag applies to what object
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # type of object (product, customer, order, etc.)
    # id of the object
    # using ContentType to get the type of the object and the id of the object (the object itself) "generic relation"
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
