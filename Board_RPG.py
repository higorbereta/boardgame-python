import personagem

def menu():

    qnt_personagem = 0

    if(qnt_personagem <= 0):
        print("Por favor, cadastre os dados do primeiro personagem!")
        nome_personagem, raca_pers, classe_pers, nivel_pers, exp_perso = personagem.cadastra_personagem()
    
    encerrar = False
    while(not encerrar):
        menu_option = int(input("Opções de Visualização:\n 1 - Ficha de Personagem\n 0 - Encerrar\nQual opção deseja acessar? "))
        if(menu_option == 1):
            print("============ <> ============")
            print("Ficha de Personagem")
            personagem.ficha_personagem(nome_personagem,raca_pers,classe_pers,nivel_pers,exp_perso)
        if(menu_option == 0):
            encerrar = True


if(__name__ == "__main__"):
    menu()