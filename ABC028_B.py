import io
import sys

_INPUT = """\
6
BEAF
DECADE
ABBCCCDDDDEEEEEFFFFFF
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  S=input()
  C=['A','B','C','D','E','F']
  ans=[]
  for i in range(6):
    ans.append(S.count(C[i]))
  print(*ans)