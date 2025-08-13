
x = float(input ("Informe seu salario para ser corrijido de acordo com o quanto você ganha\n Resposta:"))
if x <= 1563.00: print("Seu novo salario é:", x * 1.25)
elif x >= 1563.01 and x <= 2200.00: print("Seu novo salario é:", x * 1.10)
elif x >= 2200.00 and x <= 3500.00: print("Seu novo salario é:", x * 1.06)
elif x > 3500: print("Seu novo salario é:", x * 1.02)
