sensor_cfg={
    "id":101,
    "type":"Lidar",
    "range":[0.1, 30.0]}

sensor_cfg["range"]=[0.1, 50.0]
sensor_cfg["status"]="active"

active_types = ["Lidar", "Camera", "Lidar", "IMU", "Camera"]
unique_sensors=set(active_types)

print(f"Unique types: {unique_sensors}, Count: {len(unique_sensors)}")