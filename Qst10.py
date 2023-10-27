def existe_soma(S, x):
  S.sort()
  
  #Ponteiros
  p1 = 0
  p2 = len(S) - 1
  
  while p1 < p2:
    if S[p1] + S[p2] == x:
      return True
    elif S[p1] + S[p2] < x:
      p1 += 1
    else:
      p2 -= 1
  return False
  
S = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = 10

print(existe_soma(S, x))
