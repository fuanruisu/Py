valores = {}
lista = []
valores.setdefault("presion",[])
for i in range(1,100):
    valores["presion"].append(getTemp())

for i in range(1,100):
print(valores["presion"])