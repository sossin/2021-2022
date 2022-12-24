import matplotlib.pyplot as plt #importa librerias de matematica
import numpy as np              #importa librerias de numeros
import scipy.special as sp      #biblioteca para crreacion de graficos
import pylab as pl              #importa librerias de pylab
from math import pi            #trae el numero pi de la libreria de mate
from math import log10       #comando de logaritmo base10
plt.close('all')

#variables ingresadas por el usuario

Vm= float(input('Ingrese el valor de la amplitud de la moduladora  --> '))
Fm= int(input('Ingrese el valor de la Frecuencia de la Moduladora  --> '))
Vc= float(input('Ingrese el valor de Amplitud de la portadora  --> '))
Fc= int(input('Ingrese el valor de la Frecuencia de la Portadora  --> '))
kf= float(input('Ingrese el factor de sensibilidad de frecuencia  --> '))
n= float(input('Ingrese el numero de periodos  --> '))
print()

#variables a usar

z= 50     # Impedancia de la portadora
Δf=kf*Vm  # Desviacion de frecuencia
β=Δf/Fm   # Indice de Modulacion

Fs=50000            #frecuencia de muestreo establecida
x=0                 #se indica a las variables a trabajar en 0
n0=[]               #vector vacio para ingresar los datos resultantes
bessel=[]           #vector vacio para ingresar los datos resultantes
f=np.arange(0,10,1) #vector en el que empesamos a trabajar

#Ecuaciones para hallar Bessel
for i in range (0,len(f)):   # realiza el calculo en cada vector
    x = round(sp.jv(i,β),2)  # funcion de bessel incluida en la libreria
    bessel.append(x)         # llena el vector besser antes declarado

n_positivos=bessel[1:11];         # componentes positivos de bessel
n_negativos=np.flip(n_positivos); # cambiar posiciones dentro del vector
n0.append(bessel[0]);             # definir el vector central

jn=np.concatenate((n_negativos,n0,n_positivos)) #unir los vectores

nB=4          # numero n presentes en bessel
BWb=2*Fm*nB   # Ancho de banda por Bessel
BWc=2*(Δf*Vm) # Ancho de banda por Carson

# Valores para las frecuencias

f_ns=[]        #definicion de vectores vacios
f_ps=[]        #definicion de vectores vacios
F0=[]          #definicion de vectores vacios
F0.append(Fc)  #Fija el vector F0 la FC como posicion central


for f_inicial in range(0,len(f)): #realiza el calculo para cada valor de f

    if f_inicial==0:    #creacion de una condicion para frecuencias negativas
        f_1=Fc-Fm;
        f_inicial=f_1;
    else:
        f_1=f_1-Fm;
        f_inicial=f_1;

    f_ns.append(f_inicial);

finv_ns=np.flip(f_ns);

for f_final in range(0,len(f)):

    if f_final==0:  #condicional para frecuencias positivas
        f_1=Fc+Fm;
        f_final= f_1;
    else:
        f_1=f_1+Fm;
        f_final=f_1;

    f_ps.append(f_final);    #llena el vector con los resultados
finv_ps=np.flip(f_ps);
Fn = np.concatenate((finv_ns,F0,f_ps)) #une componentes de frecuencias


t=np.arange(0,n*1/Fm,1/Fs)

#Hallar VC * Jn
f_VcJn=[]
VcJn=0
VcJn= np.round(abs((jn*Vc)/(np.sqrt(2))),2)
f_VcJn.append(VcJn) #llena el vector

#Hallar dB DE Jn*vC
f_VndB=[]
VndB=0

VndB=np.round(abs((20*np.log10(VcJn))),2)
f_VndB.append(VndB) #llena el vector

#Hallar LA POTENCIA EN WATTS

f_PnW=[]
PnW=0
PnW=abs(((jn*Vc)**2)/100)
f_PnW.append(PnW) #llena el vector

#Hallar LA POTENCIA EN dBm
f_PndBm=[]
PndBm=0

PndBm=np.round(abs((10*np.log10(PnW*1000))),2)#CALCULAMOS POTENCIA
f_PndBm.append(PndBm)

#Calculo de ecuaciones
Vportadora=Vc*np.cos(2*pi*Fc*t); #calculo de señal portadora
Vmoduladora=Vm*np.sin(2*pi*Fm*t); #calculo de señal moduladora
Vfm=Vc*np.cos(2*pi*Fc*t+β*np.sin(2*pi*Fm*t)); #calculo de modulacion

print('Resultado modulacion' )
print()
print('{:^10} {:^10} {:^10} {:^10}'.format('Δf','β','BWb','BWc'))
print('{:^10} {:^10} {:^10} {:^10}'.format(Δf,β,BWb,BWc))
print()
print('{:^10} {:^9} {:^9} {:^9} {:^9}'.format('Jn','Fn','Vc*Jn','Vn(dB)','Vn(dBm)','Vn(dBm)'))
for formatted in map ('{:^10} {:^10} {:^9} {:^10} {:^10}'.format,jn,Fn,VcJn,VndB, PndBm):
    print(formatted)
print()
print("LA ECUACION PORTADORA ES:")
print("Vc(t)=",Vc,"cos(2π",Fc,"t)")
print()
print("LA ECUACION MODULADORA ES:")
print("Vm(t)=",Vm,"sen(2π",Fm,"t)")
print()
print("LA ECUACION GENERAL ES:")
print("Vfm(t)=",Vc,"cos [2π",Fc,"t +",β, "sen(2π",Fm,"t)]")
print()


#Graficas
fig=plt.figure()
fig,plt.subplot(1,1,1)
plt.plot(t,Vportadora,color="blue",linewidth=0.8)
plt.title('Señal portadora')
plt.xlabel('Tiempo');
plt.ylabel('Amplitud');
plt.grid(True)

fig1=plt.figure()
fig1,plt.subplot(1,1,1)
plt.plot(t,Vmoduladora,color="black",linewidth=0.8)
plt.title('Señal Moduladora')
plt.xlabel('tiempo');
plt.ylabel('amplitud');
plt.grid(True)

fig2=plt.figure()
fig2,plt.subplot(1,1,1)
plt.plot(t,Vfm,color="red",linewidth=0.8)
plt.title('Modulacion de frecuencia')
plt.xlabel('tiempo');
plt.ylabel('amplitud');
plt.grid(True)


