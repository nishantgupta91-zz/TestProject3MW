from django.db import models

class Sites(models.Model):
    siteName = models.CharField(max_length=20)
    def __str__(self):
        return self.siteName
        
class SiteProperties(models.Model):
    relatedSite = models.ForeignKey(Sites)
    date = models.DateTimeField('Date Published')
    aValue = models.DecimalField(max_digits=10, decimal_places=2)
    bValue = models.DecimalField(max_digits=10, decimal_places=2)