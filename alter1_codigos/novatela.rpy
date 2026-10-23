# ========================     ESTADO MENTAL   ====================================
default pontos_mentais = 100
default estado_mental = "Neutro"
init python:
    # Atualiza o estado mental conforme a pontuação atual
    def atualizar_estado_mental():
        pontos = renpy.store.pontos_mentais
        if pontos <= 50:
            estado = "Inspirado"
        elif pontos <= 150:
            estado = "Neutro"
        elif pontos <= 200:
            estado = "Perturbado"
        elif pontos <= 250:
            estado = "Instavel"
        else:
            estado = "Colapsado"
        renpy.store.estado_mental = estado
    # Aumenta ou diminui os pontos atuais
    def alterar_pontos_mentais(valor):
        renpy.store.pontos_mentais = max(0,min(300, renpy.store.pontos_mentais + valor))
        atualizar_estado_mental()
    # Define uma quantidade EXATA de pontos
    def definir_pontos_mentais(valor):
        renpy.store.pontos_mentais = max(0,min(300, valor))
        atualizar_estado_mental()
# ======================== IMAGENS DO ESTADO MENTAL ========================
# Imagens exibidas conforme o estado mental atual
image estado_inspirado = "tudo/imagem/estado_mental/inspirado.png"
image estado_neutro = "tudo/imagem/estado_mental/neutro.png"
image estado_instavel = "tudo/imagem/estado_mental/instavel.png"
image estado_perturbado = "tudo/imagem/estado_mental/perturbado.png"
image estado_colapsado = "tudo/imagem/estado_mental/colapsado.png"
# ======================== TELA DO ESTADO MENTAL ==========================

screen mostrar_estado_mental():
    zorder 100
    if estado_mental == "Inspirado":
        add "estado_inspirado"
    elif estado_mental == "Neutro":
        add "estado_neutro"
    elif estado_mental == "Perturbado":
        add "estado_perturbado"
    elif estado_mental == "Instavel":
        add "estado_instavel"
    elif estado_mental == "Colapsado":
        add "estado_colapsado"
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


# ========================     CLIMA   ====================================
init python:
    def iniciar_chuva(hard=True):
        renpy.show("chuva", layer="clima")
        renpy.pause(2.0, hard=hard)
    def parar_chuva(hard=True):
        renpy.hide("chuva", layer="clima")
        renpy.pause(2.0, hard=hard)
