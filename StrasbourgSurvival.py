import random
import time

def intro():
    print("Bienvenue dans Strasbourg Survival, " + nom_du_joueur.upper() + " !")
    time.sleep(1)
    print("Tu es un survivant dans un Strasbourg post-apocalyptique infesté de zombies, ton but sera de t'enfuir de la ville, pour esperer une meilleure vie.")
    time.sleep(2)
    print("Pour cela, tu devras explorer différents lieux de la ville, tout en y survivant.")
    time.sleep(3)
    print("Tu as un couteau suisse, une conserve, et une seule idée :")
    print("QUITTER CETTE VILLE.")

# STATS 
nom_du_joueur = input("Entre ton nom de citoyen : ")

# intro
intro()
print("\nClique sur Entrée...")
input() 


sante_actuelle = 100
niveau_de_faim = 150
est_en_vie = 1
nombre_de_zombies_tues = 0

# inv
nombre_de_chairs = 0
nombre_de_conserves = 1
mon_sac_a_dos = ["Couteau suisse"]
mes_artefacts = [""]

# equipement de base
arme_equipee = "Couteau suisse"
degats_arme = 10 

armure_equipee = "Vetements civils"
points_de_protection = 0
bonus_casque_permanent = 0

# la ou on est dans nos quetes
medecin_satisfait = False
policier_secouru = False
boss_final_vaincu = False
boulanger_satisfait = False
survivants_kathedrale_secourus = False


# artefact system
artefact_bidule_actif = False
artefact_bidule_consumed = False

# compteur de présence
est_allé_a_auchan = 0



# LES OUTILS

def clean_terminal():    
    print("\n" * 50)

def afficher_le_statut_complet():
    print("-------------------------------------------------------")
    print(" SURVIVANT : " + nom_du_joueur.upper())
    print(" SANTÉ     : " + str(sante_actuelle) + " / 100")  
    print(" SATIETÉ   : " + str(niveau_de_faim) + " / 150")
    print("-------------------------------------------------------")
    print(" ARME      : " + arme_equipee)
    print(" ARMURE    : " + armure_equipee)
    print("-------------------------------------------------------")
    print(" SAC       : " + str(nombre_de_chairs) + " chairs / " + str(nombre_de_conserves) + " conserves")
    print("-------------------------------------------------------")




# LES COMBATS

def lancer_un_combat(nom_du_monstre, pv_du_monstre, force_du_monstre, est_un_boss, attaques_speciales=[]):
    global sante_actuelle, est_en_vie, nombre_de_chairs, nombre_de_conserves, nombre_de_zombies_tues


    
    print("\n")
    print(" ATTENTION, TU TE FAIS ATTAQUER!!!")
    print("Tu affrontes : " + nom_du_monstre)
    time.sleep(1)

    while pv_du_monstre > 0 and sante_actuelle > 0:
        print("\nROUND")
        print(nom_du_monstre + " : " + str(pv_du_monstre) + " PV")
        print("Vous : " + str(sante_actuelle) + " PV")
        print("1. Attaquer")
        print("2. Fuir")
        
        choix_joueur = input("Ta décision : ")

        if choix_joueur == "1":
            degats_infliges = random.randint(8, 15) + degats_arme
            pv_du_monstre = pv_du_monstre - degats_infliges
            print("Tu combats, le méchant monstre particulièrement hideux perd " + str(degats_infliges) + " PV.")
        
        elif choix_joueur == "2":
            if est_un_boss == True:
                print("Impossible de fuir un BOSS ! Peureux va !")
            else:
                if random.randint(1, 10) <= 7:
                    print("T'as pris tes jambes à ton cou !")
                else:
                    print("Oups, tu trébuches en fuyant, le zombie te griffe le dos !")
                    degats_fuite = 10 + force_du_monstre
                    sante_actuelle = sante_actuelle - degats_fuite
                    print("Tu prends " + str(degats_fuite) + " dégats suite à ta tentative de fuite...")
                return "fuite"


        # attaques du monstre
        if pv_du_monstre > 0:
            time.sleep(1)

            if est_un_boss == True:
                print("LE TITAN TE CRACHE SA BAVE RADIOACTIVE !")
                degats_bruts = 30  

            elif len(attaques_speciales) > 0:
                attaque_choisie = random.choice(attaques_speciales)
                nom_attaque = attaque_choisie[0]
                degats_bruts = attaque_choisie[1]
                print("ATTAQUE : " + nom_attaque + " !")

            else:
                # zombie de base
                print("Le zombie te griffe avec ses ongles pourris")
                degats_bruts = random.randint(15, 28) + force_du_monstre 

            # réduction des dégats si on a une armure
            degats_reels = degats_bruts - points_de_protection
            if degats_reels < 2:
                degats_reels = 2
            
            sante_actuelle = sante_actuelle - degats_reels
            print("Tu prends " + str(degats_reels) + " dégats !")

    if sante_actuelle <= 0:
        est_en_vie = est_en_vie - 1
        print("\nTu as péri contre " + nom_du_monstre + ", quelle honte...")
        return "mort"
    else:
        print("\nVICTOIRE ! Tu as vaincu " + nom_du_monstre + ", ça c'est digne de quelqu'un comme toi !")
        
        if est_un_boss == False:
            print("Tu gagnes 2 morceaux de chair.")
            nombre_de_chairs = nombre_de_chairs + 2
            nombre_de_zombies_tues = nombre_de_zombies_tues + 1

            chance_nourriture = random.randint(1, 3)
            if chance_nourriture == 1:
                print("CHANCEUX ! Le monstre avait de la nourriture dans ses poches : tu gagnes une conserve !")
                nombre_de_conserves = nombre_de_conserves + 1
        
        input("Appuis sur Entrée pour continuer...")
        return "victoire"




