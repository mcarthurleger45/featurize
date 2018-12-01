from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ProductArea(models.Model):
    area = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.area

class FeatureRequest(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    target_date = models.DateTimeField()
    client = models.ForeignKey(Client, related_name='clients', on_delete=models.SET_NULL, null=True)
    product_area = models.ForeignKey(ProductArea, related_name='products', on_delete=models.SET_NULL, null=True)
    priority = models.IntegerField()
    user = models.ForeignKey(User, related_name='feature_requests', on_delete=models.CASCADE)

    def __str__(self):
        return('[{product}] :: [{title}] by {username}'.format(product=self.product_area, title=self.title, username=self.client))

    @staticmethod
    def reorder(fr, priority):
        exists = FeatureRequest.objects.exclude(id=fr.id).filter(priority = priority)
        if len(exists) > 0:
            elem = exists[0]
            elem.priority = priority + 1
            elem.save()
            FeatureRequest.reorder(elem, elem.priority)
        else:
            return

    def save(self, *args, **kwargs):
        super(FeatureRequest, self).save(*args, **kwargs)
        FeatureRequest.reorder(self, self.priority)
