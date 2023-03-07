
from PIL import Image;
import os;
import requests; #usado para requisições HTTP em um programa python. Ela permite solicitações como GET, POST, PUT etc..
from io import BytesIO;

link_da_imagem = 'https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Red_Apple.jpg/280px-Red_Apple.jpg';

#lendo a imagem

#obtendo_imagem = requests.get(link_da_imagem);
#img = Image.open(BytesIO(obtendo_imagem.content));

img = Image.open(BytesIO(requests.get(link_da_imagem).content)); #de forma mais direta

# Salvando a imagem original

diretorio = 'c:/Users/jhona/OneDrive/Documentos/Codando/imagens/';
nome_da_imagem = 'imagem_da_maçã.jpg';
img.save(os.path.join(diretorio, nome_da_imagem));


#informações da imagem
largura_imagem = img.size[0];
altura_imagem = img.size[1];
"""o comando .size retorna a altura e largura de uma imagem em uma tupla.
dessa forma na posição 0 da tupla temos a largura e na posição 1 da tupla temos a altura."""

# obtem a matriz de pixels da imagem
matriz_pixeis = img.load();

"""Depois que a matriz de pixels é criada,
podemos usar os índices para acessar os valores dos pixels individuais.
Por exemplo, se quisermos acessar o pixel na posição (x, y),
 podemos usar a notação matriz_pixels[x, y]."""

for pixel_coluna in range(largura_imagem):
        for pixel_linha in range(altura_imagem):
                pixel_obtido = matriz_pixeis[pixel_coluna, pixel_linha];

                R = pixel_obtido[0];
                G = pixel_obtido[1];
                B = pixel_obtido[2];

                media_de_cores = int(pixel_obtido[0] * 0.3 + pixel_obtido[1] * 0.59 + pixel_obtido[2] * 0.11) #para obter cinza
                #lembrando que os valores da imagem são representados como inteiros de 0 a 255
                #dessa forma devemos converter os valores obtidos da multiplicação dos números float para int.
                novo_pixel_cinza = (media_de_cores,media_de_cores,media_de_cores);
                matriz_pixeis[pixel_coluna,pixel_linha] = novo_pixel_cinza;


#salvando novamente a imagem
img.save(os.path.join('c:/Users/jhona/OneDrive/Documentos/Codando/imagens/', 'imagemalterada.jpg'));


