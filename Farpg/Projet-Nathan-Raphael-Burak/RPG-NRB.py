import cmd 
import textwrap
import sys
import os 
import time 
import random 
import pickle
import math

screen_width = 100 

# Player Setup 
class player:
    def __init__(self):
        self.name=''
        self.job = ''
        self.lvl = 1
        self.hp = 0
        self.hpmax = 0
        self.mp = 0
        self.atk = 0
        self.md = 0
        self.df = 0
        self.location = 'Underworld'
        self.status_effects = []
        self.game_over = False
        self.souls = 0
        self.xp = 0
        self.xpbarre = 10
        self.loot = ['shield']
myPlayer = player()


class warrior:
    def __init__(self):
        self.name=''
        self.lvl = 1
        self.job = ''
        self.hp = 100   
        self.mp = 10
        self.atk = 3000
        self.md = 5
        self.df = 3
        self.location = 'Underworld'
        self.status_effects = []
        self.game_over = False
        self.souls = 0
        self.xp = 0
        self.xpbarre = 10
myPlayer = warrior()



# Enemy setup
class gobelin:
    def __init__(self):
        self.name = 'gobelin'
        self.hp = 20
        self.atk = 10
        self.mp = 0
        self.md = 0
        self.df = 1
        self.location = ''
gobelin = gobelin()

class slime:
    def __init__(self):
        self.name = 'slime'
        self.hp = 10
        self.atk = 12
        self.mp = 0
        self.md = 0
        self.df = 0
        self.location = ''
slime = slime()

class superslime:
    def __init__(self):
        self.name = 'Superslime'
        self.hp = 1
        self.atk = 45
        self.mp = 0
        self.md = 0
        self.df = 0
        self.location = ''
superslime = superslime()

class troll:
    def __init__(self):
        self.name = 'troll'
        self.hp = 70
        self.hpmax = 70
        self.atk = 30
        self.mp = 0
        self.md = 0
        self.df = 3
        self.location = ''
troll = troll()

class spider:
    def __init__(self):
        self.name = 'spider'
        self.hp = 20
        self.atk = 2
        self.mp = 0
        self.md = 0
        self.df = 0
        self.location = ''
spider = spider()

class skelleton:
    def __init__(self):
        self.name = 'skelleton'
        self.hp = 100
        self.atk = 5
        self.mp = 0
        self.md = 0
        self.df = 5
        self.location = ''
skelleton = skelleton()


class macichien:
    def __init__(self):
        self.name = 'macichien'
        self.hp = 50
        self.atk = 0
        self.mp = 20
        self.md = 10
        self.df = 1
        self.location = ''
macichien = macichien()
########## Boss #########

class wamuuuuuu:
    def __init__(self):
        self.name = 'wamuuuuuu'
        self.hp = 300
        self.atk = 20
        self.mp = 0
        self.md = 0
        self.df = 10
        self.location = 'Lac'
wamuuuuuu = wamuuuuuu()

class Laddepascal:
    def __init__(self):
        self.name = 'La d. de pascal'
        self.hp = 300
        self.atk = 20
        self.df = 1
        self.mp = 0
        self.md = 0
        self.location = 'Plaine V'
Laddepascal = Laddepascal()
class Aizen:
    def __init__(self):
        self.name = 'Aizen'
        self.df = 1
        self.hp = 300
        self.atk = 20
        self.mp = 0
        self.md = 0
        self.location = 'Désert Montagneux'
Aizen = Aizen()

class Enma:
    def __init__(self):
        self.name = 'Enma'
        self.hp = 300
        self.df = 1
        self.atk = 20
        self.mp = 0
        self.md = 0
        self.location = 'Camp'
Enma = Enma()

class Doflamingo:
    def __init__(self):
        self.name = 'Doflamingo'
        self.hp = 300
        self.df = 1
        self.atk = 20
        self.mp = 0
        self.md = 0
        self.location = 'Ishbal'
Doflamingo = Doflamingo()

class Kaido:
    def __init__(self):
        self.name = 'Kaido'
        self.hp = 300
        self.df = 1
        self.atk = 20
        self.mp = 0
        self.md = 0
        self.location = 'Fôret Noir'
Kaido = Kaido()



#loot
def loot():
    
    print("You have 3 option",myPlayer.job)
    choice = input("1. potion \n2. augmentation physique \n3. augmentation magique\n")
    loot = ["potion", "augmentation physique", "augmentation magique"]
    return choice

def lootEffect(choice, myPlayer):
    if choice == "1":
        myPlayer.hp = myPlayer.hp + 20
        print ("Tu as bu une potion, oh ton hp a augmenté de 20!")
        print ("Du coup tu as au total", myPlayer.hp, "hp")
        return myPlayer
    elif choice == "2":
        myPlayer.atk = myPlayer.atk + 2
        print("tu as reçu une augmentation physique")
        print("Cela semble avoir augmenté ton atk")
        return myPlayer
    elif choice == "3":
        myPlayer.md = myPlayer.md + 3
        myPlayer.mp = myPlayer.mp + 2
        print("tu as reçu une augmentation de tes mp")
        print("Cela semble avoir augmenté ton intelligence (vieux debile)")
        return myPlayer

# échec pour essayer de faire un loot spéciale pour les boss et de les print par la suite 
# def lootDropbossweaponwamuu():
    # loot = [""]
    # loot.append(shield)
    # myPlayer.df = myPlayer.df + 5
    # return lootDropbossweaponwamuu


# Title Screen 
def title_screen_selection():
    option = input(">")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("loadgame"):
        load_game() 
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    elif option.lower() == ("help"):
        help_menu()
    while option.lower() not in ['play', 'help', 'quit', 'back', 'loadgame']:
        print("please enter a valid command")
        option = input(">")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("loadgame"):
            load_game()
        elif option.lower() == ("quit"):
            sys.exit()
        elif option.lower() == ('back'):
            back_funct()

def load_screen_selection():
    option = input(">")
    if option.lower() == ("load-game"):
        load()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("back"):
        back_funct()
    while option.lower() not in ['load-game', 'help', 'back']:
        print("please enter a valid command")
        option = input(">")
    if option.lower() == ("load-game"):
        load()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("back"):
        back_funct()      


def title_screen():
    os.system('cls')
    print('+----------------------------+')
    print('+   Welcome to NaRaBu RPG    +')
    print('+----------------------------+')
    print('+          - Play -          +')
    print('+       - loadgame -         +')
    print('+         - Help -           +')        
    print('+         - Quit -           +')   
    print('+  - Copyright 2020 rpg -    +') 
    print('+----------------------------+')
    title_screen_selection()  

def load_game():
    os.system('cls')
    print('+----------------------------+')
    print('+-------- LoadGame ----------+')
    print('+----------------------------+')
    print('+       - load-game -         +')
    print('+----------------------------+')
    print('+         - Help -           +')        
    print('+         - Back -           +')   
    print('+   - Copyright 2020 rpg -   +')  
    print('+----------------------------+')
    load_screen_selection() 

