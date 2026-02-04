#Pseudocode 
#BEGIN PROGRAM

    #DEFINE system_name

    #INITIALIZE temperature_c
    #INITIALIZE voltage 

    #DEFINE safe_temperature_min 
    #DEFINE safe_temperature_max
    #DEFINE safe_voltage_min
    #DEFINE safe_voltage_max

    #READ temperature sensor -> temperature_c
    #READ temperature sensor -> temperature_f

    #CONVERT temperature_c -> temperature_f

    #IF temperature_c is within safe_temperature THEN
    #   temperature_safe <-TRUE
    #ELSE 
    #   temperature_safe <-FALSE
    #END

    #IF volatage is within safe_voltage THEN
    #   safe_voltage <-TRUE
    #ELSE 
    #   safe_voltage <-FALSE
    #END IF

    #IF temperature_safe AND voltage_safe THEN
        #system_status <-"OK"
    #ELSE
        #system_status <-"FAULT"
    #END IF 

    #PRINT system_name
    #PRINT temperature in Celsius and Fahrenheit
    #PRINT voltagex``
    #PRINT system_status

#END PRORAM

#PYTHON CODE 
 
def celsius_to_fahrenheit (temp_c: float) -> float:
    return temp_c *9/5 + 32 

temperature_c = 70  
voltage=12.0
system_name="Temperature sensor"
is_running= True

temperature_f = celsius_to_fahrenheit(temperature_c)

temp_safe = 0.0 <= temperature_c <= 80
voltage_safe = 0.0 <= voltage <= 24.0
system_safe = temp_safe and voltage_safe

status="OK" if system_safe else "FAULT"

print(
  f"[{system_name}]"
  f"Temp: {temperature_c:.1f} C ({temperature_f:.1f} F),"
  f"volatage{voltage:.1f} V,"
  f"Status: {status}"
)