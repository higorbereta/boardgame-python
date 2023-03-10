def menu():

    qnt_personagem = 0

    if(qnt_personagem <= 0):
        print("Por favor, cadastre os dados do primeiro personagem!")
        nome_personagem, raca_pers, classe_pers, nivel_pers, exp_perso = cadastra_personagem()
    
    encerrar = False
    while(not encerrar):
        menu_option = int(input("Opções de Visualização:\n 1 - Ficha de Personagem\n 0 - Encerrar\nQual opção deseja acessar? "))
        if(menu_option == 1):
            print("============ <> ============")
            print("Ficha de Personagem")
            ficha_personagem(nome_personagem,raca_pers,classe_pers,nivel_pers,exp_perso)
        if(menu_option == 0):
            encerrar = True


def cadastra_personagem():
    print("============ <> ============")
    nome = input("Nome Personagem -> ")
    raca = input("Raça: [Humanos, Elfos, Anões, Meio Elfo] -> ")
    classe = input("Classe: [Mago, Guerreiro, Arqueiro, Ladino, Monge, Paladino] -> ")
    nivel = 1
    exp = 0
    print("============ <> ============")

    return nome, raca, classe, nivel, exp


def ficha_personagem(nome_pers, raca, classe,nivel,exp):
    print("=============[]=============\n Nome: {}\n Raça: {}\n Classe: {}".format(nome_pers,raca,classe))
    
    next_level = nivel * 5 + 5
    pend_exp = next_level - exp

    while(pend_exp <= 0):
        nivel = nivel + 1
        exp = exp - next_level
        next_level = nivel * 5 + 5
        pend_exp = next_level - exp

    print(" Nível: {}\n Exp: {} / {}".format(nivel,exp,next_level))
    print("=============[]=============")


if(__name__ == "__main__"):
    menu()