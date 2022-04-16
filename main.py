if __name__ == '__main__':
    from Planta import Planta
    from Controlador import Controlador
    from utils import de_a

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

    p = Planta(600, 0)
    controller = Controlador(p, flc_rules, 700, 'COG')

    print(controller.control_plant())
