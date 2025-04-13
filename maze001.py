################################################################
###                 M O S T R A   M A Z E                    ###
################################################################
### Neste teste, mostra o labirinto gerado pelo algoritmo de ###
### Aldous-Broder                                            ###
################################################################
### Prof. Filipo Mor, FILIPOMOR.COM                          ###
################################################################

import pygame
import sys
#from enum import Enum
from random import randint

class ArestasFechadas:
    def __init__(self, superior, inferior, esquerda, direita):
        self.superior = superior
        self.inferior = inferior
        self.esquerda = esquerda
        self.direita = direita

class Celula:
    def __init__(self, arestasFechadas, corPreenchimento, corLinha, visited):
        self.arestasFechadas = arestasFechadas
        self.corPreenchimento = corPreenchimento
        self.corLinha = corLinha
        self.visited = visited

    def corPreenchimento(self):
        return self.corPreenchimento

    def arestasFechadas(self):
        return self.arestasFechadas

    def visited(self):
        return self.visited

    def desenhar(self, tela, x, y, aresta):
        # x : coluna
        # y : linha

        # calcula as posicoes de desenho das linhas de cada aresta
        arSuperiorIni = (x,y)
        arSuperiorFim = (x+aresta,y)
        arInferiorIni = (x,y+aresta)
        arInferiorFim = (x+aresta,y+aresta)
        arEsquerdaIni = (x,y)
        arEsquerdaFim = (x,y+aresta)
        arDireitaIni  = (x+aresta,y)
        arDireitaFim  = (x+aresta,y+aresta)

        # preenche a célula com a cor definida
        pygame.draw.rect(tela, self.corPreenchimento, (x,y,aresta,aresta))
        # linha superior
        if(self.arestasFechadas.superior):
            pygame.draw.line(tela, self.corLinha, arSuperiorIni, arSuperiorFim)
        # linha inferior
        if(self.arestasFechadas.inferior):
            pygame.draw.line(tela, self.corLinha, arInferiorIni, arInferiorFim)
        # linha esquerda
        if(self.arestasFechadas.esquerda):
            pygame.draw.line(tela, self.corLinha, arEsquerdaIni, arEsquerdaFim)
        # linha direita
        if(self.arestasFechadas.direita):
            pygame.draw.line(tela, self.corLinha, arDireitaIni, arDireitaFim)

class AldousBroder:
    def __init__(self, matriz, qtLinhas, qtColunas, aresta, celulaPadrao):
        self.matriz = matriz
        self.qtLinhas = qtLinhas
        self.qtColunas = qtColunas
        self.aresta = aresta
        self.celulaPadrao = celulaPadrao
        #self.visitados = []

    def __len__(self):
        return len(self.matriz)

    def __iter__(self):
        return iter(self.matriz)

    def resetaLabirinto(self):
        #celulaPadrao = Celula(ArestasFechadas(False, False, False, False), xxx, (255,255,255), False)
        for linha in range(self.qtLinhas):
            for coluna in range(self.qtColunas):
                self.matriz[linha][coluna] = self.celulaPadrao

    def SorteiaCelulaVizinha(self, linhaCelulaAtual, colunaCelulaAtual):
        encontrou = False
        while(encontrou == False):
            linhaVizinha = linhaCelulaAtual + randint(-1,1)
            colunaVizinha = colunaCelulaAtual + randint(-1,1)
            if(linhaVizinha >= 0 and linhaVizinha < self.qtLinhas and colunaVizinha >= 0 and colunaVizinha < self.qtColunas):
                encontrou = True

        return linhaVizinha, colunaVizinha


    def GeraLabirinto(self):

        self.resetaLabirinto()

        unvisitedCells = self.qtLinhas * self.qtColunas
        #cont = 0
        currentCellLine, currentCellColumn, neighCellLine, neighCellColumn = -1, -1, -1, -1
        #guess = -1

        # sorteia uma célula qualquer
        currentCellLine   = randint(0, self.qtLinhas-1)
        currentCellColumn = randint(0, self.qtColunas-1)

        while(unvisitedCells > 0):

             # Sorteia um vizinho qualquer da célula atual
             neighCellLine, neighCellColumn = self.SorteiaCelulaVizinha(currentCellLine, currentCellColumn)

             if(self.matriz[neighCellLine][neighCellColumn].visited == False):
                # incluir aqui a rotina paar abrir uma passagem. Por enquanto, apenas pinta a célula
                self.matriz[neighCellLine][neighCellColumn].visited = True
                self.matriz[neighCellLine][neighCellColumn].corPreenchimento = (0,255,0)
                unvisitedCells -= 1
                #cont += 1

             currentCellLine, currentCellColumn = neighCellLine, neighCellColumn

