# Strasbourg Survival
## Description

Strasbourg Survival est un jeu d'aventure textuel en Python se déroulant dans un Strasbourg apocalyptique envahi de zombies. Vous incarnez un survivant qui doit explorer la ville, accomplir des quêtes et trouver un moyen pour s'échapper.



## Lancement

Prérequis : Python 3.8 ou (pas de biblihotèque autre necessairre).

```bash
python StrasbourgSurvival.py


## Fonctionnalités

- Système de combat au tour par tour avec différents choix (attaquer, fuir)
- 6 lieux explorables, chacun avec ses propres ennemis et événements
- 4 quêtes secondaires qui débloquent l'accès au boss final
- Système d'inventaire : armes, armures, nourriture, artefact 
- Gestion de la santé et de la faim du joueur
- Combat de boss avec mécaniques spéciales (esquive, mini-jeu de réaction, coup critique, artefact)
- Texte d'introduction et fin narrative selon le résultat



## Lieux explorables

| Lieu                  | Buts 
|                       |
| La Pharmacie          | Quête : donner 5 chairs au Dr. Élophe → obtenir une Tenue de médecin 
| Le Poste de Police    | Quête : tuer le zombie de garde → obtenir un Fusil d'assaut 
| Homme de Fer          | Combat libre contre des zombies errants 
| Auchan de Hautepierre | Nourriture, boss de zone (Folle Ménagère), artefact secret aux toilettes 
| La Boulangerie        | Quête : sauver le fils de Romexel pour obtenir une Veste en Kevlar 
| La Cathédrale         | Quête optionnelle : sauver des survivants pour obtenir un Casque de chantier 
| Dépôt de Trams        | Boss final qui n'est accessible uniquement après les 3 quêtes principales 




## Objets

**Armes**

| Objet             | DGT | Obtention 
|                   |     |
| Couteau suisse    | +10 | Départ 
| Fusil d'assaut    | +35 | Quête Police 

**Armures**

| Objet                   |Protection | Obtention 
|                         |           |   
| Vêtements civils        | 0         | Départ 
| Tenue de médecin        | 12        | Quête Pharmacie 
| Veste en Kevlar         | 13        | Quête Boulangerie 
| Casque de chantier      | +10       | Quête Cathédrale 

**Consommables**

| Objet           | Effet 
|                 |   
| Conserve        | +35 satiété  
| Chair de zombie | Monnaie d'échange pour la quête Pharmacie 

**Artefact**

Bidule doré boosté / Usage unique lors du boss : redonne 80 PV si le joueur tombe à 0 



## Mécaniques principales

**Santé et satiété**

La santé maximum est de 100 PV (on peut monter à 120 si on est très reposés). La satiété démarre à 150 et diminue à chaque exploration. En dessous de 70, le joueur est averti. En dessous de 30, il perd 10 PV par tour. À 0, il meurt de faim.

**Combat**

Chaque round, le joueur choisit d'attaquer ou de fuir. Les dégâts infligés sont aléatoires, augmentés par l'arme équipée. Les dégâts reçus sont réduits par l'armure équipée. Fuir est impossible contre les boss.

**Quêtes**

Trois quêtes sont obligatoires pour débloquer le dépôt de trams (médecin, policier, boulanger). La quête de la cathédrale est optionnelle mais donne le Casque de chantier, utile contre le boss final.



# Ayant déja présenté la béta du jeu à plusieurs éléves de la classe, j'ai eu bcp de remarques constructives qui m'ont permis d'améliorer le jeu, et suite à ça, beaucoup ont aimé et m'ont réclamé une suite ! Je pense donc sortir un chapitre 2 durant les vacances, à vous de me dire si cela vous interesse/ si vous avez des envies particulières pour la suite.
