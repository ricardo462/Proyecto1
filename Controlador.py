from re import A
import numpy as np
from utils import memb_grade, de_a
class Controlador:
    def __init__(self, planta, reglas, PO, method) -> None:
        self.planta = planta
        self.reglas = reglas 
        self.PO = PO
        self.previous_TP = 0
        self.method = method

    def control_plant(self):
        delta_H = self.get_delta_H()
        self.planta.update(delta_H)
    
    def get_delta_H(self):
        EP = self.EP()
        TP = self.TP(EP)
        delta_H = self.FIS(EP, TP, self.reglas, self.method)
        return delta_H
    
    def EP(self):
        return self.planta.get_P() - self.PO

    def TP(self, EP):
        return EP - self.previous_TP

    
    def FIS(self, E1, E2, rules, method="COG", samples=41, ran=[-1.0,1.0]):
        d = np.abs(ran[1]-ran[0])
        sampling = np.arange(ran[0],ran[1],step=d/samples)
        out = np.zeros_like(sampling)
        t_rules = []
        for n, rule in enumerate(rules):
            a = memb_grade(E1,de_a(rule[0],rule[1]))
            b = memb_grade(E2,de_a(rule[2],rule[3]))
            h = min(a,b)
            if h>0: t_rules.append(n+1)
            for i, x in enumerate(sampling):
                f_x = min(h,memb_grade(x,rule[4]))
                out[i] = max(out[i],f_x)
                
        if method == "COG":
            if np.sum(out) == 0:
                S = 0
            else:
                S = np.sum(out*sampling)/np.sum(out)
            
        if method == "MMP":
            if np.sum(out) == 0:
                S = 0
            else:
                max_value = np.max(out)
                max_idx =out.index(max_value)
                S = sampling[max_idx]
        
        if method == "MOM":
            if np.sum(out) == 0:
                S = 0
            else:
                max_value = np.max(out)
                suma = 0
                count = 0
                for h in out:
                    if h == max_value:
                        suma+= h
                        count+= 1
                S = suma/count
        
        return S

    