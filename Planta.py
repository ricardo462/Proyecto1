class Planta:
    def __init__(self, P_0, H_0, k=0.7) -> None:
        self.k = k
        self.H = H_0
        self.P = P_0

    def get_P(self):
        return self.P  
    
    def get_delta_P(self, delta_H):
        return self.k * delta_H

    def update(self, delta_H):
        self.H += delta_H
        self.P += self.get_delta_P(delta_H)
    
