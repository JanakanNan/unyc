from django.db import models

# Create your models here.
class Biere(models.Model):
    ref = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def get_references(self):
        return self.ref + " , " + self.name + " , " + self.description

    def __repr__(self):
        return self.name + " is added"

class Comptoir(models.Model):
    pks = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def get_comptoirs(self):
        return self.pks + " , " + self.name

    def __repr__(self):
        return self.pks + "is added"

class Ranking(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)


    class Meta:
        unique_together = ['name']
        ordering = ['name']

    def __str__(self):
        return '%s: %s' % (self.name, self.description)

    def __repr__(self):
        return self.name + "is added"

class Stock(models.Model):
    biid = models.ForeignKey(Biere, related_name='bieres', on_delete=models.CASCADE)
    raid = models.ForeignKey(Ranking, related_name='rankings', on_delete=models.CASCADE, null=True)
    coid = models.ForeignKey(Comptoir, related_name='comptoirs', on_delete=models.CASCADE)
    stock = models.IntegerField()

    class Meta:
        unique_together = ['biid', 'stock']
        ordering = ['stock']

    def __str__(self):
        return '%d' % (self.stock)

    def get_stock(self):
        return self.biere.ref + " , " + self.biere.name + " , " + self.biere.description + " , " + self.stock

    def __repr__(self):
        return self.stock + "is added"






