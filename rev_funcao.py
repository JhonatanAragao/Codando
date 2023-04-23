#função imprime nome idade e sexo
while True:
    def dadosPessoa (nome,idade,sexo):
        nome = nome;
        idade = idade;
        sexo = sexo
        if sexo == " masculino":
            print("O usuário foi cadastrado com sucesso!")
            print("Ele %s possui%s anos de idade e é do sexo%s!"%(nome,idade,sexo))
        else:
            print("A usuária foi cadastrada com sucesso!")
            print("Ela %s possui%s anos de idade e é do sexo%s!"%(nome,idade,sexo))
        return

    dados = input("Digite os dados do usuário separados por uma vírgula!\n")
    nome, idade, sexo = dados.split(",")
    dadosPessoa(nome,idade,sexo)
