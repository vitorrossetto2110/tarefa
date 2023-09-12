def fahrenheit(celsius):
    return (celsius * 9/5) + 32

print("Temperaturas equivalentes entre 0°C e 100°C em Fahrenheit:")

for celsius in range(0, 101, 10):
    try:
        celsius_temperatura = fahrenheit(celsius)
        print(f"{celsius}°C = {celsius_temperatura:.2f}°F")
    except ValueError:
        print("Erro: Valor inválido para celsius")
