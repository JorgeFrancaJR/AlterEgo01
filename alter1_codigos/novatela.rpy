# ========================     HUD GLOSSARIO   ====================================
screen hud:
    imagebutton:
        idle "tudo/imagem/fundo/icone_barra_idle.png"
        hover "tudo/imagem/fundo/icone_barra_hover.png"
        focus_mask True
        action Show("glossario", transition=dissolve)
    imagebutton:
        idle "tudo/imagem/fundo/icone_livro_idle.png"
        hover "tudo/imagem/fundo/icone_livro_hover.png"
        focus_mask True
        action Show("inventario", transition=dissolve)
# ========================     SELEÇÃO DE PERSONAGENS   ====================================
#    TELA DE SELECAO
default persistent.unlocked_routes = ["Jinguji Sakura"]
# Tamanho dos retratos na tela
default persistent.unlocked_routes = ["Jinguji Sakura"]

screen choose_route_screen():
    tag menu

    # Fundo da tela em 1920x1080
    add "tudo/imagem/fundo/fundo_selecao.png"

    # Título
    text "ESCOLHA SEU PROTAGONISTA":
        xalign 0.5
        ypos 140
        size 38
        color "#F5A5B8"
        bold True

    # JINGUJI SAKURA
    imagebutton:
        idle "tudo/imagem/fundo/jinguji_sakura_retrato_idle.png"
        hover "tudo/imagem/fundo/jinguji_sakura_retrato_rover.png"
        focus_mask True
        action Return("Jinguji Sakura")
        sensitive "Jinguji Sakura" in persistent.unlocked_routes
    # ROTA Azul
    imagebutton:
        idle "tudo/imagem/fundo/blue_retrato_idle.png"
        hover "tudo/imagem/fundo/blue_retrato_rover.png"
        focus_mask True
        action Return("blue")
        sensitive "prota2" in persistent.unlocked_routes
    # ROTA AMARELA
    imagebutton:
        idle "tudo/imagem/fundo/rota_amarela_idle.png"
        hover "tudo/imagem/fundo/rota_amarela_rover.png"
        focus_mask True
        action Return("yellow")
        sensitive "yellow" in persistent.unlocked_routes

    # ROTA PRATA
    imagebutton:
        idle "tudo/imagem/fundo/rota_prata_idle.png"
        hover "tudo/imagem/fundo/rota_prata_rover.png"
        xpos 1150
        ypos 250
        focus_mask True
        action Return("silver")
        sensitive "silver" in persistent.unlocked_routes

    # ROTA DOURADA
    imagebutton:
        idle "tudo/imagem/fundo/rota_dourada_idle.png"
        hover "tudo/imagem/fundo/rota_dourada_rover.png"
        xpos 1500
        ypos 250
        focus_mask True
        action Return("gold")
        sensitive "gold" in persistent.unlocked_routes

    text "Desbloqueie novas rotas durante a história.":
        xalign 0.5
        ypos 900
        size 18
        color "#D5C4C8"
