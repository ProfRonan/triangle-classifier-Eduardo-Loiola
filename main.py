a = int(input("Digite o valor do primeiro lado: "))
b = int(input("Digite o valor do segundo lado: "))
c = int(input("Digite o valor do terceiro lado: "))
if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        tipo_triangulo = "Equilátero"
    elif a == b or b == c or a == c:
        tipo_triangulo = "Isósceles"
    else:
        tipo_triangulo = "Escaleno"
else:
    tipo_triangulo = "Não é um triângulo"
print("O tipo de triângulo formado é:", tipo_triangulo)
