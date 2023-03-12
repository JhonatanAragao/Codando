#Faça uma função que retorne o reverso de um número inteiro informado. Ex.: 127 >> 721


def inverte_numero(numero):
    numero_str = str(numero);
    numero_invertido = numero_str[::-1];
    numero_invertido = int(numero_invertido);
    return numero_invertido;

print(inverte_numero(int(input("Digite um número:\n"))));

