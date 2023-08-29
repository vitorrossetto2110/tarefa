def fahrenheit(celsius):
    return (celsius * 9/5) + 32


print("Temperatura:")
for celsius in range(0, 101, 10):
    fahrenheit_temperatura = fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit_temperatura:.2f}°F")
