#4.1
import math

degrees = [0, 30, 45, 60, 90, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360]

print("Degrees   Sin         Cos         Tan")
print("---------------------------------------")

for degree in degrees:
    radian = math.radians(degree)
    sin_value = math.sin(radian)
    cos_value = math.cos(radian)
    
    if degree == 90 or degree == 270:
        tan_value = math.inf if degree == 90 else -math.inf
    else:
        tan_value = math.tan(radian)
    
    print(f"{degree: 3}°     {sin_value: .6f}     {cos_value: .6f}     {tan_value: .6f}")



    


    

