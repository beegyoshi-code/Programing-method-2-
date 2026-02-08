import numpy as np

period_1=[[10, 11, 12], [20, 21, 22]]
period_2=[[30, 31, 32], [40, 41 , 42]]

full_data = np.vstack((period_1,period_2))

y_coords = full_data [:, 1]

sub_matrix= full_data [2:, 1:]

data_backup = full_data.copy()

print(f"FULL SHAPE: {full_data.shape}")
print(f"sub-matrix:\n {sub_matrix}")