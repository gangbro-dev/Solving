import re

pat = "0110001011001"
pat = re.finditer("100+1+$", pat)
print(("YES", "NO")[re.match('(100+1+|01)+$', input()) is None])
print(("YES", "NO")[re.match('(100+1+|01)+$', input()) is None])
