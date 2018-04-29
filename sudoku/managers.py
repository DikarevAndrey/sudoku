from django.db import models
from django.db.models.aggregates import Count
from random import randint


class SudokuTableManager(models.Manager):
  def get_random(self):
    count = self.all().count()
    # count = self.aggregate(count=Count('id'))['count']
    random_index = randint(0, count - 1)
    return self.all()[random_index]