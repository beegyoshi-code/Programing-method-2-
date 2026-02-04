safety_limit_torque= 5.0
torques= [1.2, 5.5, 0.8, 10.2, 4.9, -2.1, 7.0]
safe_torques=[t for t in torques if abs(t)<=5.0 ]
safe_torques.append(0.0)
print(f"validated commands: {safe_torques}")