# ========================     GLOSSARIO   ====================================
screen glossario:
    modal True
    $ estado = estado_personagens[personagem_atual]
    # ======================================================
    # BACKGROUND
    # ======================================================
    add estado["foto"]:
        xalign 1
        yalign 1
        fit "cover"
    # ======================================================
    # TÍTULO VERTICAL
    # ======================================================
    vbox:
        xpos 1750
        ypos 100
        spacing 10
        for letra in estado["titulo"]:
            if letra == " ":
                null height 15
            else:
                text "[letra]":
                    font "tudo/fonte/aquifer.ttf"
                    size 45
                    color "#AAA5B5"
                    xalign 0.5
                    outlines [(1, "#000000")]
    # ======================================================
    # NOME
    # ======================================================
    text estado["nome"]:
        xpos 1150
        ypos 100
        size 35
        color "#FFFFFF"
        text_align 0.5
        font "tudo/fonte/aquifer.ttf"
    text "NOME":
        xpos 1150
        ypos 150
        size 15
        bold True
        color "#FFFFFF"
        text_align 0.5
    # ======================================================
    # IDADE
    # ======================================================
    text estado["idade"]:
        xpos 1150
        ypos 200
        size 35
        color "#FFFFFF"
        text_align 0.5
        font "tudo/fonte/aquifer.ttf"
    text "IDADE":
        xpos 1150
        ypos 250
        size 15
        bold True
        color "#FFFFFF"
        text_align 0.5
    # ======================================================
    # CARACTERÍSTICA
    # ======================================================
    text estado["traco"]:
        xpos 1150
        ypos 300
        size 35
        color "#FFFFFF"
        text_align 0.5
        font "tudo/fonte/aquifer.ttf"
    text "TRAÇOS":
        xpos 1150
        ypos 350
        size 15
        bold True
        color "#FFFFFF"
        text_align 0.5
    # ======================================================
    # MEDO
    # ======================================================
    text estado["medo"]:
        xpos 1150
        ypos 400
        size 35
        color "#FFFFFF"
        text_align 0.5
        font "tudo/fonte/aquifer.ttf"
    text "MEDO":
        xpos 1150
        ypos 450
        size 15
        bold True
        color "#FFFFFF"
        text_align 0.5
    # ======================================================
    # SETA ESQUERDA
    # ======================================================
    textbutton "❮":
        xpos 1650
        ypos 900
        text_size 80
        text_color "#FFFFFF"
        text_hover_color "#AAA5B5"
        text_outlines [(2, "#000000")]
        action [SetVariable("personagem_atual", (personagem_atual - 1) % len(personagens)),With(Dissolve(0.5))]
    # ======================================================
    # SETA DIREITA
    # ======================================================
    textbutton "❯":
        xpos 1750
        ypos 900
        text_size 80
        text_color "#FFFFFF"
        text_hover_color "#AAA5B5"
        text_outlines [(2, "#000000")]
        action [SetVariable("personagem_atual", (personagem_atual + 1) % len(personagens)),With(Dissolve(0.5))]
    # ======================================================
    # FECHAR
    # ======================================================
    imagebutton:
        idle "tudo/imagem/fundo/icone_barra_idle.png"
        hover "tudo/imagem/fundo/icone_barra_hover.png"
        focus_mask True
        action Hide("glossario", transition=dissolve)

# ========================     INVENTARIO   ====================================
default mochila = []
default traco = []
default aba_inventario = "itens"

screen inventario():
    tag menu
    modal True
    zorder 200
    add Solid("#000000CC")
    # FUNDO: posição original, sem redimensionar
    add "tudo/imagem/fundo/fundo_inventario.png"
    # PERSONAGEM: parte superior
    add "tudo/imagem/fundo/personagem_inventario_en.png"

    # BOTÃO BAG: quadrado esquerdo
    imagebutton:
        idle "tudo/imagem/fundo/bag_idle.png"
        hover "tudo/imagem/fundo/bag_hover.png"
        xpos 0
        ypos 0
        focus_mask True
        action SetVariable("aba_inventario", "itens")

    # BOTÃO TRACE: quadrado direito
    imagebutton:
        idle "tudo/imagem/fundo/trace_idle.png"
        hover "tudo/imagem/fundo/trace_hover.png"
        xpos 0
        ypos 0
        focus_mask True
        action SetVariable("aba_inventario", "habilidades")

    # LISTA INFERIOR
    vbox:
        xpos 0
        ypos 430
        xsize 1920
        spacing 15
        if aba_inventario == "itens":
            if mochila:
                viewport:
                    xalign 0.5
                    xsize 1000
                    ysize 250
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    vbox:
                        spacing 8
                        for item in mochila:
                            textbutton item[0]:
                                xsize 950
                                text_size 25
                                text_color "#FFFFFF"
                                text_hover_color "#d9b66c"
                                action Show(
                                    "descricao_objeto",
                                    titulo=item[0],
                                    descricao=item[1]
                                )
            else:
                text "Mochila vazia.":
                    xalign 0.5
                    size 23
                    color "#FFFFFF"
        elif aba_inventario == "habilidades":
            if traco:
                viewport:
                    xalign 0.5
                    xsize 1000
                    ysize 250
                    scrollbars "vertical"
                    mousewheel True
                    draggable True

                    vbox:
                        spacing 8

                        for perk in traco:

                            textbutton perk[0]:
                                xsize 950
                                text_size 25
                                text_color "#FFFFFF"
                                text_hover_color "#d9b66c"
                                action Show(
                                    "descricao_objeto",
                                    titulo=perk[0],
                                    descricao=perk[1]
                                )

            else:

                text "Nenhuma habilidade adquirida.":
                    xalign 0.5
                    size 23
                    color "#FFFFFF"

    # BOTÃO FECHAR (X)
    imagebutton:
        idle "tudo/imagem/fundo/X_inventario_idle.png"
        hover "tudo/imagem/fundo/X_inventario_hover.png"
        focus_mask True
        action [Hide("descricao_objeto"),Hide("inventario", transition=dissolve)]
