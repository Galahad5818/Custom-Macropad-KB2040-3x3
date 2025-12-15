# Custom-Macropad-KB2040-3x3
Macropad personnalisé avec 9 touches, encodeur rotatif cliquable et bouton power dédié. Boîtier imprimé en 3D, carte électronique maison et firmware CircuitPython.
# Custom-Macropad-KB2040-3-3-Encodeur
Macropad personnalisé avec 9 touches, encodeur rotatif cliquable et bouton power dédié. Boîtier imprimé en 3D, carte électronique maison et firmware CircuitPython.

**🧩 Custom Macropad – KB2040 (CircuitPython)**<br>
Ce projet est un macropad entièrement personnalisé, conçu et réalisé de A à Z :

- Design mécanique (impression 3D)
- Carte électronique maison
- Firmware en CircuitPython
- Configuration logicielle modulaire avec plusieurs maps

👉 Premier projet personnel, réalisé sur environ 3 mois, avec pour objectif d’apprendre l’électronique, la conception 3D et le développement embarqué.

**✨ Fonctionnalités**
- Clavier matriciel 3×3 (9 touches)
- Encodeur rotatif cliquable
  - Rotation : volume système
  - Clic : lecture / pause
- Bouton Power dédié
  - Arrêt immédiat du PC
-  2 maps configurables
  - Changement de map via la touche 0
  - LED RGB intégrée pour indiquer la map active
- Émulation clavier USB (HID)
- Code modulaire (actions séparées du main)

**🧠 Architecture logicielle**<br>
<code>code.py</code><br>
Gère :
Lecture des entrées (touches, encodeur, bouton power)
Changement de map
Volume et media control
Appels aux actions

<code>maps.py</code><br>
Contient :
Les actions de chaque touche
Les commandes système (via Win + R)
Les macros clavier
Les fonctions globales (verrouillage, extinction, etc.)


**🎛 Gestion des maps**<br>
Map 1 (LED rouge)
- Déverrouillage du PC
- Lancement d’applications
- Contrôle multimédia
- Verrouillage / veille

Map 2 (LED bleue)
- Actions alternatives (exemple : saisie de codes)

Le changement de map se fait via la touche 0.

**🧪 Matériel utilisé**<br>

Microcontrôleur : KB2040
Firmware : CircuitPython
Encodeur rotatif avec bouton
LED NeoPixel intégrée
PCB custom
Boîtier imprimé en 3D

**📸 Photos**<br>
![IMG_20251214_225748V2](https://github.com/user-attachments/assets/79548706-77de-43b8-ac35-a215ec06e960)
<img width="2559" height="1372" alt="EsayEDA Switch upside down2" src="https://github.com/user-attachments/assets/773cb989-1b69-44d5-a925-a56af4a77c45" />


**🚀 Installation**<br>
Installer CircuitPython sur la KB2040
Copier les fichiers du dossier firmware/ sur la carte CIRCUITPY
Adapter les chemins Windows dans maps.py


**⚠️ Notes importantes:**<br>
Les chemins d’applications Windows sont à adapter
Le projet utilise une disposition clavier Windows FR
Le macropad agit comme un clavier USB, aucune application PC n’est nécessaire

**📜 Licence:**<br>
Projet open-source – libre d’utilisation et de modification. Non commercialisable (pas d'utilisation ou de copie à des fin payante)
