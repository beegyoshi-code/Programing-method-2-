raw_data= " TEMP_DATA:25.678"
fix_string=raw_data.strip().replace("TEMP_DATA:","")
temp = float(fix_string)
print(f"Current Temperature:{temp:.2f}")