def help_menu():
    os.system('cls')
    print('+------------------------------------------------------+')
    print('+               Welcome to Project RPG                 +')
    print('+------------------------------------------------------+')
    print('+: Type go north, go south, go west, go east to move  :+')
    print('+          -: Type the commands to do them :-          +')        
    print('+        -: Use "look" to inspect something :-         +')   
    print('+            -: Good Luck and have fun :-              +') 
    print('+                    -: Back :-                        +') 
    print('+------------------------------------------------------+')
    title_screen_selection()



def back_funct():
    os.system('cls')
    print('+----------------------------+')
    print('+   Welcome to Project RPG   +')
    print('+----------------------------+')
    print('+         - Play -           +')
    print('+       - loadgame -         +')
    print('+         - Help -           +')        
    print('+         - Quit -           +')   
    print('+  - Copyright 2020 rpg -    +') 
    print('+----------------------------+')  
    title_screen_selection()  

######Save / Load ######
# systeme pour load une game en verifiant si uu fichier 'savefile' si oui oui il va lire le binaire dans le code pour ensuite le load 
def load():
    if os.path.exists("savefile") == True:
        os.system('cls')
        with open('savefile', 'rb') as f:
            global myPlayer
            myPlayer = pickle.load(f)
        print("Chargement.........")
        input(">")
        viewstat()
    else: 
        print("Aucune partie n'a été sauvegardé ")
        title_screen()

###### MAP ########

DESCRIPTION = 'DESCRIPTION'
EXAMINATION = 'info'
SOLVED = False
UP = 'go north',
DOWN = 'go south',
LEFT = 'go west',
RIGHT = 'go east',

# on mis en place ce dictionnaire pour pouvoir dire qu'on est déja passé dessus et qu'on à déjà tué le boss mais pas on a ne l'a pas add encore
solved_place = {'Fôret Noir': False, 'Plaine V': False, 'Village': False, 'Village de Briggs': False,
               'Market Place': False, 'Melt Town': False, 'Port de Melt': False, 'Montagne West': False,
               'Silk Road': False, 'Camp': False, 'Lac': False, 'Désert Montagneux': False,
               'Frontière': False, 'Xing': False, 'Ishbal': False, 'Underworld': False,
                }

zone_map = {
        # a1
        'Fôret Noir': {
            DESCRIPTION: " Personne n'est revenu de cet endroit...",
            EXAMINATION: 'info',
            UP: 'Frontière', 
            DOWN: 'Market Place', 
            LEFT: 'Village de Briggs', 
            RIGHT: 'Plaine V',
            
        },
        # a2
        'Plaine V': {
            DESCRIPTION: "Cette plaine est vaste et inhabitable ",
            EXAMINATION: 'info',
            SOLVED: False,
            UP: 'Xing', 
            DOWN: 'Melt Town', 
            LEFT: 'Fôret Noir', 
            RIGHT: 'Village ',
        },
        # a3
        'Village': {
            DESCRIPTION: "Village très peu animé",
            EXAMINATION: '',
            SOLVED: False,
            UP: 'Ishbal',
            DOWN: 'Port de melt',
            LEFT: 'Plaine V',
            RIGHT: 'Village de Briggs',
        },
        # a4
        'Village de Briggs': {
            DESCRIPTION: "Village frontalier",
            EXAMINATION: 'info',
            SOLVED: False,
            UP: 'Underworld',
            DOWN: 'Montagne East',
            LEFT: 'Village',
            RIGHT: 'Fôret Noir',
        },
        # b1
        'Market Place': {
            DESCRIPTION: "Tu y trouveras de tout",
            EXAMINATION: 'info',
            SOLVED: False,
            UP: 'Fôret Noir',
            DOWN: 'Silk Road',
            LEFT: 'Montagne East',
            RIGHT: 'Melt Town',
        },
        # b2
        'Melt Town': {
            DESCRIPTION: "La Capital d'Amestris",
            EXAMINATION: 'info',
            SOLVED: False,
            UP: 'Plaine V',
            DOWN: 'Camp',
            LEFT: 'Market Place',
            RIGHT: 'Port de Melt',
        },
        # b3
        'Port de Melt': {
            DESCRIPTION: "Un Accès plus rapide à plusieurs endroits",
            EXAMINATION: 'info',
            SOLVED: False,
            UP: 'Village',
            DOWN: 'Lac',
            LEFT: 'Melt Town',
            RIGHT: 'Montagne East',
        },
        # b4
        'Montagne East': {
            DESCRIPTION: "Terrain glissant!!Attention!!",
            EXAMINATION: 'info',
            SOLVED: False,
            UP: 'Village de Briggs',
            DOWN: 'Désert Montagneux',
            LEFT: 'Port de Melt',
            RIGHT: 'Market Place',
        },
        # c1
        'Silk Road': {
            DESCRIPTION: "Attention aux voleurs et aux monstres",
            EXAMINATION: 'info',
            SOLVED: False,
            UP: 'Market Place',
            DOWN: 'Frontière',
            LEFT: 'Désert Montagneux',
            RIGHT: 'Camp',
        },
        # c2
        'Camp': {
            DESCRIPTION: "Campement abandonné",
            EXAMINATION: 'info',
            SOLVED: False,
            UP: 'Melt Town',
            DOWN: 'Xing',
            LEFT: 'Silk Road',
            RIGHT: 'Lac',
        },
        # c3
        'Lac': {
            DESCRIPTION: "Une légende raconte qu'un monstre y habite",
            EXAMINATION: 'info',
            SOLVED: False,
            UP: 'Port de Melt',
            DOWN: 'Ishbal',
            LEFT: 'Camp',
            RIGHT: 'Désert Montagneux',
        },
        # c4
        'Désert Montagneux': {
            DESCRIPTION: "Cet endroit te servira pour monter en niveaux ",
            EXAMINATION: 'info',
            SOLVED: False,
            UP: 'Montagne East',
            DOWN: 'Underworld',
            LEFT: 'Lac',
            RIGHT: 'Silk Road',
        },
        # d1
        'Frontière': {
            DESCRIPTION: " Frontière non surveillé ",
            EXAMINATION: 'info',
            SOLVED: False,
            UP: 'Silk Road',
            DOWN: 'Fôret Noir',
            LEFT: 'Underworld',
            RIGHT: 'Xing',
        },
        # d2
        'Xing': {
            DESCRIPTION: "Ville de l'élixirologie",
            EXAMINATION: 'info',
            SOLVED: False,
            UP: 'Camp',
            DOWN: 'Plaine V',
            LEFT: 'Frontière',
            RIGHT: 'Ishbal',
        },
        # d3
        'Ishbal': {
            DESCRIPTION: 'Village detruit par la guerre',
            EXAMINATION: 'info',
            SOLVED: False,
            UP: 'Lac',
            DOWN: 'Village',
            LEFT: 'Xing',
            RIGHT: 'Underworld',
        },
        # d4
        'Underworld': {
            DESCRIPTION: 'Vaste désert où les morts ressuscitent ',
            EXAMINATION: "L'endroit semble calme, vous y voyez des cadavres. Certains vous ressemblent.",
            SOLVED: False,
            UP: 'Désert Montagneux',
            DOWN: 'Village de Briggs',
            LEFT: 'Ishbal',
            RIGHT: 'Frontière',
        },
        
    
    }




