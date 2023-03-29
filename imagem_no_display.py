import pygame as pg; #usando o alias 'pg' para simplificar os chamados de pygame;
from pygame.locals import *;
from sys import exit;

pg.init(); #função que inicializa os módulos da biblioteca 'pygame'
#ao chamar init, a biblioteca inicializa os seguintes módulos: display, font, mixer, joystick, image, time;

"""Informação: pygame.display.flip() é usado para atualizar a janela de exibição
e mostrar qualquer mudança na tela que tenha sido feita desde a última atualização."""

criar_tela = pg.display.set_mode((1200,600), pg.RESIZABLE); #resizable permite que o usuário redimensione a tela; largura x altura

pg.display.set_caption('Jogo principal'); #definindo um título

icone = pg.image.load('C:\\Users\jhona\Downloads\iconeteste.png'); #adicionando um icone com caminho específico

pg.display.set_icon(icone); #definindo a imagem do ícone;

while True:
    for event in pg.event.get(): #serve para obter eventos que ocorram na janela como cliques, teclas e etc;
        if event.type == QUIT:
            pg.quit();
            exit();
    pg.draw.circle(criar_tela, (255,0,0), (600, 300), 60); #criando um circulo para ser exibido na tela;
    pg.draw.rect(criar_tela, (0,0,255), (500, 300, 20,80));
    pg.draw.rect(criar_tela, (0,0,255), (680, 300, 20,80));
    image = pg.image.load('amor.jpeg');
    image = pg.transform.scale( image, (200,300));
    criar_tela.blit(image, (180,100));
    pg.display.update(); #atualizando os eventos da tela e mantendo o loop dele aberta;



