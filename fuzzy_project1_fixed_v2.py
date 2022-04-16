import numpy
import matplotlib.pyplot as plt

#Funciones para trabajar Conjuntos Difusos:

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

#Valores Difusos

ng = [-1.0,-1.0,-0.8,-0.5]
nm = [-0.8,-0.5,-0.4,-0.2]
np = [-0.4,-0.3,-0.2,-0.1]
ni = [-0.2,-0.1, 0.0, 0.0]
ce = [-0.2, 0.0, 0.0, 0.2]
pi = [ 0.0, 0.0, 0.1, 0.2]
pp = [ 0.1, 0.2, 0.3, 0.4]
pm = [ 0.2, 0.4, 0.5, 0.8]
pg = [ 0.5, 0.8, 1.0, 1.0]

#Reglas Difusas

flc_rules = [[          ng, de_a(ng,pp), pg],
			 [ de_a(ng,nm), de_a(ng,np), pm],
			 [          np, de_a(np,pi), pm],
			 [          ni, de_a(ng,nm), pm],
			 [          ni, de_a(pm,pg), np],
			 [ de_a(ni,pi),          ce, ce],
			 [          pi, de_a(ng,nm), pp],
			 [          pi, de_a(pm,pg), nm],
			 [          pp, de_a(np,pg), nm],
			 [ de_a(pm,pg), de_a(pp,pg), nm],
			 [          pg, de_a(np,pg), ng],
			 [          ni,          pp, ce],
			 [          ni,          np, pp],
			 [          pi,          np, ce],
			 [          pi,          pp, np],
			 [ de_a(ng,np), de_a(pm,pg), pg],
			 [ de_a(pp,pg), de_a(ng,nm), ng]]

#Mapa de Reglas

def rule_map(rules):
    vert = [0,0,1,1,0,0]
    fig, axs = plt.subplots(len(rules),3, figsize=(12, 2*len(rules)))
    for i, rule in enumerate(rules):
        E1 = rule[0]
        E2 = rule[1]
        S1 = rule[2]
        
        axs[i][0].plot([-1,*E1,1], vert, color="olive")
        axs[i][0].grid(axis='y')
        axs[i][0].set_ylabel(f"Rule {i+1}", fontsize=24)
        
        axs[i][1].plot([-1,*E2,1],vert, color="blue")
        axs[i][1].grid(axis='y')
        
        
        axs[i][2].plot([-1,*S1,1],vert, color="orange")
        axs[i][2].grid(axis='y')
    #Titles
    fig.tight_layout()
    fig.subplots_adjust(top=0.95)
    fig.suptitle("Rule Map", fontsize=40)
    axs[0][0].set_title('E1', fontsize=24)
    axs[0][1].set_title('E2', fontsize=24)
    axs[0][2].set_title('S1', fontsize=24)
    plt.show()

#Maqina de Inferencia

def FIS(E1, E2, rules, method="COG", samples=41, ran=[-1.0,1.0]):
    d = numpy.abs(ran[1]-ran[0])
    sampling = numpy.arange(ran[0],ran[1],step=d/samples)
    out = numpy.zeros_like(sampling)
    t_rules = []
    for n, rule in enumerate(rules):
        h = min(memb_grade(E1,de_a(rule[0],rule[1])),
          memb_grade(E2,de_a(rule[2],rule[3])))
        if h>0: t_rules.append(n+1)
        for i, x in enumerate(sampling):
            f_x = min(h,memb_grade(x,rule[4]))
            out[i] = max(out[i],f_x)
            
    if method == "COG":
        if numpy.sum(out) == 0:
            S = 0
        else:
            S = numpy.sum(out*sampling)/numpy.sum(out)
        
    if method == "MMP":
        if numpy.sum(out) == 0:
            S = 0
        else:
            max_value = numpy.max(out)
            max_idx =out.index(max_value)
            S = sampling[max_idx]
    
    if method == "MOM":
        if numpy.sum(out) == 0:
            S = 0
        else:
            max_value = numpy.max(out)
            suma = 0
            count = 0
            for h in out:
                if h == max_value:
                    suma+= h
                    count+= 1
            S = suma/count
    
    return S, sampling, out, t_rules

rule_map(flc_rules)