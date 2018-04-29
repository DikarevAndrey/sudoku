from django.db import models
from django.core.validators import validate_comma_separated_integer_list
from sudoku.managers import *


class SudokuTable(models.Model):
  quiz = models.CharField(validators=[validate_comma_separated_integer_list], max_length=200, blank=False)
  solution = models.CharField(validators=[validate_comma_separated_integer_list], max_length=200, blank=False)

  objects = SudokuTableManager()