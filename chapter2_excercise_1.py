#euler equation 
#BEGIN PROGRAM 

#INITIALIZE VELOCITY(velo),TIME_STEP(time_step),GRAVITY(gravity)

#def LOOP
# CALCULATE the change :gravity * time_step



v = 0.0 #velocity
dt= 0.1 #time_step
g= -9.81 #gravity
for i in range (10):
    v += g*dt
    print(v)