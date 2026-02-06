voltages = [12.6, 11.8, 11.5, 10.8, 10.2]
for i, v in enumerate (voltages):
    print(f"Minute {i}: {v} V ")
print ("Filtering Readings:")
for v in voltages:
    if v > 12.0: continue
    if v < 11.0: break 
print(v)