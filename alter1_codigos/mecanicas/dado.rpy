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
