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
