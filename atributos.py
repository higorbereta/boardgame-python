def new_atrib():
    print("Você poderá distribuir um total de 20 pontos de atributos.[FORÇA, DESTREZA, CONSTITUIÇAO, INTELIGÊNCIA, SABEDORIA E CARISMA]")
    
    confirmar = False

    while(not confirmar):
        atrib_for = int(input("Força: "))
        atrib_dex = int(input("Destreza: "))
        atrib_const = int(input("Constituição: "))
        atrib_int = int(input("Inteligência: "))
        atrib_wis = int(input("Sabedoria: "))
        atrib_charis = int(input("Carisma: "))

        total_distrib = atrib_for + atrib_dex + atrib_const + atrib_int + atrib_wis + atrib_charis
        pts_restantes = 20 - total_distrib

        if(pts_restantes < 0):
            print("Você distribui {} pontos acima do que permitido. Corrija !".format(pts_restantes))
        if(pts_restantes > 0):
            print("Faltam {} pontos a serem distribuidos.".format(pts_restantes))
        if(pts_restantes == 0):
            escolha_confirm = input("Digite 1 para confirmar ou outra tecla para reiniciar -> ")
            if(int(escolha_confirm) == 1):
                print("CONFIRMADO !!!")
                confirmar = True
                return atrib_for, atrib_dex, atrib_const, atrib_int, atrib_wis, atrib_charis
            else: 
                print("REINICIANDO !!!")

if(__name__ == "__main__"):
    new_atrib()