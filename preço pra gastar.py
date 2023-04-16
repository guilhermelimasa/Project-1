gastos = 0
vg = 0
while gastos < 1000:
    vg = int(input("digite o valor do novo gasto: "))
    gastos = gastos + vg
else:
    print("vc chegou no limite ")
print(gastos)