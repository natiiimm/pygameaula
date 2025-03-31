###
### Exploracao da biblioteca PyGame
###
### Prof. Filipo Novo Mor
###
import pygame
import sys

# Inicializa o pygame
pygame.init()

# Define as dimensões da janela
largura, altura = 300, 200
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("teste com botão e sprite")

# Define as cores
branco = (255, 255, 255)
cinza = (200, 200, 200)
preto = (0, 0, 0)

# Carrega a sprite sheet do personagem
# o arquivo deve conter todas as imagens em uma unica linha
sprite_sheet = pygame.image.load("Attack.png").convert_alpha()
num_quadros = 8  # Número de quadros na sprite sheet

# Calcula os tamanhos corretos dos quadros
quadro_largura = sprite_sheet.get_width() // num_quadros  # Largura de cada quadro
quadro_altura = sprite_sheet.get_height()  # Altura total da sprite sheet

# Extraí os quadros na linha correta
quadros = [sprite_sheet.subsurface((i * quadro_largura, 52, quadro_largura, quadro_altura - 52)) for i in range(num_quadros)]

# Função para desenhar o botão
def desenha_botao(tela, cor, pos, tamanho, texto):
    fonte = pygame.font.Font(None, 36)
    pygame.draw.rect(tela, cor, (pos[0], pos[1], tamanho[0], tamanho[1]))
    texto_surface = fonte.render(texto, True, preto)
    texto_rect = texto_surface.get_rect(center=(pos[0] + tamanho[0] // 2, pos[1] + tamanho[1] // 2))
    tela.blit(texto_surface, texto_rect)

# Dimensões do botão
largura_botao, altura_botao = 100, 50

# Posição do botão no canto inferior direito
x_botao = largura - largura_botao - 10
y_botao = altura - altura_botao - 10

# Variáveis de animação
indice_quadro = 0
tempo_animacao = 100  # Tempo a cada quadro em milissegundos
cronometro = 0

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if botao.collidepoint(evento.pos):
                rodando = False

    # Atualiza o quadro da animação
    cronometro += pygame.time.get_ticks()
    if cronometro > tempo_animacao:
        indice_quadro = (indice_quadro + 1) % num_quadros
        cronometro = 0

    # Preenche o fundo de branco
    tela.fill(branco)

    # Desenha a animação do personagem no canto superior esquerdo
    tela.blit(quadros[indice_quadro], (10, 10))

    # Desenha o botão
    botao = pygame.Rect(x_botao, y_botao, largura_botao, altura_botao)
    desenha_botao(tela, cinza, botao.topleft, botao.size, "Sair")

    # Atualiza a tela
    pygame.display.flip()

# Encerra o pygame
pygame.quit()
sys.exit()
