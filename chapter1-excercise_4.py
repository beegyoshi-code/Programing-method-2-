raw_gps=(10.823, 106.629, 5.0)
lat , lon, _ = raw_gps
def get_velocity():
    return(3.0,-2)
vx,vy=get_velocity()
print(f"Velocity: x ={vx}m/s, velocity: y={vy}m/s" )