#!/usr/bin/env python3

BUFF_OPTIONS = {
    "1": "Tu as trop pris confiance, je ne vais pas te donner 20% de dégâts en plus, t'es un fou !",
    "2": "Tu as trop pris confiance, je ne vais pas te donner 20% de soin en plus, t'es un fou !",
    "3": "Tu as trop pris confiance, je ne vais pas te donner 20% de vie en plus, t'es un fou !",
    "4": "Tu as trop pris confiance, je ne vais pas te donner 20% de défense en plus, t'es un fou !",
    "5": "Voilà un champion ! T'as intérêt à le massacrer ce boss !"
}

def bv_message():
    print("Bienvenue bob dans le monde magique de erutnevdA ruoY esoohC\n" +
          "Aujourd'hui nous nous retrouvons au boss final qui vous permettra de gagner le coeur de la princesse\n")

def v_name():
    name = input("Avant de commencer pouvez-vous me rappeler votre nom : ")
    if name.lower() == "bob":
        print("Ouf, j'ai cru que tu étais un usurpateur\n")
        return True
    else:
        print("T'es qui ? Je te connais pas ! Sors de mon jeu !\n")
        return False

def display_buff_options():
    print("Bien, commençons par se donner des buffs :")
    print(" - 20% de dégat\n" + " - 20% de soin en plus\n" + " - 20% de vie en plus\n" + " - 20% de défense en plus\n " + "- -20% de tout\n")

def select_buff_option():
    buff = input("<R> Quelle option choisissez-vous (1, 2, 3, 4, 5) ? ")
    if buff in BUFF_OPTIONS:
        print(BUFF_OPTIONS[buff])
    else:
        print("Option invalide, choisissez parmi les options disponibles.")
        select_buff_option()
        
def phase1():
    calcul_niveau_primaire = input("<E> Combien cela vaut 9-3/(1/3)+1 = ")
    if calcul_niveau_primaire == "1":
        print("<V> Bravo, tu peux passer à la suite\n")
        print("Phase 2 enclanché")
    else:
        print("C'est faux, retente une prochaine fois !")
        exit()

def phase2():
    calcul_niveau_collège = input("<E> Combien cela vaut ((4×5)−20)/4 = ")
    if calcul_niveau_collège == "0":
        print("<R> Bravo, tu peux passer à la suite\n")
        print("Phase Final enclanché")
    else:
        print("C'est faux, retente une prochaine fois !")
        exit()
        
def phaseFinal():
    nom = input("<SE> Quelle est le nom de ce jeu : ")
    if nom == "Choose Your Adventure":
        print(" Bravo, le  boss a était vaincus, tu peux récupérer ta récompense à cette adresse : https://urlz.fr/qqrz")
    else:
        print("Tu y était presque, retente le coup, une prochaine fois")
    
        
def main():
    bv_message()
    if not v_name():
        return
    display_buff_options()
    select_buff_option()
    phase1()
    phase2()
    phaseFinal()

if __name__ == "__main__":
    main()
