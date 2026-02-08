import numpy as np
raw_imu = np.array([0.1, 0.2, 9.8, 0.15, 0.22, 9.78, 0.12, 0.21, 9.81, 0.11, 0.23, 9.79])

imu_matrix= raw_imu.reshape (4, 3)

print(f"shape {imu_matrix.shape}")
print(f"Time step 1 (X,Y,Z): {imu_matrix[0]}")