# ======================== DESCRIÇÃO ========================

screen descricao_objeto(titulo, descricao):

    modal True
    zorder 300

    add Solid("#00000099")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 600
        background Solid("#30303d")
        padding (30, 25)

        vbox:
            spacing 20

            text titulo:
                size 32
                color "#e8d6a3"
                xalign 0.5

            text descricao:
                size 22
                color "#FFFFFF"
                text_align 0.5
                xalign 0.5

            textbutton "Fechar":
                xalign 0.5
                text_size 24
                text_color "#FFFFFF"
                text_hover_color "#d9b66c"
                action Hide("descricao_objeto")
# ========================     REMOVER ITEM E HABILIDADE   ====================================
init python:
# Remover item da mochila
    def remover_item(nome):
        for item in store.mochila[:]:
            if item[0] == nome:
                store.mochila.remove(item)
                return
    # Remover habilidade
    def remover_habilidade(nome):
        for perk in store.traco[:]:
            if perk[0] == nome:
                store.traco.remove(perk)
                return
    def tem_habilidade(nome):
        return any(perk[0] == nome for perk in store.traco)
    def tem_item(nome):
        return any(item[0] == nome for item in store.mochila)

# ======================== DADO ROLANDO ========================
# ============================================================
# SISTEMA DE DADO D20 ANIMADO
# ============================================================

default dado_valor = 1
default dado_rolando = False


# ============================================================
# FUNÇÕES DO DADO
# ============================================================

init python:

    import random

    def atualizar_dado(lados=20):
        """
        Atualiza o número enquanto o dado está rolando.
        """
        if store.dado_rolando:
            store.dado_valor = random.randint(1, lados)


    def finalizar_dado(lados=20):
        """
        Finaliza a rolagem e preserva o resultado.
        """
        if store.dado_rolando:
            store.dado_valor = random.randint(1, lados)
            store.dado_rolando = False


# ============================================================
# TELA DE ROLAGEM
# ============================================================

screen animacao_dado(lados=20, duracao=1.5):

    modal True
    zorder 300

    # Fundo escurecido.
    add Solid("#000000CC")

    # Fundo principal do dado.
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1920
        ysize 1080

        background Frame("tudo/imagem/fundo/fundo_dado.png")
        padding (25, 25)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 25
            text "[dado_valor]":
                size 100
                color "#FFFFFF"
                xalign 0.5
                outlines [(3, "#d9b66c")]
    # --------------------------------------------------------
    # ANIMAÇÃO DO DADO
    # --------------------------------------------------------

    if dado_rolando:

        # Troca o número durante a rolagem.
        timer 0.10 repeat True action Function(
            atualizar_dado, lados
        )

        # Finaliza a rolagem após a duração configurada.
        timer duracao action Function(
            finalizar_dado, lados
        )

    else:

        # Fecha a tela automaticamente após mostrar o resultado.
        timer 1.5 action Return(dado_valor)


# ============================================================
# FUNÇÃO QUE INICIA A ROLAGEM
# ============================================================

init python:

    def rolar_dado_animado(lados=20, duracao=2):

        # Prepara uma nova rolagem.
        store.dado_rolando = True
        store.dado_valor = renpy.random.randint(1, lados)

        # Abre a tela e aguarda o resultado.
        resultado = renpy.call_screen(
            "animacao_dado",
            lados=lados,
            duracao=duracao
        )

        # Retorna o resultado final para a história.
        return resultado
    def dificuldade_teste(dificuldade):
        resultado = rolar_dado_animado(20)
        return resultado >= dificuldade




# ========================     CLIMA   ====================================
init python:
    def iniciar_chuva(hard=True):
        renpy.show("chuva", layer="clima")
        renpy.pause(2.0, hard=hard)
    def parar_chuva(hard=True):
        renpy.hide("chuva", layer="clima")
        renpy.pause(2.0, hard=hard)
