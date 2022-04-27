import io
import sys

_INPUT = """\
6
1 2 3 4 5
1 2 3 5 8
"""

sys.stdin = io.StringIO(_INPUT)
case_no=int(input())
for __ in range(case_no):
  from itertools import combinations
  X=list(map(int,input().split()))
  ans=[]
  for k in combinations(range(5),3):
    ans.append(sum([X[k[i]] for i in range(3)]))
  ans.sort(reverse=True)
  print(ans[2])