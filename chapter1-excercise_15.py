import numpy as np

rng = np.random.default_rng(seed=42)
power_matrix = rng.random((4, 5)) * 10

total_sys = power_matrix.sum()
avg_per_motor = power_matrix.mean(axis=1) # Average of each row
peak_per_step = power_matrix.max(axis=0)  # Max of each column

time_series_view = power_matrix.T # Transpose
print(f"Total: {total_sys:.2f}W, New Shape: {time_series_view.shape}")