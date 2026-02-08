import numpy as np 

sensor_left = np.array([1.5, 0.8, 2.3])
sensor_right = np.array([2.1, 0.5, 1.9])

all_readings = np.concatenate ((sensor_left, sensor_right))
sorted_readings = np.sort(all_readings) 

final = sorted_readings.reshape (3, 2)
print(f"result {final}")