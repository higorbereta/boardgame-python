import atributos
import Board_RPG

def cadastra_personagem():
    print("============ <> ============")
    nome = input("Nome Personagem -> ")
    raca = input("Raça: [Humanos, Elfos, Anões, Meio Elfo] -> ")
    classe = input("Classe: [Mago, Guerreiro, Arqueiro, Ladino, Monge, Paladino] -> ")
    nivel = 1
    exp = 0
    print("============ <> ============")

    atributos.new_atrib()

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
    Board_RPG.menu()