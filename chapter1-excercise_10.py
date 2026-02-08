import math 
from datetime import datetime

arm_length = 1.5
angle_deg = 30.0

start_time=datetime.now()

angle_rad = math.radians(angle_deg)
x= arm_length *math.cos(angle_deg)
y= arm_length *math.sin(angle_deg)

duration= datetime.now() - start_time

print(f"Coordinates: x={x:.3f}m, y={y:.3f}m")
print(f"Calculation took: {duration.total_seconds() * 10**6:.2f} microseconds")