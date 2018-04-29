from django.core.management.base import BaseCommand
from sudoku.models import *
import numpy as np


class Command(BaseCommand):
  help = 'Seeds database with data'

  def handle(self, *args, **options):
    for line in open('sudoku.csv', 'r').read().splitlines():
      quiz, solution = line.split(",")

      quiz_string = ''
      for c in quiz:
        quiz_string += c
        quiz_string += ','

      solution_string = ''
      for c in solution:
        solution_string += c
        solution_string += ','

      SudokuTable.objects.create(quiz=quiz_string[:-1], solution=solution_string[:-1])