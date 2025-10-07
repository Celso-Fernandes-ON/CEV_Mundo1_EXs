number1 = int(input(": "))
number2 = int(input(": "))
number3 = int(input(": "))
if number1 < number2 + number3 and number2 < number1 + number3 and number3 < number2 + number1:
  print("é triangulo")
else:
  print("não é triangulo")