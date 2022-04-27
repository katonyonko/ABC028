import io
import sys

_INPUT = """\
6
3 2
3 1
765 573
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  N,K=map(int,input().split())
  print(((K-1)*(N-K)*6+(K-1+N-K)*3+1)/(N**3))