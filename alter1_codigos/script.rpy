
#-------------------------EFEITOS CLIMA--------------------------------------
image chuva = Movie(play="tudo/imagem/chuva.webm",size=(1920,1080) ,loop=True)
init python:
    config.layers = ["master","fundo","clima","personagens","transient","screens","overlay"]
#-------------------------NOMES PERSONAGEM--------------------------------------
define eu = Character("Kyo")
define minazinha = Character("Laharl")
define outramina = Character("Psico")
default nome_jinguji = "????"
define jinguji_sakura = DynamicCharacter("nome_jinguji")


image bgpark = "bg_park.jpg"
image bgrua = "bg_ruas.jpg"
image bgred = "bg_red.jpg"
image fundo_preto = Solid("#000000")

image minazinha_f1 = "tudo/imagem/minazinha1-1.png"
image outramina_f1 = "tudo/imagem/outraminazinha1-1.png"


image city_f1 = "tudo/imagem/fundo/cidade_f1.png"

image static_dante_f1 = "tudo/imagem/dante/static_dante_f1.png"


default foiprocafe = False
default qntsCafe = 3
default sucesso = 0


default persistent.unlocked_routes = [ "red", "yellow", "silver", "gold"]
label start:

    call screen choose_route_screen
    $ selected_route = _return
    if selected_route == "Jinguji Sakura":
        $ persistent.unlocked_routes.append("blue")
        with dissolve
        jump jinguji_historia

    elif selected_route == "red":
        jump capitulo221

    elif selected_route == "yellow":
        jump capitulo221

    elif selected_route == "silver":
        jump start

    elif selected_route == "gold":
        jump capitulo221

    $ renpy.notify("Você encontrou uma chave!")


    eu "oi"
    $ renpy.notify("Você encontrou Corajoso!")
    $ traco.append(("Corajoso","Você consegue agir mesmo diante do medo. Em situações difíceis, sua coragem pode abrir novos caminhos."))
    $ traco.append(("Medas","Você consegue agir mesmo diante do medo. Em situações difíceis, sua coragem pode abrir novos caminhos."))
    $ traco.append(("fasff","Você ssssssssss agir mesmo diante do medo. Em situações difíceis, sua coragem pode abrir novos caminhos."))
    $ traco.append(("xczc","Vo abrir novos caminhos."))
    $ traco.append(("asff","Você consegue agir mesmo diações difíceis, sua coragem pode abrir novos caminhos."))
    $ mochila.append(("Chave da Sala 3","Uma chave que abre a sala do professor Yuki."))
    $ mochila.append(("Chave da Sala 3","Uma chave que abre a sala do professor Yuki."))
    $ mochila.append(("Chave da Sala 3","Uma chave que abre a sala do professor Yuki."))


    "You're in {w=0.5}{b}MY{/b}{w=0.5} world now, you {i}little{/i} {color=#f00}punk  ssssds!"           #bem util para fazer efeito
    "Você hesita diante do perigo e perde a confiança."

    $remover_habilidade("Corajoso")
    $remover_habilidade("Medas")

    "Você já não se sente tão corajoso."


    $ iniciar_chuva(hard=True)
    show city_f1 onlayer fundo with dissolve
    show static_dante_f1 onlayer personagens at Transform(xpos=50, yalign=1.0) with dissolve
    show minazinha_f1 onlayer personagens at left with dissolve
    show static_dante_f1 onlayer personagens at Transform(xpos=180, yalign=1.0) with dissolve
    show static_dante_f1 onlayer personagens at Transform(xpos=500, yalign=1.0, xzoom=-1) with dissolve

    show static_dante_f1 onlayer personagens at Transform(xpos=500, yalign=1.0, xzoom=-1, matrixcolor=BrightnessMatrix(-0.1)) with dissolve
    show static_dante_f1 onlayer personagens at Transform(xpos=500, yalign=1.0, xzoom=-1, matrixcolor=BrightnessMatrix(0.0)) with dissolve
    minazinha "seu bumbum durinho"
    #hide sentado onlayer fundo
    #show _fundo_roxo onlayer fundo with dissolve
    hide sideimage onlayer screens
    "oi"
    scene fundo_preto
    show minazinha_f1
    $ renpy.notify("Você encontrou uma chave!???????????????????")
    "agora estamos na ruassssssssssssssssssssssssssssssssssssssssssssss\nsssssssssssssssssssssssssssssssssssssssssssssss"
    "agora no red denovo"
    "Parou de chover."
    $ parar_chuva(hard=True)
    "realmente parou"
    $ remover_item("Chave da Sala 3")
    $ remover_item("Chave da Sala 3")
    $ remover_item("Chave da Sala 3")
    menu:
        "oque faz"
        "Usar a Chave da Sala 3" if tem_item("Chave da Sala 3"):
            "Você pega a chave e abre a porta."
            $ remover_item("Chave da Sala 3")
        "Arrombar a porta" if tem_habilidade("Chave da Sala 3"):
            "Você tenta forçar a fechadura."
        "Ir embora":
            "Você decide continuar pelo corredor."
        "Ir embora":
            "Você decide continuar pelo corredor."
        "Ir embora":
            "Você decide continuar pelo corredor."
        "Ir embora":
            "Você decide continuar pelo corredor."
        "Ir embora":
            "Você decide continuar pelo corredor."
        "Ir embora":
            "Você decide continuar pelo corredor."
        "Ir embora":
            "Você decide continuar pelo corredor."
        "Ir embora":
            "Você decide continuar pelo corredor."

    "oi"

    "O que você quer se tornar?"
    menu:
        "Carrasco":
            $ estado_personagens[0]["titulo"] = "CARRASCO"
            jump arrombar_porta
        "Herói":
            $ estado_personagens[0]["titulo"] = "HERÓI"
        "Vilão":
            $ estado_personagens[0]["titulo"] = "VILÃO"
    "Você acabou de se transformar em um [estado_personagens[0]['titulo']]"
    "ola"


    label arrombar_porta:
    "Você está diante de uma porta trancada."
    menu:
        "Ação - >12 -":
            $ sucesso = teste_habilidade(12)
            if sucesso:
                "Você arromba a porta."
            else:
                "Você não consegue arrombar a porta."
        "Corajoso - >7 -" if tem_habilidade("Corajoso"):
            $ sucesso = teste_habilidade(7)
            if sucesso:
                "Você se joga pela janela e sai ileso."
            else:
                "Você se joga, mas se machuca um pouco."




    #jump capitulo1
    #call screen conceito
    "aqui quer dizer que funcionou"
    minazinha "You've created a new Ren'Py game."
    pause 1
    minazinha "Xxxxx"

    scene bgrua
    with dissolve
    show minazinha_f1 at left
    with dissolve
    show outramina_f1 at right
    "muito bom"
    hide minazinha_f1
    hide outramina_f1
    show parabens
    with dissolve


    "ei"


    menu:
        "sim eu fui":
            "Interessante, entao venha ate o cafe"
            minazinha "claro claro"
            $ foiprocafe = True
            jump cafe

        "nao eu nao fui":
            $ foiprocafe = False
            jump cafe

label cafe:
    scene fundo_preto
    if foiprocafe == True:
        eu "a eu fui sim"
        eu "e gastei [qntsCafe] contigo"
        eu "a variavel ??? está [foiprocafe]"
    else:
        "eu nao fui"

return

####   BOTAR MUSICA | PARA MUSICA  ####### play music "tudo/audio/prepare_your_swords.mp3"               |    stop music fadeout 1
####   TEXTO  CENTRADO #####                  centered "Em uma galáxia distante..2222222\nssdsd\nnnn."
###    NOTIFICAÇÃO  ####                   $ renpy.notify("Você encontrou uma chave!")
###   MOSTRAR O FUNDO    ####             show city_f1 onlayer fundo with dissolve                       |    hide city_f1 onlayer fundo
###   MOSTRAR PERSONAGEM  ###             show kyo_serio onlayer personagens at right with dissolve      |    hide kyo_serio onlayer personagens
###   DESBLOQUEAR  PERSONAGEM ###         $ persistent.unlocked_routes.append("prota2")
