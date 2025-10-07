number1 = int(input(": "))
number2 = int(input(": "))
number3 = int(input(": "))
maior = number1
menor = number1
# maior
if number3 < number2 > number1 :
  maior = number2
if number2 < number3 > number1:
  maior = number3
# menor
if number1 > number2 < number3:
  menor = number2
if number1 > number3 < number2:
  menor = number3
print(f"maior {maior}")
print(f"menor {menor}")