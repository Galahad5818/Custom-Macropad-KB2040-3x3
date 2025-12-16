# Custom-Macropad-KB2040-3x3
![IMG_20251214_225748V2](https://github.com/user-attachments/assets/79548706-77de-43b8-ac35-a215ec06e960)
Macropad personnalisé avec 9 touches, encodeur rotatif cliquable et bouton power dédié. Boîtier imprimé en 3D, carte électronique maison et firmware CircuitPython.

## Custom Macropad – KB2040 (CircuitPython)<br>
Ce projet est un macropad entièrement personnalisé, conçu et réalisé de A à Z :

- Design mécanique (impression 3D)
- Carte électronique maison
- Firmware en CircuitPython
- Configuration logicielle modulaire avec plusieurs maps

Premier projet personnel, réalisé sur environ 3 mois, avec pour objectif d’apprendre l’électronique, la conception 3D et le développement embarqué.

## PCB / Carte éléctronique + 3D de la carte<br>
Les fichiers pour la carte électronique et les fichiers 3D des PCB se trouve dans le dossier "Carte électronique".
Vous-y trouverai deux versions : 
- Gerber_EsayEDA Switch upside down
Cette version est ma première itération de carte électronique. Elle est 100 % fonctionnel pour ma part, je l'ai testé et c'est celle de mon macropad actuel. Elle a un léger défaut : les switchs de clavier, on été placé dans la mauvaise orientation (ils ont été tournés de 180°, mais cela ne gêne en rien son fonctionnement.)  
- Gerber_EsayEDA Switch good not tested
Cette deuxième version corrige l'erreur du premier marcopad, les switchs sont dans le bon sens. Toutefois, je n'ai pas testé cette nouvelle version en vrai. Sur le papier et d'après le logiciel tout est bon.

## Fonctionnalités
- Encodeur rotatif cliquable
  - Rotation : volume système + ou -
  - Clic : lecture / pause des fichiers audio, vidéo Youtube, ...
- Bouton Power dédié
  - Arrêt immédiat du PC
- Clavier matriciel 3×3 (8 touches programmable par map)
  -  2 maps configurables (voir plus si vous shouaiter en ajouter)
    - Changement de map via la touche 0 (haut a gauche)
    - La LED RGB intégrée a l'ESP indique la map active
      - (exmple : couleur bleu --> map 1 = 8 touches configurable, chanement de map avec touche 0, couleur rouge --> map 2 = 8 nouvelle touche configurable ...)

###  Gestion des maps
Tout ses maps sont entièrement configurable et c'est à vous de les adapter à vos besoins. <br>
Pour ma part j'ai construit les maps de la manière suivante : 
Map 1 (LED rouge)
- Déverrouillage du PC
- Écriture de chiffre
- Lancement d’applications (Exemple avec Discord, Youtube via le navigateur, Spotify)
- Veille prolonger de l'ordinateur.
- Verrouillage (Win + L)

Map 2 (LED bleue)
- Écriture de chiffre

Le changement de map se fait via la touche 0 (première touche en haut à gauche).

## Architecture logicielle
<code>code.py</code><br>
Gère :
Lecture des entrées (touches, encodeur, bouton power)
Le changement de map
Volume et media control
Appels aux actions

<code>maps.py</code><br>
Contient :
Les actions de chaque touche et de chaque map
- Les commandes système (via Win + R)
- Les macros clavier
- Les fonctions globales (verrouillage, overture d'application, etc.)


## Matériel utilisé
**Vous trouverez une section dédiée au matériel utilisé dans le dossier "Composent"**<br>
Microcontrôleur : KB2040<br>
Firmware : [CircuitPython pour KB2040](https://circuitpython.org/board/adafruit_kb2040/)<br>
PCB custom<br>
Boîtier imprimé en 3D

## 📸 Photos
![IMG_20251214_225748V2](https://github.com/user-attachments/assets/b91737a8-a96f-4391-8eea-442f346fa38b)
<img width="2559" height="1372" alt="EsayEDA Switch upside down2" src="https://github.com/user-attachments/assets/773cb989-1b69-44d5-a925-a56af4a77c45" />
![IMG_20251214_225913](https://github.com/user-attachments/assets/07436db6-6bd8-4548-8c6b-be316a7dbcf5)


##  Installation
- Installer [CircuitPython sur la carte KB2040](https://circuitpython.org/board/adafruit_kb2040/)<br>
- Copier les fichiers du dossier firmware/ sur la carte CIRCUITPY <br>
- Adapter les chemins Windows et les actions que vous shouaiter effectuer dans <code>maps.py</code><br>

## Defaut et possible amélioration
> [!WARNING]
> Defaut et possible amélioration
>- La première carte à les switch a l'envert : <code>Solution</code> J'ai fait une autre version avec les switch dans le bon sens<br>
>- La bague de sérage du bouton power est trop grosse et elle frote les pins de sont propre connecteur à l'arrière, et le boitier en impression 3D. Cela m'a conduit à retirer le connecteur initalement prévue, et ne pas mettre la bague de sérage : <code>Solution</code>
>J'ai retirer la bague le bouton tien de lui meme, un peux de colle chaude peux etre ajouter au besoin.
>![defaut (2)](https://github.com/user-attachments/assets/d927f98a-2d5a-4556-8c26-e93173217da6) <br>
>- Le PCB n'est pas assez épaise ou n'a pas asser de chouche : Il est un peux trop transparant. Par conséquent, le rétroéclairage des partie transpante du PCB (4 ligne diagonale, devant chaque ligne de touches) faisait une sorte de halo lumineux dans cette zone au lieux de ne passer qu'au travert des partie transparente : <code>Solution</code>
>J'ai donc du ajouter une structure suplémentaire dans le boitier afin de cloisoner la lumère


## Notes importantes
> [!IMPORTANT]
>Les chemins d’applications Windows sont à adapter. <br>
> Le projet utilise une disposition clavier Windows FR <br>
> Le macropad agit comme un clavier USB, aucune application PC n’est nécessaire

## Licence
Projet open-source – libre d’utilisation et de modification. Non commercialisable (pas d'utilisation ou de copie à des fin payante)
