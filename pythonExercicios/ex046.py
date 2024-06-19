import time

print('Contagem regressiva para estouro de fogos de artifício')
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
print('BUMMM BUMMMM BUMMMM ACABOOO')