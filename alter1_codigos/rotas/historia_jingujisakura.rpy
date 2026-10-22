define Boch = Character("???")
define Nomura = Character("???")
image cenario_jinguji_c1 = "tudo/imagem/jinguji_s/cenario/cenario_jinguji_c1.png"
image cenario_jinguji_a2 = "tudo/imagem/jinguji_s/cenario/cenario_jinguji_a2.png"




label jinguji_historia:
    scene fundo_preto
    $ traco.append(("Atleta","Anos de corrida prepararam você para correr grandes distancias."))
    $ traco.append(("Coragem","Anos de corrida prepararam você para correr grandes distancias."))
    $ traco.append(("Perseverante","Anos de corrida prepararam você para correr grandes distancias."))
    $ traco.append(("Robustez","Anos de corrida prepararam você para correr grandes distancias."))
    $ nome_jinguji = "Jinguji Sakura"
    $ estado_personagens[0]["titulo"] = "ESTUDANTE"
    $ estado_personagens[0]["nome"] = "Jinguji Sakura"
    $ estado_personagens[0]["idade"] = "17"
    $ estado_personagens[0]["traco"] = "Atleta"
    $ estado_personagens[0]["medo"] = "Pai"
    $ estado_personagens[0]["foto"] = "tudo/imagem/jinguji_s/jingujisakura_glos_f1.png"
    $ jinguji_sakura = DynamicCharacter("nome_jinguji")
    $ definir_pontos_mentais(100)
    jump historia_jinguji_cap01
    return
###########################################################-------------------------------------------------------------------############################################
label historia_jinguji_cap01:

    centered "{cps=15}{i}Aquele que consagra a própria existência à busca incessante da perfeição corre o risco de transformar suas maiores virtudes em instrumentos de sua própria ruína, pois, ao contemplar continuamente aquilo que ainda lhe falta, torna-se incapaz de reconhecer a grandeza do que já conquistou.{w=0.5} .{w=0.5} .{w=0.5}{/i}{/cps}"
    centered "{cps=15}Capitulo 01\n {w=1} Um Dia Expecionalmente Comum{/cps}"


    $ iniciar_chuva(hard=True)
    $ Nomura.name = "Personagem A"
    $ Boch.name = "Personagem B"
    scene cenario_jinguji_c1 with dissolve

    Nomura "Imprestavel… Sinceramente, é a única palavra que me vem à cabeça quando olho pra você."
    Boch "Ah, vai se foder! O QUE CARALHOS VOCÊ QUERIA QUE EU FIZESSE?!"
    Boch "ERAM QUATRO DISTORÇÕES! QUATRO! Duas de Manifestação, uma de Praga e uma de Fenda! Você tem noção do que é ter que lidar com tudo isso ao mesmo tempo?!"
    Boch "A gente foi enviado pra FECHAR UMA FENDA! Era só isso! Mas aí uma Distorção de Praga saiu daquela merda e tudo foi pro inferno!"
    scene cenario_jinguji_a2
    Boch "Então me diz, já que você parece saber exatamente o que fazer… O QUE VOCÊ TERIA FEITO NO MEU LUGAR?!"
    Nomura "O mínimo. Eu teria feito o mínimo que se espera de alguém na sua posição como sacertode."


    show screen hud
    show screen mostrar_estado_mental
    jinguji_sakura "eae"
    $ definir_pontos_mentais(199)

    menu:
        "Faço o que?"
        "Olho para o lado [Pertubado]" if estado_mental == "Pertubado":
            "Nao gostei"
        "Me lanço pela janela (Dificuldade 40)" if estado_mental == "Neutro":
            $ resultado = dificuldade_teste(40)
            if resultado == "acerto_critico":
                "ACERTO CRÍTICO! Você consegue realizar um feito extraordinário."
            elif resultado == "erro_critico":
                "ERRO CRÍTICO! Algo terrível acontece."
            elif resultado == "sucesso":
                "Você passou no teste!"
            else:
                "Você falhou!"
                $ alterar_pontos_mentais(100)
        "Me lanço pela janela (Dificuldade 60)" if tem_habilidade("Atleta"):
            $ resultado = dificuldade_teste(60)

            if resultado == "acerto_critico":
                "ACERTO CRÍTICO! Você consegue realizar um feito extraordinário."

            elif resultado == "erro_critico":
                "ERRO CRÍTICO! Algo terrível acontece."

            elif resultado == "sucesso":
                "Você passou no teste!"
            else:
                "Você falhou!"
    Boch "A gente foi enviado pra FECHAR UMA FENDA! Era só isso! Mas aí uma Distorção de Praga saiu daquela merda e tudo foi pro inferno!"
    Boch "A gente foi enviado pra FECHAR UMA FENDA! Era só isso! Mas aí uma Distorção de Praga saiu daquela merda e tudo foi pro inferno!"
    Boch "A gente foi enviado pra FECHAR UMA FENDA! Era só isso! Mas aí uma Distorção de Praga saiu daquela merda e tudo foi pro inferno!"
    return
