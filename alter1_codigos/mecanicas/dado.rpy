
# ============================================================
# SISTEMA DE DADOS ANIMADOS - D20 E D100
# SUCESSO, FALHA, ACERTO CRITICO E ERRO CRITICO
# ============================================================

default dado_valor = 1
default dado_rolando = False
default dado_tipo_resultado = "rolando"


# ============================================================
# ANIMACAO DOS FUNDOS
# A IMAGEM NASCE PEQUENA E SE EXPANDE
# ============================================================

transform fundo_zoom:

    xalign 0.5
    yalign 0.5
    zoom 0.05
    alpha 0.0

    parallel:
        easeout 0.45 zoom 1.2

    parallel:
        easeout 0.20 alpha 1.0


# ============================================================
# NUMERO DURANTE A ROLAGEM
# ============================================================

transform numero_rolando:

    zoom 1.0


# ============================================================
# NUMERO FINAL - SUCESSO E FALHA
# CRESCE DO CENTRO ATE O TAMANHO NORMAL
# ============================================================

transform numero_zoom_normal:

    xalign 0.5
    yalign 0.5
    zoom 0.05
    alpha 0.0

    parallel:
        easeout 0.40 zoom 1.2

    parallel:
        easeout 0.20 alpha 1.0


# ============================================================
# NUMERO FINAL - RESULTADOS CRITICOS
# CRESCE, ULTRAPASSA O TAMANHO E VOLTA
# ============================================================

transform numero_zoom_critico:

    xalign 0.5
    yalign 0.5
    zoom 0.05
    alpha 0.0

    parallel:
        easeout 0.35 zoom 1.25
        easeout 0.12 zoom 1.0

    parallel:
        easeout 0.15 alpha 1.0


# ============================================================
# FUNCOES DO DADO
# ============================================================

init python:

    import random
    import os

    def atualizar_dado(lados=20):

        if store.dado_rolando:
            store.dado_valor = random.randint(1, lados)


    def finalizar_dado(lados=20, dificuldade=50):

        if not store.dado_rolando:
            return

        # Sorteia o resultado definitivo
        store.dado_valor = random.randint(1, lados)

        resultado = store.dado_valor

        # Classifica o resultado
        if resultado == 1:

            tipo = "erro_critico"

        elif lados == 100 and resultado == 100:

            tipo = "acerto_critico"

        elif resultado >= dificuldade:

            tipo = "sucesso"

        else:

            tipo = "falha"

        # Guarda o resultado
        store.dado_tipo_resultado = tipo

        # Encerra a rolagem
        store.dado_rolando = False

        # Sons para cada resultado
        sons = {
            "acerto_critico":
                "audio/dado_critico.ogg",

            "sucesso":
                "audio/dado_sucesso.ogg",

            "falha":
                "audio/dado_falha.ogg",

            "erro_critico":
                "audio/dado_falha_critica.ogg",
        }

        caminho_som = sons.get(tipo)

        # Toca o som se o arquivo existir
        if caminho_som:

            caminho_completo = os.path.join(
                config.gamedir,
                caminho_som
            )

            if os.path.isfile(caminho_completo):

                renpy.sound.play(caminho_som)


# ============================================================
# TELA DE ROLAGEM ANIMADA
# ============================================================

screen animacao_dado(lados=20, duracao=2, dificuldade=50):

    modal True
    zorder 300

    # Fundo escuro
    add Solid("#000000CC")

    # --------------------------------------------------------
    # FUNDO PADRAO DURANTE A ROLAGEM
    # --------------------------------------------------------

    if dado_rolando:

        add "tudo/imagem/mecanicas/dado_padrao.png":
            xysize (1920, 1080)

    # --------------------------------------------------------
    # ACERTO CRITICO
    # --------------------------------------------------------

    elif dado_tipo_resultado == "acerto_critico":

        add "tudo/imagem/mecanicas/dado_critico_positivo.png":
            xysize (1920, 1080)
            at fundo_zoom

    # --------------------------------------------------------
    # SUCESSO NORMAL
    # --------------------------------------------------------

    elif dado_tipo_resultado == "sucesso":

        add "tudo/imagem/mecanicas/dado_sucesso.png":
            xysize (1920, 1080)
            at fundo_zoom

    # --------------------------------------------------------
    # FALHA NORMAL
    # --------------------------------------------------------

    elif dado_tipo_resultado == "falha":

        add "tudo/imagem/mecanicas/dado_falha.png":
            xysize (1920, 1080)
            at fundo_zoom

    # --------------------------------------------------------
    # ERRO CRITICO
    # --------------------------------------------------------

    elif dado_tipo_resultado == "erro_critico":

        add "tudo/imagem/mecanicas/dado_critico_negativo.png":
            xysize (1920, 1080)
            at fundo_zoom

    # --------------------------------------------------------
    # NUMERO DURANTE A ROLAGEM
    # --------------------------------------------------------

    if dado_rolando:

        text "[dado_valor]":

            xalign 0.5
            yalign 0.5

            size 100
            color "#FFFFFF"

            outlines [(4, "#D9B66C")]

            at numero_rolando

    # --------------------------------------------------------
    # NUMERO FINAL COM ANIMACAO
    # --------------------------------------------------------

    else:

        if dado_tipo_resultado == "acerto_critico":

            $ cor_numero = "#FFD700"
            $ animacao_numero = numero_zoom_critico

        elif dado_tipo_resultado == "erro_critico":

            $ cor_numero = "#FF3333"
            $ animacao_numero = numero_zoom_critico

        elif dado_tipo_resultado == "sucesso":

            $ cor_numero = "#8CFF9B"
            $ animacao_numero = numero_zoom_normal

        else:

            $ cor_numero = "#FFFFFF"
            $ animacao_numero = numero_zoom_normal

        text "[dado_valor]":

            xalign 0.5
            yalign 0.5

            size 120
            color cor_numero

            outlines [(4, "#000000")]

            at animacao_numero

    # --------------------------------------------------------
    # CONTROLE DOS TEMPORIZADORES
    # --------------------------------------------------------

    if dado_rolando:

        timer 0.08 repeat True action Function(
            atualizar_dado, lados
        )

        timer duracao action Function(
            finalizar_dado, lados, dificuldade
        )

    else:

        # Mantem o resultado na tela por 1.5 segundos
        timer 1.5 action Return(dado_valor)


# ============================================================
# FUNCAO QUE INICIA A ROLAGEM
# ============================================================

init python:

    def rolar_dado_animado(
        lados=100,
        duracao=2,
        dificuldade=50
    ):

        # Impede valores invalidos
        if lados < 2:
            lados = 2
        # Prepara a rolagem
        store.dado_rolando = True
        store.dado_tipo_resultado = "rolando"
        store.dado_valor = renpy.random.randint(1, lados)
        # Abre a tela e aguarda o resultado
        resultado = renpy.call_screen(
            "animacao_dado",
            lados=lados,
            duracao=duracao,
            dificuldade=dificuldade)
        return resultado
# ============================================================
# SISTEMA DE TESTE DE DIFICULDADE
# ============================================================
init python:
    def dificuldade_teste(
        dificuldade,
        lados=100,
        duracao=2
    ):
        resultado = rolar_dado_animado(
            lados=lados,
            duracao=duracao,
            dificuldade=dificuldade)
        # Erro critico
        if resultado == 1:
            return "erro_critico"
        # Acerto critico exclusivo do D100
        if lados == 100 and resultado == 100:
            return "acerto_critico"
        # Sucesso normal
        if resultado >= dificuldade:
            return "sucesso"
        # Falha normal
        return "falha"
