import matplotlib.pyplot as plt
dt=0.01 #time_step
time_values = [i * dt for i in range(1000)]
m= 0.5 #kg
k= 20 #N/m
d= 0.5 #Ns/m


x=1.0 #initial position
v=0.0 #initial velocity
x_values=[] 
t = [i * dt for i in range(1000)]
plt.xlabel('Time')
plt.ylabel('Positinos')

for i in range (1000):
    a=(-k*x - d*v)/m
    v= v+(a *dt)
    x= x + (v*dt)
    x_values.append(x)

    plt.plot(t, x_values)
plt.show()