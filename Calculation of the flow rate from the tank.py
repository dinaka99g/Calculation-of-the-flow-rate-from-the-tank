
from cmath import pi
import matplotlib.pyplot as plt

h=10     #visina tecnosti u rezervoaru
g=9.81   #gravitaciono ubrzanje
L=100    #duzina cijevi
lamda=0.015
d1=1
d2=0.2
l=100
ksi=50
A1=d1**2*pi/4
A2=d2**2*pi/4



dt=0.1   #vremenski korak
v1_0=0    #v1 u pocetnom trenutku
v2_0=0   #izlazna brzina u pocetnom trenutku

t=0   #trenutno vrijeme na pocetku nula 
abc=True

t_ukupno=30 #ukupno vrijeme simulacije
n_dt=int(t_ukupno/dt) #broj vremenskih koraka
data_t=[]
data_v2=[]

for k in range (1,n_dt+1): #ne izvrsava se ovaj korak n_dt+1
   
    t=t+dt
    v2=v2_0+dt/L*(v1_0**2/2-v2_0**2/2+g*h-(lamda*L/d2+ksi)*v2_0**2/2) #sejv svaki put drugu v2_0

    v2_0=v2 #smjena stare i nove vrijednosti, onda taj ide u drugi korak
 
    print(k, t, v2, v2_0) 
    data_t.append(t)
    data_v2.append(v2)

    if (abc):
        v1=v2*A2/A1
        h=h-v1*dt
    else:
        v1_0=v1



slika=plt.figure(figsize=(8,6))

dijagram=plt.subplot(1,1,1) #koristimo matricni raspored dijagrama, koristimo jedan, matrica 1x1, ako hocemo 2 onda 2,2 ako hocemo (prvi broj vertikalno, drugi horizontalno)
l1=plt.plot(data_t,data_v2,c='r',ls='-',lw=5)
lx=plt.xlabel("vrijeme t[s]")
ly=plt.ylabel("brzina isticanja")

plt.savefig('brzina_isticanja_iz_rezervoara.png')
plt.show()

  




