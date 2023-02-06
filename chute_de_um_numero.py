"""
Crie um programa que gere um número aleatório de 1 a 10 e peça um chute ao usuário.
O programa deve informar se o chute do usuário foi maior ou menor que o número aleatório gerado.
"""
import random;
numero = random.randint(1,11); #na função randint o número inferior do intervalo é incluído, mas o superior não!
chute = int(input("Digite um número de 1 a 10:\n"));

while chute != numero:
    if chute < 1 or chute > 10:
        print("Digite apenas valores inteiros entre 1 e 10\n");
        chute = int(input("Digite um número de 1 a 10:\n"));
    else:
        if chute > numero:
            print("O valor digitado foi acima do esperado!\n");
            chute = int(input("Digite um número de 1 a 10:\n"));
        else:
            print("O valor digitado foi abaixo do esperado!\n");
            chute = int(input("Digite um número de 1 a 10:\n"));
print("Parabéns você acertou o número aleatório. O valor esperado era: %d" %(numero));
