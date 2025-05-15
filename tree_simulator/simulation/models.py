from django.db import models
import random

class Branch(models.Model):
    def grow_fruit(self):
        if random.random() < 0.5:
            Fruit.objects.create(
                size=random.uniform(2.0, 4.0),
                branch=self  # set reverse link
            )

    def grow(self):
        for fruit in self.fruit_set.all():
            fruit.grow()
        self.grow_fruit()

class Fruit(models.Model):
    branch = models.ForeignKey(Branch, related_name='fruit_set', on_delete=models.CASCADE) # 🔧 this enables branch.fruit_set
    type = models.CharField(max_length=20, default='Apple')
    size = models.FloatField(default=2.0)
    ripeness = models.IntegerField(default=0)

    def grow(self):
        self.ripeness = min(100, self.ripeness + random.randint(5, 15))
        self.save()

    def __str__(self):
        return f"{self.type} ({self.size:.1f}cm, {self.ripeness}%)"

class Tree(models.Model):
    name = models.CharField(max_length=50)
    branches = models.ManyToManyField(Branch)

    def grow(self):
        for branch in self.branches.all():
            branch.grow()
