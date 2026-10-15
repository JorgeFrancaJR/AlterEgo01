# ========================     HUD GLOSSARIO   ====================================
screen hud:
    textbutton "☰":
        xpos 10
        ypos 5
        text_size 60
        text_color "#FFFFFF"
        text_hover_color "#777777"
        action Show("glossario", transition=dissolve)

    textbutton "🎒":
        xpos 90
        ypos 5
        text_size 50
        text_color "#FFFFFF"
        text_hover_color "#AAA5B5"
        action Show("inventario", transition=dissolve)
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
                    font "fontes/aquifer.ttf"
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
        font "fontes/aquifer.ttf"
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
        font "fontes/aquifer.ttf"
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
        font "fontes/aquifer.ttf"
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
        font "fontes/aquifer.ttf"
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
    textbutton "☰":
        xpos 10
        ypos 5
        text_size 60
        text_color "#FFFFFF"
        text_hover_color "#777777"
        action Hide("glossario", transition=dissolve)

# ========================     INVENTARIO   ====================================
default mochila = []
default perks = []
default aba_inventario = "itens"

screen inventario:
    tag menu
    modal True
    zorder 200
    # Fundo escuro
    add Solid("#000000bb")
    # Janela principal
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1100
        ysize 700
        background Solid("#20202a")
        padding (35, 30)
        vbox:
            spacing 25

            # Título
            text "PERSONAGEM":
                size 38
                color "#e8d6a3"
                xalign 0.5

            # ======================== ABAS ========================
            hbox:
                xalign 0.5
                spacing 50
                if aba_inventario == "itens":

                    textbutton "ITENS":
                        text_size 28
                        text_color "#d9b66c"
                        text_hover_color "#FFFFFF"
                        action SetVariable("aba_inventario", "itens")

                else:

                    textbutton "ITENS":
                        text_size 28
                        text_color "#888888"
                        text_hover_color "#FFFFFF"
                        action SetVariable("aba_inventario", "itens")

                if aba_inventario == "habilidades":

                    textbutton "HABILIDADES":
                        text_size 28
                        text_color "#d9b66c"
                        text_hover_color "#FFFFFF"
                        action SetVariable("aba_inventario", "habilidades")

                else:

                    textbutton "HABILIDADES":
                        text_size 28
                        text_color "#888888"
                        text_hover_color "#FFFFFF"
                        action SetVariable("aba_inventario", "habilidades")

            # ======================== LISTA DE ITENS ========================

            if aba_inventario == "itens":

                text "MOCHILA":
                    size 25
                    color "#d9b66c"

                if mochila:

                    viewport:
                        xsize 1000
                        ysize 430
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        vbox:
                            spacing 10

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
                        size 23
                        color "#999999"

            # ======================== LISTA DE HABILIDADES ========================

            elif aba_inventario == "habilidades":

                text "HABILIDADES ADQUIRIDAS":
                    size 25
                    color "#d9b66c"

                if perks:

                    viewport:
                        xsize 1000
                        ysize 430
                        scrollbars "vertical"
                        mousewheel True
                        draggable True

                        vbox:
                            spacing 10

                            for perk in perks:

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
                        size 23
                        color "#999999"

            null height 10

            # ======================== FECHAR ========================

            textbutton "Fechar":
                xalign 0.5
                text_size 25
                text_color "#FFFFFF"
                text_hover_color "#d9b66c"
                action Hide("inventario", transition=dissolve)


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
        for perk in store.perks[:]:
            if perk[0] == nome:
                store.perks.remove(perk)
                return
    def tem_habilidade(nome):
        return any(perk[0] == nome for perk in store.perks)
    def tem_item(nome):
        return any(item[0] == nome for item in store.mochila)

# ======================== DADO ROLANDO ========================
default dado_valor = 1
default dado_rolando = False
init python:
    import random
    def atualizar_dado(lados):
        if store.dado_rolando:
            store.dado_valor = random.randint(1, lados)
    def finalizar_dado(lados):
        store.dado_valor = random.randint(1, lados)
        store.dado_rolando = False
screen animacao_dado(lados=20, duracao=1.5):
    modal True
    zorder 300
    # Fundo escuro por trás da janela
    add Solid("#00000099")
    # Janela com imagem de fundo
    frame:
        xalign 0.5
        yalign 0.5
        xsize 450
        ysize 400
        background Frame("images/fundos/fundo_dado.jpg", 20, 20)
        padding (25, 25)
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 25
            text "TESTE DE HABILIDADE":
                size 22
                color "#e8d6a3"
                xalign 0.5
            text "[dado_valor]":
                size 100
                color "#FFFFFF"
                xalign 0.5
                outlines [(3, "#d9b66c")]
            if dado_rolando:
                text "Rolando o dado...":
                    size 20
                    color "#aaa5b5"
                    xalign 0.5
                # Atualiza o número durante a animação.
                timer 0.08 repeat True action Function(atualizar_dado, lados)
                # Encerra a rolagem após a duração definida.
                timer duracao action Function(finalizar_dado, lados)
            else:
                text "":
                    size 20
                    color "#8de0a8"
                    xalign 0.5
                # Retorna o resultado e fecha a tela.
                timer 0.8 action Return(dado_valor)
init python:
    def teste_habilidade(dificuldade=10):
        rolagem = rolar_dado_animado(20)
        return rolagem > dificuldade
    def rolar_dado_animado(lados=20, duracao=1.5):
        store.dado_rolando = True
        store.dado_valor = renpy.random.randint(1, lados)
        resultado = renpy.call_screen("animacao_dado",lados=lados,duracao=duracao)
        return resultado
# ========================     CLIMA   ====================================
init python:
    def iniciar_chuva(hard=True):
        renpy.show("chuva", layer="clima")
        renpy.pause(2.0, hard=hard)
    def parar_chuva(hard=True):
        renpy.hide("chuva", layer="clima")
        renpy.pause(2.0, hard=hard)
#=============================
init python:
    def showsideimage(personagem):
        renpy.show(personagem,layer="screens",tag="sideimage",at_list=[Transform(xalign=0.0,yalign=1.0)])
