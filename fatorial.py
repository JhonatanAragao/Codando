
"""
Relembrando exercício do cálculo de fatorial com o uso do WHILE AND FOR;
"""

numero = 5;
i = 1;
fatorial = 1;
while i <= numero:
   fatorial *= i;
   i += 1;
print(fatorial);

"""
1ª
fatorial = 1
i = 1
resultado = 1

2º
fatorial= 1
i = 2
resultado = 2

3º 
fatorial = 2
i = 3
resultado = 6

4º
fatorial = 6
i = 4
resultado = 24

5º
fatorial = 24
i = 5
resultado = 120

Chegamos ao resultado final esperado!
"""
"""
Agora fazendo o cálculo de fatorial com o uso do loop FOR.
A função range() exige a definição do último elemento da sequência numérica. Por padrão, o parâmetro start será igual a 0 e o step igual a 1
"""
numero = 4;
fatorial = 1;
for i in range(1,numero + 1):
    fatorial *= i;
print(fatorial);