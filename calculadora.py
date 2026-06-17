historico = [] #este comando permite que os dados registrados na calculadora sejam guardados
while True:    #while permite que o usuário escolha fazer mais calculos ou não
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
    historico.append (resultado)

    opcao = input("Deseja realizar outra operação? (S/N): ")

    if opcao == "N":
        print ("Seu histórico de resultados é: ",historico)
        break   #a condiçaõ "break" interrompe com um comando  arepetição do calculo
