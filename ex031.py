distance = int(input("km: "))
if distance <= 200:
  print(f"R${distance*0.5:.2f}")
else:
  print(f"R${distance*0.45:.2f}")