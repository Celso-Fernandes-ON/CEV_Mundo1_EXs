import random
import time
n1 = random.randint(1,5)
n2 = int(input(": "))
print("Processando...")
time.sleep(2)
if n1==n2:
 print(f"acertou {n1} {n2}")
else:
 print(f"não acertou, era {n2} e não {n1}")
print(n1)