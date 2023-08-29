def celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

começo = int(input("Digite o começo (em Fahrenheit): "))
fim = int(input("Digite o fim (em Fahrenheit): "))
intervalo = int(input("Digite o valor do intervalo: "))

print(f"Temperaturas  entre {começo}°F e {fim}°F em Celsius:")
for fahrenheit in range(começo, fim + 1, intervalo):
    celsius_temp = celsius(fahrenheit)
    print(f"{fahrenheit}°F = {celsius_temp:.2f}°C")
