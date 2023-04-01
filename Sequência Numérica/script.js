let botaoClicado = false; //variável para obter o valor se o botão foi clicado ou não

function clickbotao(){ //função do botão start: iniciar e pegar o valor fornecido pelo usuário;
  let numeroInicial = parseInt(document.getElementById("numeroInicial").value);

  if (isNaN(numeroInicial)){ //verificando se a caixa input não está vazia;
      document.getElementById("erro").innerHTML = "Ops... digite um valor inicial";
      document.getElementById("numeroAtual").innerHTML = 0; //zerando resultado caso o usuário inicie um valor e depois volte a deixar a caixa de input vazia;
      botaoClicado = false;

  }
  else {
      document.getElementById("numeroAtual").innerHTML = numeroInicial;
      document.getElementById("erro").innerHTML = "";
      botaoClicado = true;
  }
}

function proximoNumero(){
  let numeroAtual = parseInt(document.getElementById("numeroAtual").innerHTML);
  let proximoNumero = parseInt(numeroAtual + 1);
  switch (botaoClicado){ //condicional para permitir que o número mude apenas quando o botão start for clicado
    case true:
        document.getElementById("numeroAtual").innerHTML = proximoNumero;
        document.getElementById("erro").innerHTML = "";
    case false:
        return;
  }
}

  function retorno(){ //função para atribuir ao botão sub a subtração -1 do valor atual na página;
      let numeroInicial = parseInt(document.getElementById("numeroInicial").value);
      let numeroAtual = document.getElementById("numeroAtual").innerHTML;
      let sub = parseInt(numeroAtual - 1);
    switch (isNaN(numeroInicial)){
        case true:
            return;
        case false:
            if (numeroAtual > 0){
                    document.getElementById("numeroAtual").innerHTML = sub;
            }
        else {
                    document.getElementById("erro").innerHTML = "Nada para subtrair";
        }
    }
  }


