a = int(input("Digite um número para um lado: "))
b = int(input("Digite um segundo número para o segundo lado: "))
c = int(input("Digite um terçeiro número para o terçeiro lado : "))
if (a + b) < c or (b + c) < a or (a + c) < b: 
    print("Não é um triângulo.")
elif a == b and b == c:
    print("Equilátero.")
elif a == b or b == c or a == c:
    print("Isósceles.")
else:
    print("Escaleno.")