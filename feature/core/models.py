from django.db import models

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

    def __str__(self):
        return('[{product}] :: [{title}] by {username}'.format(product=self.product_area, title=self.title, username=self.client))
    
