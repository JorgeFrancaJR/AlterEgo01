image cenario_jinguji_f1 = "tudo/imagem/jinguji_s/cenario/cenario_jinguji_f1.png"




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
    jump historia_jinguji_cap01
    return

label historia_jinguji_cap01:
    centered "{cps=15}{i}Aquele que consagra a própria existência à busca incessante da perfeição corre o risco de transformar suas maiores virtudes em instrumentos de sua própria ruína, pois, ao contemplar continuamente aquilo que ainda lhe falta, torna-se incapaz de reconhecer a grandeza do que já conquistou.{w=0.5} .{w=0.5} .{w=0.5}{/i}{/cps}"
    centered "{cps=15}Capitulo 01\n {w=1} Um Dia Expecionalmente Comum{/cps}"
    show screen hud
    $ iniciar_chuva(hard=True)
    show cenario_jinguji_f1 onlayer fundo with dissolve
    menu:
        "Eu repentinamente..."
        "Me lanço pela janela (Dificuldade 10)":
            if dificuldade_teste(10):
                "Você salta pela janela e consegue aterrissar sem sofrer dano."
            else:
                "Você cai de mau jeito e quebra a perna."

        "Procurar outra saída":
            "Você decide procurar outro caminho."
    jinguji_sakura "eae"
    return
