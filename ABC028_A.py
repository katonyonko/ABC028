import io
import sys

_INPUT = """\
6
80
100
59
95
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N=int(input())
  if N<=59: print('Bad')
  elif N<=89: print('Good')
  elif N<=99: print('Great')
  else: print('Perfect')