######## Game interactivity #############
def print_location():
    os.system('cls')
    print("+" + ('-' * (4 +len(myPlayer.location))) + "+")
    print("<  " + myPlayer.location.upper() + "  >")
    print("+" + ('-' * (4 +len(myPlayer.location))) + "+")
    print(">" + (zone_map[myPlayer.location][DESCRIPTION]))
    # print(">" + (zone_map[myPlayer.location][EXAMINATION]))
    
def prompt():
    print("+========================+")
    print('> Tu veux faire quoi? <')
    print("+========================+")
    print("[-] move / go ")
    print("[-] examine ")
    print("[-] stat ")
    print("[-] loot ")
    print("[-] boss-fight ")
    print("[-] fight ")
    print("[-] save ")
    print("[-] main menu ")
    print("[-] quit ")
    print("+========================+")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'boss-fight', 'fight', 'examine', 'interact', 'look', 'stat','loot', 'save','main menu','quit']
    while action.lower() not in acceptable_actions:
        print("Tu veux faire quoi la ? c'est pas possible. \n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() == 'save':
        os.system('cls')
        with open ('savefile', 'wb') as f:
            pickle.dump(myPlayer, f)
            print('\nLa partie a été sauvegardé\n')
        action = input(">")
        viewstat()
    elif action.lower() == 'loot':
        viewloot()
    elif action.lower() == 'main menu':
        title_screen()
    elif action.lower() == 'stat':
        os.system('cls')
        viewstat()
    elif action.lower() in ['move', 'go']:
        player_move()
    elif action.lower( ) in ['examine', 'interact', 'look']:
        print_location()
        prompt()
    elif action.lower() in ['fight']:
        if myPlayer.location == 'Désert Montagneux' :
            combat()
        else:
            print("> Cet endroit n'est pas appropié pour level up... <")
            print("> Rends toi au Désert Montagneux pour level up      <")
            input('>')
            os.system('cls')
            prompt()
    elif action.lower() in ['boss-fight']:
        if myPlayer.location == wamuuuuuu.location :
            bossfight()
        elif myPlayer.location == Laddepascal.location:
            boss2fight()
        elif myPlayer.location == Aizen.location:
            boss3fight()
        elif myPlayer.location == Enma.location:
            boss4fight()
        elif myPlayer.location == Doflamingo.location:
            boss5fight()
        elif myPlayer.location == Kaido.location:
            boss6fight()
        else :
            print("Aucun Boss n'est présent ici heureusement pour toi tu peux vivre encore longtemps")
            prompt()
        


def player_move():
    ask = "Ou veux tu aller ? \n"
    destination = input(ask)
    if destination.lower() == 'go north' :
        destination = zone_map[myPlayer.location][UP]
        movement_handler(destination)
    elif destination.lower() == 'go west':
        destination = zone_map[myPlayer.location][LEFT]
        movement_handler(destination)
    elif destination.lower() ==  'go east':
        destination = zone_map[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif destination.lower() ==  'go south':
        destination = zone_map[myPlayer.location][DOWN]
        movement_handler(destination)
    else:
        print("Commande invalide, utilise go north, go south, go west, ou go east pour te déplacer.\n")
        player_move()

        
def movement_handler(destination):
    print("\nTu t'es deplacé en " + destination + ".")
    myPlayer.location = destination
    print_location()
    spawnchance = random.randint(0,10)
    if spawnchance > 3:
        combat()
    else :
        prompt()

def viewstat():
    # MaD = magic damage
    print("+------------------------+")
    print("+      Name :", myPlayer.name,"      +")
    print("+ |     Lvl :", myPlayer.lvl,"       | +")
    print("+ |     Exp :", myPlayer.xp,  "/", myPlayer.xpbarre,   "  | +")
    print("+------------------------+")
    print("+         Stats          +")
    print("+------------------------+")
    print("+ |     HP :", myPlayer.hp,"      | +")
    print("+ |    Atk :", myPlayer.atk,"       | +")
    print("+ |    Def :", myPlayer.df,"        | +")
    print("+ |    Mad :", myPlayer.md,"        | +")
    print("+ |   Mana :", myPlayer.mp,"       | +")
    print("+ |   Souls :", myPlayer.souls,"       | +")
    print("+ |____________________| +")
    print("+------------------------+")
    print("+    Class :", myPlayer.job,"    +")
    print("+------------------------+")
    input(">")
    prompt()

def viewloot():
    print("+------------------------+")
    print("+      Name :", myPlayer.name,"      +")
    print("+------------------------+")
    print("+          Loot          +")
    print("+------------------------+")
    print(myPlayer.loot)
    print("+ |                    | +")
    print("+ |                    | +")
    print("+ |                    | +")
    print("+ |                    | +")
    print("+ |                    | +")
    print("+ |____________________| +")
    print("+------------------------+")
    print("+    Class :", myPlayer.job,"    +")
    print("+------------------------+")
    input(">")
    prompt()
########Game Functionnality#######
def wongame():
    print("bravo a toi, tu as recup toute les souls\n")
    print("je pensais pas que tu pourrais le faire bravo")
    title_screen()

def start_game():
    return
       
def main_game_loop():
    while myPlayer.souls < 6 :
        prompt()
    else:
        wongame()
    # si le boss est vaincu
def game_over():
    os.system('cls')
    fin = ("Je t'avais dis de faire attention.... maintenant tu es mort...")
    for character in fin:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    title_screen()

def setup_game():
    os.system('cls')
    question1 = "Salut, comment t'appelles tu ? "
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myPlayer.name = player_name

##### Job  ########
    question2 = "Tu pense être quoi ?\n"
    question2added = "(tu peux être un warrior, un mage ou un priest)"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    valid_jobs = ['warrior', 'mage', 'priest']
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ['warrior']
    if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print("Tu vas maintenant être réincarné en un " + myPlayer.job + " t'as fais le bon choix ;)!\n")
        
    else:
            print('malheureusement je peux que te réincarner en warrior dsl :)')
            player_job = input('> ')
            if player_job.lower() in valid_jobs:
                myPlayer.job = player_job
                print("Tu vas maintenant être réincarner en un " + player_job + '!\n')


    question3 = "Bienvenue, " + player_name + " le " + player_job + ".\n"
    for character in question3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.05)
    

    speech1 = "Bienvenue dans ce monde de merde\n"
    speech2 = "Tu vas en baver\n"
    speech3 = "Fais gaffe a pas te perdre...\n"
    speech4 = "hihihihihihihihihihiihihih!!!\n"
    for character in speech1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
    for character in speech2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
    for character in speech3:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.01)
    for character in speech4:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(0.03)
    os.system('cls')
    print("+----------------+")
    print("+ ET C'EST PARTI +")
    print("+----------------+")
    main_game_loop()