class Malha:
    def __init__(self, qtLinhas, qtColunas, aresta, celulaPadrao):
        self.qtLinhas = qtLinhas
        self.qtColunas = qtColunas
        self.aresta = aresta
        self.celulaPadrao = celulaPadrao
        #self.matriz = self.GeraMatriz(qtLinhas, qtColunas, celulaPadrao)
        self.matriz = self.GeraMatriz()

    def __len__(self):
        return len(self.matriz)

    def __iter__(self):
        return iter(self.matriz)

    def __getitem__(self, index):
        return self.matriz[index]

    def __setitem__(self, index, value):
        self.matriz[index] = value

    def __aslist__(self):
        return self.matriz

    def GeraMatriz(self):
        matriz = []
        for i in range(self.qtLinhas):
            linha = []
            for j in range(self.qtColunas):
                linha.append(self.celulaPadrao)
            matriz.append(linha)
        return matriz

    def DesenhaLabirinto(self, tela, x, y):
        for linha in range(self.qtLinhas):
            for coluna in range(self.qtColunas):
                self.matriz[linha][coluna].desenhar(tela, x + coluna * self.aresta, y + linha * self.aresta, self.aresta)



'''
def AbreRotas(matriz, corRota):
    for linha in range(1, len(matriz)):
        for coluna in range(1, len(matriz[linha])):
            if(matriz[linha][coluna].arestasFechadas.direita == False):
                matriz[linha][coluna+1].arestasFechadas.esquerda = False
                #matriz[linha][coluna+1].corPreenchimento = corRota
                #matriz[linha][coluna].corPreenchimento   = corRota
'''







def main():
    pygame.init()

    ### definição das cores
    azul     = ( 50, 50,  255)
    preto    = (  0,   0,   0)
    branco   = (255, 255, 255)
    vermelho = (255,   0,   0)
    cinza    = (128, 128, 128)

    # Dimensões da janela
    [largura, altura] = [600, 300]

    ### Dimensões da malha (matriz NxM)
    N = 10  # número de linhas
    M = 10  # número de colunas
    aresta = 15 # dimensão dos lados das células

    celulaPadrao = Celula(ArestasFechadas(False,False,False,False), preto, vermelho, False)
    #matriz = GeraMatriz(N, M, celulaPadrao)
    matriz = Malha(N, M, aresta, celulaPadrao)
    labirinto = AldousBroder(matriz, N, M, aresta, celulaPadrao)

    # valores de teste das paredes abertas e coloração das células
    #matriz[0][0] = Celula(ArestasFechadas(0,0,0,0), azul, branco)
    labirinto.matriz[0][2] = Celula(ArestasFechadas(True, True, True, True), cinza, azul, True)
    labirinto.matriz[0][0] = Celula(ArestasFechadas(False, False, False, False), azul, branco, False)
    labirinto.matriz[1][1] = Celula(ArestasFechadas(False, False, False, False), branco, azul, False)
    #matriz[1][0] = Celula(ArestasFechadas(0, 0, 0, 0), branco, vermelho)
    #matriz[2][2] = Celula(ArestasFechadas(0, 0, 0, 0), azul, preto)
    ###AbreRotas(matriz, cinza)


    # Cria a janela
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Mostra Malha')

    ###
    ### Loop principal
    ###
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        ### preenche a tela com a cor branca
        tela.fill(branco)

        ### centraliza a grade na janela
        [linha, coluna] = ((tela.get_width()  - (M * aresta)) // 2,
                           (tela.get_height() - (N * aresta)) // 2)
        #desenhar_grade(tela, linha, coluna, aresta, N, M, matriz)
        labirinto.matriz.DesenhaLabirinto(tela, linha, coluna)

        ### atualiza a tela
        pygame.display.flip()


if __name__ == '__main__':
    main()