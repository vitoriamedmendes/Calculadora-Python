print ("Calculadora iniciada")
num1 = int(input("digite o primeiro numero: ")) 
num2 = int(input("digite o segundo numero: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+": 
    resultado = num1 + num2

elif operacao == "-": 
    resultado = num1 - num2

elif operacao == "*":
    resultado = num1*num2

elif operacao =="/":
    resultado = num1/num2

print("O Resultado é: ", resultado)