# BOUCLE DU JEU

while est_en_vie >= 1:
    clean_terminal()
    afficher_le_statut_complet()

    print("--- MENU PRINCIPAL ---")
    print("1. Explorer un lieu")
    print("2. Ouvrir le sac à dos (Equiper ou Manger)")
    print("3. Se reposer (+50 PV, -15 Faim)")
    print("4. Quitter la partie")

    choix_menu = input("\nQue veux tu faire ? ")

    if choix_menu == "1":
        clean_terminal()
        print("--- CARTE DE STRASBOURG ---")
        print("1. La Pharmacie (Cherchons un Docteur)")
        print("2. Le Poste de Police (Il y a peut etre encore quelqu'un ??)")
        print("3. Homme de fer (Surement infesté de zombies)")
        print("4. Auchan de Hautepierre (ça doit etre tout autant garni en zombies qu'en matériel...) ")
        print("5. La Boulangerie  (l'odeur de croissant attire... tout le monde(je suppose??))")
        print("6. La Cathédrale (quelqu'un a allumé une lumière là haut...)")

        # ajout du dépot de tram si quetes finies
        if medecin_satisfait == True and policier_secouru == True and boulanger_satisfait == True:
            print("7. Le Dépot de Trams (on trouvera peut etre comment partir d'ici...)")

        lieu = input("\nOù veux tu aller ? ")




        # pharmacie
        if lieu == "1":
            if medecin_satisfait == False:
                print("\nDr.ELOPHE : 'J'ai besoin de 5 morceaux de chair pour tester des remèdes'")
                print("Vous en avez : " + str(nombre_de_chairs) + " / 5")
                
                if nombre_de_chairs >= 5:
                    donner = input("Veux tu donner des morceaux de chair ? (oui/non) : ")
                    if donner == "oui":
                        nombre_de_chairs = nombre_de_chairs - 5
                        mon_sac_a_dos.append("Tenue de médecin")
                        medecin_satisfait = True
                        print("Dr.ELOPHE : 'Merci ! Prends cette Tenue de médecin.'")
                input("\nAppui sur Entrée...")
            else:
                print("\nLe lieu est vide, des traces de combats sont présentes..."); input("...")




        # police
        elif lieu == "2":
            if policier_secouru == False:
                print("\nTu viens de rentrer dans le poste, tu entends des bruits de pas provenant de la salle de garde...")
                time.sleep(1)
                resultat_combat = lancer_un_combat("Zombie de Garde", 55, 20, False)  
                
                if resultat_combat == "victoire":
                    print("\nUn officier caché derrière un bureau vous appelle.")
                    print("Officier : 'OHHHH MERCI MERCI MERCI! Prends mon Fusil d'assaut, j'en ai d'autres pour moi.'")
                    mon_sac_a_dos.append("Fusil d'assaut")
                    policier_secouru = True
                input("\nAppui sur Entrée...")
            else:
                print("\nTu rentres dans le poste.")
                lancer_un_combat("Zombie Errant", 40, 22, False)  




        # HDF
        elif lieu == "3":
            print("\nTu chasses les zombies entassés sur la place")
            lancer_un_combat("Zombie errants de HDF", 45, 15, False)  




        # AUCHAN
        elif lieu == "4":
            print("\nTu rentres dans le Auchan, l'odeur de javel mélangée au sang est... spéciale.")
            print("1. Aller discrètement vers le rayon nourriture")
            print("2. Ça hurle au rayon ménager... S'y diriger.")
            print("3. Tu vas fairetesbesoins aux toilettes (les conserves ont travaillé ton estomac)")
            choix_auchan = input("\nTon choix : ")
            
            if choix_auchan == "1":
                est_allé_a_auchan = est_allé_a_auchan + 1
                print("\nTu rampes entre les rayons (peureux va !)")
                print("Miracle ! Tu trouves une conserve de nourriture pour chien.")
                if est_allé_a_auchan >= 3:
                    if random.randint(1, 2) == 1:
                        print("Le rayon est vide...")
                    else: nombre_de_conserves = nombre_de_conserves + 1
                else:
                    nombre_de_conserves = nombre_de_conserves + 2
                    print("Tu gagnes +2 nourriture (Conserve de chien).")
            
            elif choix_auchan == "2":
                print("\nTu cours vers le fond du magasin.")
                print("Une femme de ménage zombifiée te saute dessus en hurlant, elle a un aspirateur dans les mains...")   
                 
                #boss de la zone
                attaques_menagere = [
                    ("Elle te frappe avec le tuyau d'aspirateur", 24),
                    ("Elle te balance un seau d'eau de Javel dans les parties !", 32),
                    ("Elle t'aspire le lob d'oreille avec son Dyson", 28),
                    ("Elle t'asperge d'eau usagée de WC dans les yeux, tu vois flou", 38),
                ]
                          
                resultat_combat = lancer_un_combat("La Folle Ménagère", 100, 0, False, attaques_menagere)  
                
                if resultat_combat == "victoire":
                    print("\nEn fouillant ses entrailles, tu récupères son Aspirateur.")
                    mon_sac_a_dos.append("Aspirateur")

            elif choix_auchan == "3":
                print("\nTu te rends aux toilettes, des defecations surplombent les cabines, c'est un chouia ragoutant.")
                time.sleep(1)
                print("Hyn, mais quoi??")
                print('Tu vois quelquechose briller dans une des cuvettes...')
                choix_toilettes = input("\nVeux tu fouiller la cuvette ? Tu te dis qu'il y a peut etre des risques... (oui/non) : ")
                if choix_toilettes == "oui":
                    print("\nTu plonges ta main dans la cuvette, tu ressens une texture étrange...")
                    print("Urghhh, l'odeur est infame, et ça a l'air moisi :(  ")
                    print("Tu as subit 35pts de dégats...")
                    sante_actuelle = sante_actuelle - 40
                    choix_toilettes_2 = input("\nContinuer à fouiller??? (oui/non) : ")
                    if choix_toilettes_2 == "oui":
                        print("Oh, on dirait une sorte de bidule doré pas fifou...")
                        time.sleep(3)
                        print("ARTEFACT TROUVE : Le bidule doré pas fifou mais qui est boosté enft")
                        mes_artefacts.append("Bidule doré boosté")

            input("\nAppuie sur Entrée pour sortir du magasin.")





        # boulangerie
        elif lieu == "5":
            clean_terminal()
            print("\nTu pousses la porte de la boulangerie.")
            print("L'odeur de croissant moisis flotte dans l'air.")
            print("Un vieil homme barricadé derrière le comptoir te fait signe.")
            time.sleep(1)

            if boulanger_satisfait == False:
                print("\nRomexel (le boulanger) : 'Mon fils est bloqué par des zombies dans la réserve...'")
                print("Romexel : 'Occupe toi de ses ordures et je te file ma Veste en Kevlar qu'un client a oubliée ici.'")
                print("\nTu entends des cris venir de la réserve.")
                time.sleep(1)

                print("\nChoix :")
                print("1. Aller nettoyer la réserve")
                print("2. Partir, c'est pas mes oignons (je suis un horrible personnage)")
                choix_boulangerie = input("\nTon choix : ")

                if choix_boulangerie == "1":
                    print("\nTu ouvres la porte de la réserve... IL Y EN A DEUX.")

                    # zombies de zone
                    attaques_boulanger = [
                        ("Il te lance un sac de farine de 50kg en pleine tete", 24),
                        ("Il te griffe les lèvres et laisse de la levure dans la plaie (qui va vouloir t'embrasser maintenant?)", 18),
                        ("Il utilise une baguettes rassie comme une matraque", 22),
                        ("Il te crache de la pate crue directement dans les yeux", 28),
                    ]

                    resultat1 = lancer_un_combat("Zombie Boulanger", 85, 0, False, attaques_boulanger)

                    if resultat1 == "victoire" or resultat1 == "fuite":
                        if resultat1 == "fuite":
                            print("\nOups, t'as fui mais l'autre est encore là...")

                        # zombie de zone2
                        attaques_livreur = [
                            ("Il te roule dessus avec son vélo de livraison", 34),
                            ("Il te jette sa sacoche remplie de Tasty Crousty dans les côtes", 22),
                            ("Il essaie de te mordre le mollet en pédalant dans le vide", 12),
                            ("Il te balance sa pile de boîtes de pizza", 26),
                        ]

                        resultat2 = lancer_un_combat("Zombie Livreur", 75, 0, False, attaques_livreur)

                        if resultat2 == "victoire":
                            print("\nRomexel : 'MAGNIFIQUE ! Tu mérites un bisous, quoique...'")
                            print("Romexel te tend une Veste en Kevlar et une conserve appetissante.")
                            mon_sac_a_dos.append("Veste en Kevlar")
                            nombre_de_conserves = nombre_de_conserves + 1
                            boulanger_satisfait = True

                elif choix_boulangerie == "2":
                    print("\nRomexel te regarde partir avec un regard dépité, tu le vois saupoudrer de la cyanure sur son croissant du matin...")

            else:
                print("\nRomexel : 'MERCI. Tiens, un croissant.'")
                print("(Il te tend quelque chose de suspect qui ressemble vaguement à un croissant)")

            input("\nAppuis sur Entrée pour sortir de la boulangerie...")




        # cathédrale
        elif lieu == "6":
            clean_terminal()
            print("\nTu arrives devant la Cathédrale de Strasbourg.")
            print("Une lumière clignote tout en haut de la flèche.")
            print("Des voix viennent de l'intérieur...")
            time.sleep(2)

            print("\n1. Entrer par le portail principal")
            print("2. Passer par la porte secondaire")
            choix_entree = input("\nTon choix : ")

            survivants_ok = False

            if choix_entree == "1":
                print("\nTu entre avec classe par la grande porte, c'est INFESTÉ de zombies")
                print("Un ZOMBIE PRÉDICATEUR se retourne.")
                print("'NOUVEEEEAU PAAASTEUUUUR' il hurle ça en sautant sur toi")
                time.sleep(1)

                # boss de zone
                attaques_predicateur = [
                    ("Il te frappe avec sa Bible", 28),
                    ("Il t'asperge d'eau bénite infectée", 24),
                    ("Il te plante avec sa croix", 40),
                    ("Il te mord le cou avec un appetit religieusement contestable", 33),
                    ("Il te balance le pupitre de l'orgue sur les pieds", 26),
                ]

                resultat_predicateur = lancer_un_combat("Le Zombie Prédicateur", 100, 0, False, attaques_predicateur)

                if resultat_predicateur == "victoire":
                    print("\nLes survivants cachés dans la crypte sortent et se mettent à te vénerer")
                    survivants_ok = True

            elif choix_entree == "2":
                clean_terminal()
                print("\nTu passe discreto par la porte secondaire")
                print("Tu aperçois 4 survivants barricadés à l'interieur")
                time.sleep(1)
                print("\nUne femme te montre du doigt un zombie Prédictateur")
                survivants_ok = False

                print("\n1. Aller affronter le Zombie Prédicateur")
                print("2. Partir sans les aider (oui, je suis un odieux personnage)")
                choix_cathedrale = input("\nTon choix : ")

                if choix_cathedrale == "1":
                    attaques_predicateur = [
                        ("Il te frappe avec sa Bible", 22),
                        ("Il t'asperge d'eau bénite infectée", 18),
                        ("Il te plante avec sa croix", 32),
                        ("Il te mord le cou avec un appetit religieusement contestable", 26),
                        ("Il te balance le pupitre de l'orgue sur les pieds", 20),
                    ]
                    resultat_predicateur = lancer_un_combat("Le Zombie Prédicateur", 100, 0, False, attaques_predicateur)

                    if resultat_predicateur == "victoire":
                        survivants_ok = True
                else:
                    print("\nTu repars. Les survivants te regardent partir. Tu ne te retournes pas")
                    survivants_ok = False

            # si tu aides tu gagnes bonus
            if survivants_ok == True and survivants_kathedrale_secourus == False:
                print("\nLes survivants te sertent la main.")
                print("Un d'eux te donne un casque")
                print("Une autre sort deux conserves ")
                mon_sac_a_dos.append("Casque de chantier")
                nombre_de_conserves = nombre_de_conserves + 3
                survivants_kathedrale_secourus = True
                print("\nYeayyy, 4 personnes de sauvées")

            elif survivants_kathedrale_secourus == True:
                print("\nLes survivants sont toujours la")
                print("Ils te saluent depuis les bancs. Les GOAT finalement")

            input("\nAppuis sur Entrée pour sortir de la Cathédrale...")




        elif lieu == "7" and medecin_satisfait and policier_secouru and boulanger_satisfait:
            clean_terminal()
            print("\nTu pousses la porte du dépot de Tram...")
            print("LE CONTROLEUR TITANESQUE se met à hurler, il porte encore son brassard CTS.")
            print("_______________________________________________________________________________________________________")
            print("_______________________________________________________________________________________________________")
            print("ATTENTION, NE PAS SPAM LA TOUCHE ENTREE LORS DU MINI JEU, RISQUE DE CRASH")
            print("_______________________________________________________________________________________________________")
            print("_______________________________________________________________________________________________________")
            time.sleep(2)

            pv_boss = 750
            if "Aspirateur" in mon_sac_a_dos:
                print("\nTu sors l'Aspirateur du Auchan !")
                print("Tu aspires une énorme partie de sa bave radioactive avant le début du combat.")
                pv_boss = 450 
                print(f"Le controlleur en perd ses contraventions. Ses PV chutent à {pv_boss}.")
                time.sleep(2)

            # bonus casque
            bonus_casque = bonus_casque_permanent
            if bonus_casque > 0:
                print("\nTon casque de chantier tank comme un boss")
                print(f"Tu as +{bonus_casque} points de protection contre le boss")
                time.sleep(1)
            


            while pv_boss > 0 and sante_actuelle > 0:
                print("\n" + "="*40)
                print(f" BOSS : LE TITAN CTS / PV : {pv_boss}")
                print(f" TOI  : {nom_du_joueur.upper()} / PV : {sante_actuelle}")
                print("="*40)
                
                print("1. Attaque habituelle")
                print("2. Tu vises sa Tête (quitte ou double)")
                print("3. Mini-jeu de précision")
                print("4. Tu tentes une esquive")
                
                if "Bidule doré boosté" in mes_artefacts and artefact_bidule_actif == False:
                    print("5. Frotter le Bidule doré boosté")
                
                choix = input("\nTon choix : ")
                esquive_active = False

                if choix == "1":
                    degats_base = random.randint(15, 20) + degats_arme
                    bonus_artefact = 0
                    pv_boss -= degats_base
                    print(f"Tu frappes le boss et lui infliges {degats_base} dégâts.")
                
                elif choix == "2":
                    chance = random.randint(1, 2)
                    if chance == 1:
                        degats_base = (random.randint(20, 30) + degats_arme) * 2
                        pv_boss -= degats_base
                        print(f"BAHHAHAHAHAH, dans son crane, il perd {degats_base} PV !")
                    else:
                        print("Oups, c'est pas fifou, il a bougé au dernier moment, tu tires dans le vide.")

                elif choix == "3":
                    print("Le compte à rebours commence, sois prêt à appuyer sur Entrée !")
                    for i in range(3, 0, -1):
                        print(i)
                        time.sleep(1)

                    print("GO !")
                    debut = time.time()
                    input("Appuie sur Entrée le plus vite possible : ")
                    fin = time.time()

                    temps_reaction = fin - debut

                    if temps_reaction < 0.40:
                        print(f"Wow ({temps_reaction:.2f}s)")
                        time.sleep(1)
                        print("Le boss subit 100 dgts.")
                        pv_boss -= 100
                    else:
                        print(f"T'es pas le plus rapide ({temps_reaction:.2f}s)")

                
                elif choix == "4":
                    print("Tu executes un superbe salto arrière pour esquiver la prochaine attaque.")
                    esquive_active = True
                    print("Le controlleur frappe un tram et se fait mal, il subit 50 dgts...")
                    pv_boss -= 50
                
                elif choix == "5" and "Bidule doré boosté" in mes_artefacts and artefact_bidule_actif == False:
                    print("\nTu sors le Bidule doré boosté...")
                    time.sleep(2)
                    print("Une aura subliminale sort de lui, tu lui chatoille se qui lui sert de nombril et...")
                    time.sleep(2)
                    print("Bah, il ajuste disparu ?")
                    artefact_bidule_actif = True
                    artefact_bidule_consumed = False
                    time.sleep(2)

                if pv_boss > 0:
                    time.sleep(1)

                    
                    type_attaque = random.randint(1, 4)  
                    
                    if type_attaque == 1:
                        nom_att = "Coup de pied dans les parties"
                        degats_bruts = 30 
                    elif type_attaque == 2:
                        nom_att = "Bave radioactive CTS"
                        degats_bruts = 40  
                    elif type_attaque == 3:
                        nom_att = "AMENDE DE 3EME CLASSE"
                        degats_bruts = 53
                    else:
                        nom_att = "Il te projette contre une rame de tram "
                        degats_bruts = 50

                    degats_reels = degats_bruts - points_de_protection - bonus_casque
                    if esquive_active:
                        print("YEAYYY ! Ton esquive fonctionne")
                        degats_reels = int(degats_reels * 0.2)
                    
                    if degats_reels < 0:
                        degats_reels = 0
                    sante_actuelle -= degats_reels
                    
                    print(f"\nATTAQUE DU BOSS : Le controlleur te lance : {nom_att} !")
                    print(f"Tu encaisses {degats_reels} dégâts !")
                    time.sleep(1)

            if pv_boss <= 0:
                print("\nLe Titan s'effondre dans ses propres contraventions.")
                boss_final_vaincu = True
                input("\nAppuie sur Entrée pour continuer...")
                break
            elif sante_actuelle <= 0:
                # si l'artefact est actif et pas encore consommé, il give 2eme vie
                if artefact_bidule_actif and not artefact_bidule_consumed:
                    artefact_bidule_consumed = True
                    artefact_bidule_actif = False
                    # retirer l'artefact de l'inventaire
                    if "Bidule doré boosté" in mes_artefacts:
                        try:
                            mes_artefacts.remove("Bidule doré boosté")
                        except ValueError:
                            pass
                    
                    sante_actuelle = 80
                    print("\nYEAY, JE ME SENS REVIVRE, SERAIT-CE CELA LA MAGIE DU BIDULE DORE??? ")
                    time.sleep(2)
                    continue
                else:
                    est_en_vie = est_en_vie - 1
                    print("\nLe Titan t'a écrasé sous le poids des contraventions... Vu les couts, tu n'y survis pas...")
                    time.sleep(2)
                    break

        else:
            print("\nLieu invalide ou dépôt de trams inaccessible pour l'instant.")
            time.sleep(1)

        niveau_de_faim = niveau_de_faim - 15




    # sac
    elif choix_menu == "2":
        clean_terminal()
        print("--- TON SAC À DOS ---")
        print("Arme portée : " + arme_equipee)
        print("Armure portée : " + armure_equipee)
        print("\nItems utilisables :")
        
        if "Fusil d'assaut" in mon_sac_a_dos:
            print("[1] Équiper le Fusil d'assaut")
            
        if "Tenue de médecin" in mon_sac_a_dos:
            print("[2] Équiper la Tenue de médecin (si je gagne pas de l'éloquence avec ça je capte pas)")
            
        if "Couteau suisse" in mon_sac_a_dos:
            print("[3] Équiper le Couteau suisse")
            
        if nombre_de_conserves > 0:
            print("[4] Manger une conserve (Stock : " + str(nombre_de_conserves) + ")")

        if "Veste en Kevlar" in mon_sac_a_dos:
            print("[5] Équiper la Veste en Kevlar (histoire d'etre BG)")

        if "Casque de chantier" in mon_sac_a_dos:
            print("[6] Équiper le Casque de chantier ")

        print("[0] Fermer le sac")
        
        choix_sac = input("\nTon choix : ")
        
        if choix_sac == "1" and "Fusil d'assaut" in mon_sac_a_dos:
            arme_equipee = "Fusil d'assaut"
            degats_arme = 35
            print("Fusil d'assaut équipé et chargé")
                
        elif choix_sac == "2" and "Tenue de médecin" in mon_sac_a_dos:
            armure_equipee = "Tenue de médecin"
            points_de_protection = 12
            print("Tenue de médecin enfilée sur ton corps d'athlète :)")
                
        elif choix_sac == "3" and "Couteau suisse" in mon_sac_a_dos:
            arme_equipee = "Couteau suisse"
            degats_arme = 10
            print("Tu as de nouveau ton couteau en main")
            
        elif choix_sac == "4" and nombre_de_conserves > 0:
            nombre_de_conserves = nombre_de_conserves - 1
            niveau_de_faim = niveau_de_faim + 35  
            if niveau_de_faim > 150:
                niveau_de_faim = 150
            print("Tu dégustes ta conserve d'anchois (sans trop de convictions), tu es revigoré")

        elif choix_sac == "5" and "Veste en Kevlar" in mon_sac_a_dos:
            armure_equipee = "Veste en Kevlar"
            points_de_protection = 13
            print("Tu enfiles la Veste en Kevlar. (tu deviens le plus beau des survivants)")

        elif choix_sac == "6" and "Casque de chantier" in mon_sac_a_dos:
            bonus_casque_permanent = 10
            print("Casque de chantier équipé ! Tu gagnes +10 points de protection permanents.")

        elif choix_sac != "0":
            print("Choix invalide.")

        time.sleep(2)





    elif choix_menu == "3":
        print("\nTu dors un peu... (et tu fais des cauchemars de zombies controleurs CTS)")
        sante_actuelle = sante_actuelle + 50
        if sante_actuelle > 100:
            sante_actuelle = 120
        niveau_de_faim = niveau_de_faim - 15
        time.sleep(2)

    elif choix_menu == "4":
        print("\nTu t'apprete à quitter, est tu sur de ton choix?")
        choix_quitter = input("Appuie sur Entrée pour confirmer, ou sur une autre touche pour annuler : ")
        if choix_quitter == "":
            est_en_vie = est_en_vie - 10

    else:
        print("\nChoix invalide, tape 1, 2, 3 ou 4.")
        time.sleep(1)


    if niveau_de_faim <= 70:
        print("\nTu es affamé")
        time.sleep(2)
        
    if niveau_de_faim <= 30:
        sante_actuelle -= 10
        print("\nTU POURRAIS PENSER A TON VENTRE UN PEU??? MANGE")  
        time.sleep(2)  
        
    if niveau_de_faim <= 0:
        print("\nTu es mort de faim... et t'avais des conserves dans le sac, p'tit malin.")
        time.sleep(3)
        est_en_vie = est_en_vie - 1




# FIN 
clean_terminal()
if boss_final_vaincu == True:
    print("GG ! " + nom_du_joueur.upper() + " tu as vaincu le controlleur vicieux de la CTS dans le Dépot de Tram !")
    print("Tu peux enfin partir si tu le souhaites.")
    time.sleep(10)
    print("\nSCORE FINAL :")
    print("Tu as tué " + str(nombre_de_zombies_tues + 1) + " zombies.")
    print("Quetes accomplies :")
    if medecin_satisfait:
        print("   Dr. Strauss est satisfait")
    if policier_secouru:
        print("  L'officier est secouru")
    if boulanger_satisfait:
        print("  Le fils du boulanger est secouru")
    if survivants_kathedrale_secourus:
        print("  Les survivants de la cathédrale sont secourus")
    print("Maintenant que tu as accès aux trams, tu décide d'en prendre un, et de partir vers l'allemagne...")
    time.sleep(10)
    print("----------------------------------------------------------")
    print("FIN DU CHAPITRE 1 : LA FUITE DE STRASBOURG")
    print("----------------------------------------------------------")
else:
    print("BOUHHHHH ! T'as perdu, c'était facile pourtant...")
    time.sleep(10)
