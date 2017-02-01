# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

n  = m = 600851475143 
s = 0 
c = 2
while(c*c <= m):
  if m%c == 0:
    m = m // c
    s = c
  else:
    if (c==2): c=3
    else: c=c+2
  
if m>s:
  s = m
  
print(s)
