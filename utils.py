def memb_grade(a, X):
    if a < X[0] or a > X[3]: return 0
    elif a >= X[0] and a < X[1]: return (a-X[0])/(X[1]-X[0])
    elif a >=X[1] and a < X[2]: return 1
    elif a >=X[2] and a <= X[3]: return (X[3]-a)/(X[3]-X[2])

def de_a(A,B):
  if A[0]<B[0]: a = A[0]
  else: a = B[0]
  if A[1]<B[1]: b = A[1]
  else: b = B[1]
  if A[2]<B[2]: c = B[2]
  else: c = A[2]
  if A[3]<B[3]: d = B[3]
  else: d = A[3]
  return [a,b,c,d]