#####Enemy########


def enemyspawn():
    enemyList = [gobelin,slime,troll,superslime,macichien,skelleton,gobelin,gobelin,slime,slime,slime,superslime]
    chance = random.randint(0,11)
    enemy = enemyList[chance]
    return enemy
    


######## lvl ########
def exp():
    xpgagné = random.randint(1,10)
    print('tu as gagné ',xpgagné,'xp')
    myPlayer.xp = myPlayer.xp + xpgagné
    if myPlayer.xp >= myPlayer.xpbarre:
        print('tu as gagné un lvl')
        myPlayer.lvl = myPlayer.lvl + 1
        myPlayer.xp = 0
        myPlayer.xpbarre = myPlayer.xpbarre * 2
        myPlayer.atk = myPlayer.atk + 5
        myPlayer.df = myPlayer.df + 2
        myPlayer.hp = myPlayer.hp + 10
        print("On dirait que tes stats on augmentées")
    else : print("Ta barre d'experience est a ",myPlayer.xp,'/',myPlayer.xpbarre)

###### battle state ######
def combat(): 
    enemy = enemyspawn()
    print("\nUn", enemy.name,"est apparu!")
    print("Tu dois faire un choix:",myPlayer.job)
    while enemy.hp > 0:
        choice = input("\n1. Attaque physique \n2. Attaque magique \n3. fuite\n")

        if choice == "1":
            print ("tu t'élances pour attaquer le", enemy.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                enemy.hp = enemy.hp - (myPlayer.atk - enemy.df)
                print ("Tu as touché l'ennemi il lui reste : ", enemy.hp, "hp\n")
            else:
                 print("T'es vraiment nul même ça t'y arrives pas, du coup tu te relève ?\n")

            
            if enemy.hp > 0:
                    hitchance = random.randint(0,10)
                    if enemy.md <= 0 :
                        if hitchance > 3:
                            myPlayer.hp = myPlayer.hp - (enemy.atk - myPlayer.df)
                            print ("Attention le", enemy.name, "fonce tout droit sur toi..., et punaise il t'a touché il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("Tout aussi nul que toi il t'a raté\n")
                    else :
                        if hitchance > 1:
                            myPlayer.hp = myPlayer.hp - enemy.md 
                            print ("Attention le", enemy.name, "fonce tout droit sur toi..., et punaise il t'a touché il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("Tout aussi nul que toi il t'a raté\n")

            else:
                    print ("Bravo tu a désintégré le", enemy.name)
                    print ("Il a drop un truc là !")
                    exp()
                    lootDrop = loot()
                    print ("Tu as reçu une", lootDrop,"\n")
                    lootEffect(lootDrop, myPlayer)
                    prompt()

        elif choice == "2":
            myPlayer.mp = myPlayer.mp - 1
            if myPlayer.mp > 0 :
                
                print ("Tu lance une incantation: System Call Genereate All Elements...")
                hitchance = random.randint(0,10)
                if hitchance > 3:
                    enemy.hp = enemy.hp - myPlayer.md
                    
                    print ("Discharge.. Whaou il ne lui reste que", enemy.hp, "hp")

                    if enemy.hp > 0:
                        hitchance = random.randint(0,10)
                        if hitchance > 7:
                            print ("Le", enemy.name, "te recopie je crois pas sûr")
                            myPlayer.hp = myPlayer.hp - enemy.atk 
                            print ("Le", enemy.name, "ta vraiment recopié, il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()

                        else:
                            print("Vous êtes pas frère pas hasard à raté tout le temps comme ça\n")
                    
                    else:
                        print ("Bravo tu a désintégré le", enemy.name)
                        print ("Il a drop un truc là !")
                        lootDrop = loot()
                        print ("Tu as reçu une", lootDrop,'\n')
                        lootEffect(lootDrop, myPlayer)
                        prompt()
                else:
                    print("Tout ça... pour ça! Tu ne l'a même pas touché\n")
                    if enemy.hp > 0:
                        print ("Le", enemy.name, "rigole pas par contre oulah...")
                        hitchance = random.randint(0,10)
                        if hitchance > 7:
                            myPlayer.hp = myPlayer.hp - (enemy.atk / myPlayer.df)                
                            print ("Le", enemy.name, "veut vraiment en découdre il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("C'est une blague il est tout aussi nul que toi\n")      
                            
            else : 
                print("T'a dépensé tout ton mana comme un bourrin tu n'a plus rien")
                if enemy.hp > 0:
                    print ("Le", enemy.name, "lui il en a encore par contre serre les fesses ça va faire mal")
                    hitchance = random.randint(0,10)
                    if hitchance > 7:
                        myPlayer.hp = myPlayer.hp - (enemy.atk / myPlayer.df) 
                        print ("Le", enemy.name, "t'a refait le portrait, il te reste", myPlayer.hp, "hp")
                        if myPlayer.hp < 1 :
                            game_over()
                    else:
                        print("Ah non c'est bon il a raté...")


        elif choice == "3":
            print("OH OH OH OH qu'est que tu nous fait là me dit que tu t'enfuis !!!!")
            runchance = random.randint(1,10)
            if runchance > 4:
                print ("T'es vraiment qu'une poule mouillée")
                prompt()
            else:
                print ("CHEHHH ça t'apprendre la prochaine fois essaye ou moins quelque chose")
                print ("Il a l'air d'être du même avis que mois ça va faire mal....")
                myPlayer.hp = myPlayer.hp - (enemy.atk / myPlayer.df) 
                print ("Pas autant que ça enfaite regarde il te reste que", myPlayer.hp, "hp")




def bossfight():
    print("\n", wamuuuuuu.name,"est apparu!")
    print("Tu dois faire un choix:",myPlayer.job)
    while wamuuuuuu.hp > 0:
        choice = input("\n1. Attaque physique \n2. Attaque magique \n3. fuite\n")

        if choice == "1":
            print ("Qu'est que tu nous prépare là...")
            hitchance = random.randint(0,10)
            if hitchance > 3:
                wamuuuuuu.hp = wamuuuuuu.hp - (myPlayer.atk - wamuuuuuu.df)
                print ("Tu l'a vraiment touché j'en reviens pas mais il reste encore : ", wamuuuuuu.hp, "hp\n")
            else:
                 print("C'est pas comme ça que tu vas gagné \n")

            
            if wamuuuuuu.hp > 0:
                    hitchance = random.randint(0,10)
                    if wamuuuuuu.md <= 0 :
                        if hitchance > 3:
                            myPlayer.hp = myPlayer.hp - (wamuuuuuu.atk - myPlayer.df)
                            print ("Attention", wamuuuuuu.name, "fonce tout droit sur toi...,AAAHHHHHHHH....hp restant :", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("Très bien esquivé\n")
                    else :
                        if hitchance > 1:
                            myPlayer.hp = myPlayer.hp - wamuuuuuu.md 
                            print (wamuuuuuu.name, " se prépare... touché il te reste que:", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("Si t'a pas de la chance je me demande ce que c'est\n")

            else:
                print ("Bravo par pur chance tu as réussi à vaincre", wamuuuuuu.name)
                print ("Son loot n'est pas comme les autres!")
                lootDrop = loot()
                # lootDropbossweaponwamuu()
                myPlayer.souls = myPlayer.souls + 1
                print ("Tu as reçu une", lootDrop,'\n')
                lootEffect(lootDrop, myPlayer)
                if myPlayer.souls == 6:
                    wongame()
                else:
                    prompt()

        elif choice == "2":
            myPlayer.mp = myPlayer.mp - 1
            if myPlayer.mp > 0 :
                
                print ("Tu lance une incantation: System Call Genereate All Elements...")
                hitchance = random.randint(0,10)
                if hitchance > 3:
                    wamuuuuuu.hp = wamuuuuuu.hp - myPlayer.md
                    
                    print ("Discharge.. Whaou il ne lui reste que", wamuuuuuu.hp, "hp")

                    if wamuuuuuu.hp > 0:
                        hitchance = random.randint(0,10)
                        if hitchance > 7:
                            print ( wamuuuuuu.name, "sort un sabre...")
                            myPlayer.hp = myPlayer.hp - wamuuuuuu.atk 
                            print ("Oh regarde au dessus y'a une météorite qui tombe.....hp restant:", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()

                        else:
                            print("Ah non c'est bon fausse alerte\n")
                    
                    else:
                        print ("Bravo par pur chance tu as réussi à vaincre", wamuuuuuu.name)
                        print ("Son loot n'est pas comme les autres!")
                        lootDrop = loot()
                        # lootDropbossweaponwamuu()
                        myPlayer.souls = myPlayer.souls + 1
                        print ("Tu as reçu une", lootDrop,'\n')
                        lootEffect(lootDrop, myPlayer)
                        if myPlayer.souls == 6:
                            wongame()
                        else:
                            prompt()
                else:
                    print("Tout ça... pour ça! Tu ne l'a même pas touché\n")
                    if wamuuuuuu.hp > 0:
                        print (wamuuuuuu.name, "rigole pas par contre oulah...")
                        hitchance = random.randint(0,10)
                        if hitchance > 7:
                            myPlayer.hp = myPlayer.hp - wamuuuuuu.atk 
                            print ("Il veut vraiment en finir avec toi il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("Nice move!\n")      
                            
            else : 
                print("Tu n'a même assez pour lancé une attaque aussi nul")
                if wamuuuuuu.hp > 0:
                    print (wamuuuuuu.name, "lui il en a encore par contre serre les fesses ça va faire mal")
                    hitchance = random.randint(0,10)
                    if hitchance > 7:
                        myPlayer.hp = myPlayer.hp - wamuuuuuu.atk 
                        print ("Il t'a refait le portrait, il ne te reste", myPlayer.hp, "hp")
                        if myPlayer.hp < 1 :
                            game_over()
                    else:
                        print("Ah non c'est bon R.A.S")


        elif choice == "3":
            print("Au moi tu es honnête avec toi même...fuiiiiiiiisss")
            runchance = random.randint(1,10)
            if runchance > 4:
                print ("On en a vraiment eu de la chance!")
                prompt()
            else:
                print ("Bon je pense que tu vas passé un mauvais quart d'heure")
                print ("Il a l'air d'être du même avis que moi ça va faire mal....")
                myPlayer.hp = myPlayer.hp - wamuuuuuu.atk
                print ("Allez on repart de plus belle il te reste encore", myPlayer.hp, "hp")

##### Boss 2 ####

def boss2fight():
    print("\n", Laddepascal.name,"est apparu!")
    print("Tu dois faire un choix:",myPlayer.job)
    while Laddepascal.hp > 0:
        choice = input("\n1. Attaque physique \n2. Attaque magique \n3. fuite\n")

        if choice == "1":
            print ("tu t'élances pour attaquer ", Laddepascal.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                Laddepascal.hp = Laddepascal.hp - (myPlayer.atk - Laddepascal.df)
                print ("Tu as touché l'ennemi il lui reste : ", Laddepascal.hp, "hp\n")
            else:
                 print("T'es vraiment nul même ça t'y arrives pas, du coup tu te relève ?\n")

            
            if Laddepascal.hp > 0:
                    hitchance = random.randint(0,10)
                    if Laddepascal.md <= 0 :
                        if hitchance > 3:
                            myPlayer.hp = myPlayer.hp - (Laddepascal.atk - myPlayer.df)
                            print ("Attention ", Laddepascal.name, "fonce tout droit sur toi..., et punaise il t'a touché il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("Il est passé quelque part je le vois plus...\n")
                    else :
                        if hitchance > 1:
                            myPlayer.hp = myPlayer.hp - Laddepascal.md 
                            print ("Attention", Laddepascal.name, "fonce tout droit sur toi..., et punaise il t'a touché il te reste", Laddepascal.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("Je crois qu'il est parti tu peux essayer de fuir\n")

            else:
                    print ("Tu commances à devenir fort... non c'est faut")
                    print ("Il a drop un truc là !")
                    lootDrop = loot()
                    ###lootDropbossweaponwamuu()
                    myPlayer.souls = myPlayer.souls + 1
                    print ("Tu as reçu une", lootDrop,'\n')
                    lootEffect(lootDrop, myPlayer)
                    if myPlayer.souls == 6:
                        wongame()
                    else:
                        prompt()

        elif choice == "2":
            myPlayer.mp = myPlayer.mp - 1
            if myPlayer.mp > 0 :
                print ("Qu'est que tu nous fait avec tes mains...")
                hitchance = random.randint(0,10)
                if hitchance > 3:
                    Laddepascal.hp = Laddepascal.hp - myPlayer.md
                    
                    print ("Oh non j'y crois pas le RASENGANNNNN, ses hp sont de :", Laddepascal.hp, "hp")

                    if Laddepascal.hp > 0:
                        hitchance = random.randint(0,10)
                        if hitchance > 7:
                            print (Laddepascal.name, "te recopie je crois pas sûr")
                            myPlayer.hp = myPlayer.hp - Laddepascal.atk 
                            print ("Le", Laddepascal.name, "ta vraiment recopié, il te reste", Laddepascal.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()

                        else:
                            print("Un vrai trouillard lui aussi\n")
                    
                    else:
                        print ("Tu peux ajouter", Laddepascal.name,"dans ta liste")
                        print ("Il a drop un truc là !")
                        lootDrop = loot()
                        ###lootDropbossweaponwamuu()
                        myPlayer.souls = myPlayer.souls + 1
                        print ("Tu as reçu une", lootDrop,'\n')
                        lootEffect(lootDrop, myPlayer)
                        if myPlayer.souls == 6:
                            wongame()
                        else:
                            prompt()
                else:
                    print("Tout ça... pour ça! Tu ne l'as même pas touché\n")
                    if Laddepascal.hp > 0:
                        print (Laddepascal.name, "rigole pas par contre oulah...")
                        hitchance = random.randint(0,10)
                        if hitchance > 7:
                            myPlayer.hp = myPlayer.hp - (Laddepascal.atk - myPlayer.df) 
                            print (Laddepascal.name, "veut vraiment en découdre il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("C'est une blague il est tout aussi nul que toi...ou peut être pas\n")      
                            
            else : 
                print("T'a dépensé tout ton mana comme un bourrin tu n'a plus rien")
                if Laddepascal.hp > 0:
                    print (" Lui il en a encore par contre serre les fesses ça va faire mal")
                    hitchance = random.randint(0,10)
                    if hitchance > 7:
                        myPlayer.hp = myPlayer.hp - (Laddepascal.atk - myPlayer.df)
                        print (Laddepascal.name, "ta refait le portrait, il te reste", myPlayer.hp, "hp")
                        if myPlayer.hp < 1 :
                            game_over()
                    else:
                        print("Ah non c'est bon il a raté...")


        elif choice == "3":
            print("Tu te fou de ma gueule...descend descend!!!!")
            runchance = random.randint(1,10)
            if runchance > 4:
                print ("Donc un arbre peut te faire éviter un boss pas mal à croire qu'il est aussi bête que toi")
                prompt()
            else:
                print ("En t'accrochant à un arbre tu as cru qu'il ne te verrait pas")
                myPlayer.hp = myPlayer.hp - 2
                print("Bah bravo en plus tu tombes de l'arbre il te reste", myPlayer.hp, "hp")
                myPlayer.hp = myPlayer.hp - Laddepascal.atk
                print ("Et lui il en rajoute hop il te reste plus que", myPlayer.hp, "hp")

def boss3fight():
    print("\nEUUUUHHHH,c'est moi ou c'est", Aizen.name,"qui vient d'atterir devant toi")
    print("Tu dois faire un choix:",myPlayer.job)
    while Aizen.hp > 0:
        choice = input("\n1. Attaque physique \n2. Bankai \n3. fuite\n")

        if choice == "1":
            print ("Tu le sors d'ou le zanpakuto, nan me dit pas que...", Aizen.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                Aizen.hp = Aizen.hp - (myPlayer.atk - Aizen.df)
                print ("Getsuga Tensho>>>>>>>>> oh la vache il lui reste :", Aizen.hp, "hp\n")
            else:
                 print("Donc la t'essaye de faire quoi face à lui...\n")

            
            if Aizen.hp > 0:
                    hitchance = random.randint(0,10)
                    if Aizen.md <= 0 :
                        if hitchance > 3:
                            myPlayer.hp = myPlayer.hp - (Aizen.atk - myPlayer.df)
                            print (Aizen.name, "ne semble pas bouché...mais pourquoi tu saignes alors...hp restant:", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("Je l'ai connu plus fort""\n")
                    else :
                        if hitchance > 1:
                            myPlayer.hp = myPlayer.hp - Aizen.md 
                            print ("Mais pourquoi tu as planté le katana dessus...non c'est son pouvoir qui fait ça...pv restant:", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("Il doit avoit pitié de toi\n")

            else:
                    print ("Tu n'a même pas utilisé le bankai pour le tué bravo")
                    print ("Il a drop un truc là !")
                    lootDrop = loot()
                    ##myPlayer.loot.append('Sword')
                    myPlayer.souls = myPlayer.souls + 1
                    print ("Tu as reçu une", lootDrop,'\n')
                    lootEffect(lootDrop, myPlayer)
                    if myPlayer.souls == 6:
                        wongame()
                    else:
                        prompt()

        elif choice == "2":
            myPlayer.mp = myPlayer.mp - 1
            if myPlayer.mp > 0 :
                print ("<<<< BANKAI >>>>")
                hitchance = random.randint(0,10)
                if hitchance > 1:
                    # myPlayer.md = myPlayer.md + 80
                    Aizen.hp = Aizen.hp - myPlayer.md
                    print ("Le vrai gestuga tensho je ne l'ai vu qu'en animé quelle force tu as il lui reste encore:", Aizen.hp, "hp")

                    if Aizen.hp > 0:
                        hitchance = random.randint(0,10)
                        if hitchance > 5:
                            print (Aizen.name, "sort le katana de son fourreau...")
                            myPlayer.hp = myPlayer.hp - (Aizen.atk - myPlayer.df) 
                            print ( Aizen.name, "il ne rigole plus trop la il te reste:", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()

                        else:
                            print("Il doit avoir pitié de toi\n")
                    
                    else:
                        print (Aizen.name,"a été battu par un seul homme tu es le deuxième")
                        print ("Il a drop un truc là !")
                        lootDrop = loot()
                        # myPlayer.loot.append('sword')
                        myPlayer.souls = myPlayer.souls + 1
                        print ("Tu as reçu une", lootDrop,'\n')
                        # lootEffect(lootDrop, myPlayer)
                        if myPlayer.souls == 6:
                            wongame()
                        else:
                            prompt()
                else:
                    print("Tout ça... pour ça! Tu ne l'a même pas touché\n")
                    if wamuuuuuu.hp > 0:
                        print (Aizen.name, "rigole pas par contre oulah...")
                        hitchance = random.randint(0,10)
                        if hitchance > 7:
                            myPlayer.hp = myPlayer.hp - (Aizen.atk - myPlayer.df) 
                            print (Aizen.name, "veut vraiment en découdre il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("Ah non c'est bon il doit être occupé ....\n")      
                            
            else : 
                print("T'as dépensé tout ton mana comme un bourrin tu n'a plus rien")
                if Aizen.hp > 0:
                    print ("Lui il en a encore par contre serre les fesses ça va faire mal")
                    hitchance = random.randint(0,10)
                    if hitchance > 7:
                        myPlayer.hp = myPlayer.hp - (Aizen.atk - myPlayer.df) 
                        print (Aizen.name, "t'a refait le portrait, il te reste", myPlayer.hp, "hp")
                        if myPlayer.hp < 1 :
                            game_over()
                    else:
                        print("Ah non c'est bon il a raté...")


        elif choice == "3":
            print("OH OH OH OH qu'est que tu nous fait là me dit que tu t'enfuis !!!!")
            runchance = random.randint(1,10)
            if runchance > 4:
                print ("T'es vraiment qu'une poule mouilée")
                prompt()
            else:
                print ("CHEHHH ça t'apprendre la prochaine fois essaye ou moins quelque chose")
                print ("Il a l'air d'être du même avis que mois ça va faire mal....")
                myPlayer.hp = myPlayer.hp - Aizen.atk
                print ("Pas autant que ça enfaite regarde il te reste que", myPlayer.hp, "hp")

def boss4fight():
    print("\n", Enma.name,"est apparu!")
    print("Tu dois faire un choix:",myPlayer.job)
    while Enma.hp > 0:
        choice = input("\n1. Attaque physique \n2. Attaque magique \n3. fuite\n")

        if choice == "1":
            print ("tu t'élances pour attaquer ", Enma.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                Enma.hp = Enma.hp - (myPlayer.atk - Enma.df)
                print ("Tu l'as touché il lui reste : ", Enma.hp, "hp\n")
            else:
                 print("T'es vraiment nul même ça t'y arrives pas, du coup tu te relève ?\n")

            
            if Enma.hp > 0:
                    hitchance = random.randint(0,10)
                    if Enma.md <= 0 :
                        if hitchance > 3:
                            myPlayer.hp = myPlayer.hp - (Enma.atk - myPlayer.df)
                            print ("Attention", Enma.name, "fonce tout droit sur toi..., et punaise il t'a touché il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("nice move!!\n")
                    else :
                        if hitchance > 1:
                            myPlayer.hp = myPlayer.hp - Enma.md 
                            print ("Attention ", Enma.name, "fonce tout droit sur toi..., et punaise il t'a touché il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("T'as réussi à l'esquivé\n")

            else:
                    print ("Bravo tu a battu comme un vrai samuraï c'est faux")
                    print ("Il a drop un truc là !")
                    lootDrop = loot()
                    ###lootDropbossweaponwamuu()
                    myPlayer.souls = myPlayer.souls + 1
                    print ("Tu as reçu une", lootDrop,'\n')
                    lootEffect(lootDrop, myPlayer)
                    if myPlayer.souls == 6:
                        wongame()
                    else:
                        prompt()

        elif choice == "2":
            myPlayer.mp = myPlayer.mp - 1
            if myPlayer.mp > 0 :
                
                print ("Tu lances une incantation: System Call Genereate Fire Element...")
                hitchance = random.randint(0,10)
                if hitchance > 3:
                    Enma.hp = Enma.hp - myPlayer.md
                    
                    print ("Discharge.. Whaou il ne lui reste que", Enma.hp, "hp")

                    if Enma.hp > 0:
                        hitchance = random.randint(0,10)
                        if hitchance > 7:
                            print ( Enma.name, "te recopie je crois pas sûr")
                            myPlayer.hp = myPlayer.hp - (Enma.atk - myPlayer.df)
                            print (Enma.name, "ta vraiment recopié, il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()

                        else:
                            print("T'as réussi à parer son coup\n")
                    
                    else:
                        print ("Bravo tu a battu", Enma.name)
                        print ("Il a drop un truc là !")
                        lootDrop = loot()
                        ###lootDropbossweaponwamuu()
                        myPlayer.souls = myPlayer.souls + 1
                        print ("Tu as reçu une", lootDrop,'\n')
                        lootEffect(lootDrop, myPlayer)
                        if myPlayer.souls == 6:
                            wongame()
                        else:
                            prompt()
                else:
                    print("Tout ça... pour ça! Tu ne l'as même pas touché\n")
                    if Enma.hp > 0:
                        print (Enma.name, "rigole pas par contre oulah...")
                        hitchance = random.randint(0,10)
                        if hitchance > 7:
                            myPlayer.hp = myPlayer.hp - (Enma.atk - myPlayer.df)
                            print (Enma.name, "veut vraiment en découdre il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("Bien equivé\n")      
                            
            else : 
                print("T'as dépensé tout ton mana comme un bourrin tu n'a plus rien")
                if Enma.hp > 0:
                    print (Enma.name, "lui il en a encore par contre serre les fesses ça va faire mal")
                    hitchance = random.randint(0,10)
                    if hitchance > 7:
                        myPlayer.hp = myPlayer.hp - (Enma.atk - myPlayer.df)
                        print (Enma.name, "t'a refait le portrait, il te reste", myPlayer.hp, "hp")
                        if myPlayer.hp < 1 :
                            game_over()
                    else:
                        print("Ah non c'est bon il a raté...")


        elif choice == "3":
            print("OH OH OH OH qu'est que tu nous fait là me dit que tu t'enfuis !!!!")
            runchance = random.randint(1,10)
            if runchance > 4:
                print ("T'es vraiment qu'une poule mouilée")
                prompt()
            else:
                print ("CHEHHH ça t'apprendre la prochaine fois essaye ou moins quelque chose")
                print ("Il a l'air d'être du même avis que mois ça va faire mal....")
                myPlayer.hp = myPlayer.hp - Enma.atk
                print ("Pas autant que ça enfaite regarde il te reste que", myPlayer.hp, "hp")

def boss5fight():
    print("\n", Doflamingo.name,"est apparu du ciel!")
    print("Tu dois faire un choix:",myPlayer.job)
    while Doflamingo.hp > 0:
        choice = input("\n1. Attaque physique \n2. Attaque magique \n3. fuite\n")

        if choice == "1":
            print ("tu t'élances pour attaquer", Doflamingo.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                Doflamingo.hp = Doflamingo.hp - (myPlayer.atk - Doflamingo.df)
                print ("Tu as touché l'ennemi il lui reste : ", Doflamingo.hp, "hp\n")
            else:
                 print("T'es vraiment nul même ça t'y arrives pas, du coup tu te relève ?\n")

            
            if Doflamingo.hp > 0:
                    hitchance = random.randint(0,10)
                    if Doflamingo.md <= 0 :
                        if hitchance > 3:
                            myPlayer.hp = myPlayer.hp - (Doflamingo.atk - myPlayer.df)
                            print ("Attention", Doflamingo.name, "fonce tout droit sur toi..., et punaise il t'a touché il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("Tout aussi nul que toi il t'a raté\n")
                    else :
                        if hitchance > 1:
                            myPlayer.hp = myPlayer.hp - Doflamingo.md 
                            print ("Attention", Doflamingo.name, "fonce tout droit sur toi..., et punaise il t'a touché il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("Tout aussi nul que toi il t'a raté\n")

            else:
                    print ("Bravo tu a battu", Doflamingo.name)
                    print ("Il a drop un truc là !")
                    lootDrop = loot()
                    ###lootDropbossweaponwamuu()
                    myPlayer.souls = myPlayer.souls + 1
                    print ("Tu as reçu une", lootDrop,'\n')
                    lootEffect(lootDrop, myPlayer)
                    if myPlayer.souls == 6:
                        wongame()
                    else:
                        prompt()

        elif choice == "2":
            myPlayer.mp = myPlayer.mp - 1
            if myPlayer.mp > 0 :
                
                print ("Tu lance une incantation: System Call Genereate All Elements...")
                hitchance = random.randint(0,10)
                if hitchance > 3:
                    Doflamingo.hp = Doflamingo.hp - myPlayer.md
                    
                    print ("Discharge.. Whaou il ne lui reste que", Doflamingo.hp, "hp")

                    if Doflamingo.hp > 0:
                        hitchance = random.randint(0,10)
                        if hitchance > 7:
                            print (Doflamingo.name, "te recopie je crois pas sûr")
                            myPlayer.hp = myPlayer.hp - (Doflamingo.atk - myPlayer.df)
                            print (Doflamingo.name, "ta vraiment recopié, il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()

                        else:
                            print("Vous êtes pas frère pas hasard à raté tout le temps comme ça\n")
                    
                    else:
                        print ("Bravo tu a désintégré", Doflamingo.name)
                        print ("Il a drop un truc là !")
                        lootDrop = loot()
                        ###lootDropbossweaponwamuu()
                        myPlayer.souls = myPlayer.souls + 1
                        print ("Tu as reçu une", lootDrop,'\n')
                        lootEffect(lootDrop, myPlayer)
                        if myPlayer.souls == 6:
                            wongame()
                        else:
                            prompt()
                else:
                    print("Tout ça... pour ça! Tu ne l'a même pas touché\n")
                    if Doflamingo.hp > 0:
                        print (Doflamingo.name, "rigole pas par contre oulah...")
                        hitchance = random.randint(0,10)
                        if hitchance > 7:
                            myPlayer.hp = myPlayer.hp - (Doflamingo.atk - myPlayer.df) 
                            print (Doflamingo.name, "veut vraiment en découdre il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("C'est une blague il est tout aussi nul que toi\n")      
                            
            else : 
                print("T'a dépensé tout ton mana comme un bourrin tu n'a plus rien")
                if Doflamingo.hp > 0:
                    print (Doflamingo.name, "lui il en a encore par contre serre les fesses ça va faire mal")
                    hitchance = random.randint(0,10)
                    if hitchance > 7:
                        myPlayer.hp = myPlayer.hp - (Doflamingo.atk - myPlayer.df) 
                        print (Doflamingo.name, "t'a refait le portrait, il te reste", myPlayer.hp, "hp")
                        if myPlayer.hp < 1 :
                            game_over()
                    else:
                        print("Ah non c'est bon il a raté...")


        elif choice == "3":
            print("OH OH OH OH qu'est que tu nous fait là me dit que tu t'enfuis !!!!")
            runchance = random.randint(1,10)
            if runchance > 4:
                print ("T'es vraiment qu'une poule mouilée")
                prompt()
            else:
                print ("CHEHHH ça t'apprendre la prochaine fois essaye ou moins quelque chose")
                print ("Il a l'air d'être du même avis que mois ça va faire mal....")
                myPlayer.hp = myPlayer.hp - Doflamingo.atk
                print ("Pas autant que ça enfaite regarde il te reste que", myPlayer.hp, "hp")

def boss6fight():
    print("\n",Kaido.name,"est apparu!")
    print("Tu dois faire un choix:",myPlayer.job)
    while Kaido.hp > 0:
        choice = input("\n1. Attaque physique \n2. Attaque magique \n3. fuite\n")

        if choice == "1":
            print ("tu t'élances pour attaquer ", Kaido.name)
            hitchance = random.randint(0,10)
            if hitchance > 3:
                Kaido.hp = Kaido.hp - (myPlayer.atk - Kaido.df)
                print ("Tu as touché l'ennemi il lui reste : ", Kaido.hp, "hp\n")
            else:
                 print("T'es vraiment nul même ça t'y arrives pas, du coup tu te relève ?\n")

            
            if Kaido.hp > 0:
                    hitchance = random.randint(0,10)
                    if Kaido.md <= 0 :
                        if hitchance > 3:
                            myPlayer.hp = myPlayer.hp - (Kaido.atk - myPlayer.df)
                            print ("Attention", Kaido.name, "fonce tout droit sur toi..., et punaise il t'a touché il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("Tout aussi nul que toi il t'a raté\n")
                    else :
                        if hitchance > 1:
                            myPlayer.hp = myPlayer.hp - Kaido.md 
                            print ("Attention", Kaido.name, "fonce tout droit sur toi..., et punaise il t'a touché il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("Tout aussi nul que toi il t'a raté\n")

            else:
                    print ("Bravo tu a désintégré ", Kaido.name)
                    print ("Il a drop un truc là !")
                    lootDrop = loot()
                    ###lootDropbossweaponwamuu()
                    myPlayer.souls = myPlayer.souls + 1
                    print ("Tu as reçu une", lootDrop,'\n')
                    lootEffect(lootDrop, myPlayer)
                    if myPlayer.souls == 6:
                        wongame()
                    else:
                        prompt()

        elif choice == "2":
            myPlayer.mp = myPlayer.mp - 1
            if myPlayer.mp > 0 :
                
                print ("Tu lance une incantation: System Call Genereate All Elements...")
                hitchance = random.randint(0,10)
                if hitchance > 3:
                    Kaido.hp = Kaido.hp - myPlayer.md
                    
                    print ("Discharge.. Whaou il ne lui reste que", Kaido.hp, "hp")

                    if Kaido.hp > 0:
                        hitchance = random.randint(0,10)
                        if hitchance > 7:
                            print (Kaido.name, "te recopie je crois pas sûr")
                            myPlayer.hp = myPlayer.hp - (Kaido.atk - myPlayer.df) 
                            print (Kaido.name, "ta vraiment recopié, il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()

                        else:
                            print("Vous êtes pas frère pas hasard à raté tout le temps comme ça\n")
                    
                    else:
                        print ("Il a drop un truc là !")
                        lootDrop = loot()
                        ###lootDropbossweaponwamuu()
                        myPlayer.souls = myPlayer.souls + 1
                        print ("Tu as reçu une", lootDrop,'\n')
                        lootEffect(lootDrop, myPlayer)
                        if myPlayer.souls == 6:
                            wongame()
                        else:
                            prompt()
                else:
                    print("Tout ça... pour ça! Tu ne l'a même pas touché\n")
                    if Kaido.hp > 0:
                        print (Kaido.name, "rigole pas par contre oulah...")
                        hitchance = random.randint(0,10)
                        if hitchance > 7:
                            myPlayer.hp = myPlayer.hp - (Kaido.atk - myPlayer.df) 
                            print (Kaido.name, "veut vraiment en découdre il te reste", myPlayer.hp, "hp")
                            if myPlayer.hp < 1 :
                                game_over()
                        else:
                            print("C'est une blague il est tout aussi nul que toi\n")      
                            
            else : 
                print("T'a dépensé tout ton mana comme un bourrin tu n'a plus rien")
                if Kaido.hp > 0:
                    print (Kaido.name, "lui il en a encore par contre serre les fesses ça va faire mal")
                    hitchance = random.randint(0,10)
                    if hitchance > 7:
                        myPlayer.hp = myPlayer.hp - Kaido.atk 
                        print (Kaido.name, "t'a refait le portrait, il te reste", myPlayer.hp, "hp")
                        if myPlayer.hp < 1 :
                            game_over()
                    else:
                        print("Ah non c'est bon il a raté...")


        elif choice == "3":
            print("Face à lui tu ne peux rien faire donc fuiiiis")
            runchance = random.randint(1,10)
            if runchance > 4:
                print ("T'es vraiment qu'une poule mouilée")
                prompt()
            else:
                print ("CHEHHH ça t'apprendre la prochaine fois essaye ou moins quelque chose")
                print ("Il a l'air d'être du même avis que mois ça va faire mal....")
                myPlayer.hp = myPlayer.hp - Kaido.atk
                print ("Pas autant que ça enfaite regarde il te reste que", myPlayer.hp, "hp")
title_screen()






