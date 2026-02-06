dist = 0.8
emergency_stop = False  

if emergency_stop :
    safety_mode ="ESTOP"
elif dist < 0.5 :
    safety_mode="COLISSION"
elif 0.5 <= dist <=1.5:
    safety_mode = "WARNING"
else:
    safety_mode = "NORMAL"

LED_color = "RED" if safety_mode !="NORMAL" else "Green"
print(f"status {safety_mode}, LED: {LED_color}")
