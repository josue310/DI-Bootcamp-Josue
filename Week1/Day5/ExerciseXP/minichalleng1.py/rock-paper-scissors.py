# from ipynb.fs.full.game import Game
from game import Game
def get_user_menu_choice():
    print("------MENU------")
    choice = input(f"(P) : Play a new game \n(S) : Show scores\n(Q) : Quit\n").lower()
    if choice in ['p', 's', 'q']:
        return choice
    else:
        return get_user_menu_choice()

def print_results(results):
    print("---GAME STATS---")
    gagne = results.get("win",0)
    perdu = results.get("loss",0)
    egal = results.get("draw",0)
    t = gagne + perdu + egal
    print(f"Total games played : {t}")
    print(f"Wins   : {gagne}")
    print(f"Losses : {perdu}")
    print(f"Draws  : {egal}")
    print("Thank you for playing Rock-Paper-Scissors! See you next time! \n")


def main():
    # 1. On initialise le dictionnaire des scores
    scores = {"win": 0, "loss": 0, "draw": 0}
    
    # 2. Boucle répétitive pour afficher le menu en continu
    while True:
        choix = get_user_menu_choice()
        
        if choix == 'p':
            # On crée l'objet de la classe Game
            nouvelle_partie = Game()
            # On lance la partie et on récupère le résultat ("win", "loss" ou "draw")
            resultat_partie = nouvelle_partie.play()
            
            # On met à jour le dictionnaire des scores
            scores[resultat_partie] += 1
            print("\nGame recorded!\n")
            
        elif choix == 's':
            # On affiche les scores actuels
            print_results(scores)
            
        elif choix == 'q':
            # L'utilisateur quitte : on affiche le résumé final et on arrête la boucle
            print("\n--- FINAL RESULTS ---")
            print_results(scores)
            break

# Cette ligne permet de lancer automatiquement le jeu quand on exécute ce fichier
if __name__ == "__main__":
    main()
