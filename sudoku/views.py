from django.shortcuts import render
from random import randint
from sudoku.models import *


def index(request):
  sudoku = SudokuTable.objects.get_random()

  quiz = list(map(int, sudoku.quiz.split(',')))
  solution = list(map(int, sudoku.solution.split(',')))

  context = {'quiz': quiz, 'solution': solution, 'range': range(9)}
  return render(request, 'index.html', context)