import numpy as np

raw_accel=np.array([ [0.1, 0.1, 9.9], [0.1, 0.1, 9.9], 
                   [0.2, 0.0, 9.8], [0.1, 0.2, 9.9]])

bias = np.array([0.1, 0.1, 9.9])

clean_accel = raw_accel - bias

accel_ms2 = clean_accel *9.81 
print(accel_ms2)