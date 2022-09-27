import numpy as np 
import matplotlib.pyplot as plt

def sirkel(x,y,r):
    #lager en array fra 0 - 2pi med 100 i mellomrom
    t = np.linspace(0, 2*np.pi, 100)
    #plotter x aksen og y aksen med 2 i tykkelse
    plt.plot(x + r*np.cos(t), y + r*np.sin(t), linewidth = 1)
    plt.axis("equal")

#denne lager matrise
A = np.array([[-2, 0, 1/2, 1], [-1/4, 1, 1/4, 0], [0, 0, 3, -1], [1/8, 1/8, 1/4, 2]])

#lager en 4 lang array med 0 inni
x = np.zeros(len(A))

#lager en 4 lang array med 0 inni
r = np.zeros(len(A))

#forloop 
for y in range(len(A)): 
    #fyller x med verdier fra arrayen diagonalt
    x[y] =  A[y][y]
    #forloop for å summere
    for z in range(len(A)):
        #adderer verdien fra hvert av kolonnene fra A til r
        r[y] = r[y] + abs(A[y,z])
    #tar r og substraherer y fra den
    r[y] = r[y]-abs(x[y])
    z = 0

#for hver x
for y in x:
    sirkel(x[z], 0, r[z])
    z += 1

#bruker eig() som returnerer egenverdi og egenvektor for en matrise
egenverdi, egenvektor = np.linalg.eig(A)

#for loop for plotting
for teller in range(len(egenverdi)):
    #lager dottene
    plt.plot(np.real(egenverdi[teller]), np.imag(egenverdi[teller]), '.', markersize = 20)

#viser plotten
plt.show()
