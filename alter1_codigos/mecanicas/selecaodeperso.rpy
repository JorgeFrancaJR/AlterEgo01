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
