from math import pi

def moment_de_inertie(D,delta,h,ro):

    v=(pi*(D**2)/4)*h
    m=ro*v
    j=(m*((D/2)**2))/2 + (m*(delta**2))/2 
    return v,m,j

##D_arbore1 = 2 * (10 ** (-3))
##delta_arbore1 = 0
##h_arbore1 = 10*(10 ** (-3))
##ro_arbore1 = 7850
##arbore1 = moment_de_inertie(D_arbore1,delta_arbore1,h_arbore1,ro_arbore1)
##
##D_arbore2 = 2 * (10 ** (-3))
##delta_arbore2 = 0
##h_arbore2 = 15*(10 ** (-3))
##ro_arbore2 = 7850
##arbore2 = moment_de_inertie(D_arbore2,delta_arbore2,h_arbore2,ro_arbore2)
##
##D_principal = 10 * (10 ** (-3))
##delta_principal = 0
##h_principal = 15*(10 ** (-3))
##ro_principal1 = 7850 * 0.5
##ro_principal2 = 8960 * 0.5
##ro_principal = ro_principal1+ro_principal2
##piesa_principal = moment_de_inertie(D_principal,delta_principal,h_principal,ro_principal)
##
##
##piesa=[]
##
##piesa.append(arbore1[0]+arbore2[0]+piesa_principal[0])
##piesa.append(arbore1[1]+arbore2[1]+piesa_principal[1])
##piesa.append(arbore1[2]+arbore2[2]+piesa_principal[2])
##
##
##print ('Volumul piesei este de: ' + str(piesa[0]) + ' [m^3]')
##print ('Masa piesei este de: ' + str(piesa[1]) + ' [kg]')
##print ('Momentul de inertie al piesei este de: ' + str(piesa[2]) + ' [kg*m^2]')


