
#-------------------------EFEITOS CLIMA--------------------------------------
image chuva = Movie(play="images/chuva.webm",size=(1920,1080) ,loop=True)
init python:
    config.layers = ["master","clima","fundo","personagens","transient","screens","overlay"]
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

image minazinha_f1 = "minazinha1-1.png"
image outramina_f1 = "outraminazinha1-1.png"
image parabens = "parabens.png"
image sentado = "kyocentado.png"
image kyo_serio= "kyo_dialogo_serio.png"
image kyo_side_serio= "kyo_side_serio.png"

image city_f1 = "images/fundos/cidade_f1.png"

image static_dante_f1 = "images/dante/static_dante_f1.png"

image _fundo_roxo = "fundo_roxo.png"

default foiprocafe = False
default qntsCafe = 3
default sucesso = 0



label start:
    play music "musics/prepare_your_swords.mp3"
    show screen hud
    scene fundo_preto
    centered "Em uma galáxia distante..2222222\nssdsd\nnnn."
    $ renpy.notify("Você encontrou uma chave!")

    $ showsideimage("kyo_side_serio")
    eu "oi"
    $ renpy.notify("Você encontrou Corajoso!")
    $ perks.append(("Corajoso","Você consegue agir mesmo diante do medo. Em situações difíceis, sua coragem pode abrir novos caminhos."))
    $ perks.append(("Medas","Você consegue agir mesmo diante do medo. Em situações difíceis, sua coragem pode abrir novos caminhos."))
    $ perks.append(("fasff","Você ssssssssss agir mesmo diante do medo. Em situações difíceis, sua coragem pode abrir novos caminhos."))
    $ perks.append(("xczc","Vo abrir novos caminhos."))
    $ perks.append(("asff","Você consegue agir mesmo diações difíceis, sua coragem pode abrir novos caminhos."))
    $ mochila.append(("Chave da Sala 3","Uma chave que abre a sala do professor Yuki."))
    $ mochila.append(("Chave da Sala 3","Uma chave que abre a sala do professor Yuki."))
    $ mochila.append(("Chave da Sala 3","Uma chave que abre a sala do professor Yuki."))


    "You're in {w=0.5}{b}MY{/b}{w=0.5} world now, you {i}little{/i} {color=#f00}punk  ssssds!"           #bem util para fazer efeito
    "Você hesita diante do perigo e perde a confiança."

    $remover_habilidade("Corajoso")
    $remover_habilidade("Medas")

    "Você já não se sente tão corajoso."

    stop music fadeout 1
    $ iniciar_chuva(hard=True)
    show city_f1 onlayer fundo with dissolve
    #show sentado onlayer fundo with dissolve
    show kyo_serio onlayer personagens at right with dissolve
    show static_dante_f1 onlayer personagens at left with dissolve

    show minazinha_f1 onlayer personagens
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
