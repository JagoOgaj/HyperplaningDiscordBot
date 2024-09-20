# Discord Bot

## Description

Ce projet est un bot Discord utilisant `discord.py` pour la gestion des commandes et `selenium` pour l'automatisation de tâches sur le web.

## Fonctionnalités

- Commande `!test` : Vérifie si le bot fonctionne correctement.
- Commande `!getSchedule` : Exécute une tâche avec Selenium et envoie une capture d'écran.

## Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre machine :
- Python 3.12
- Un environnement virtuel Python (optionnel mais recommandé)
- Le navigateur Firefox et le geckodriver correspondant

## Installation et configuration

1. **Clonez le dépôt :**

   ```bash
   git clone https://github.com/username/repository.git
   cd repository
   ```


2. **Créez un environnement virtuel (optionnel mais recommandé) :**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows utilisez `venv\Scripts\activate`
   ```

3. **Installez les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```
    
4. **Configurez les variables d’environnement :**
Assurez-vous de définir les variables d’environnement nécessaires, en créant à la racine le fichier "envVar.py" contenant 7 variable
   ```python
   EXECUTABLE_PATH: str = 
   URL_HYPERPLANNING: str = 
   ELEMENT_TO_FOCUS: str =
   INPUT: str = 
   BOT_TOKEN: str = 
   OUTPUT: str = 
   CHANNEL_ID: int = 
   ```

## Lancer le programe

Une fois l'instalation et la configuration terminé pour lancer le bot avec un `python main.py`

## Architecture 
```bash
├── DriverService                    # Contient la logique pour gérer le service du driver
│   └── driverService.py             # Fichier principal pour le service de driver
├── bot                              # Module pour la gestion du bot Discord
│   └── botDiscord.py                # Logique principale pour interagir avec Discord
├── cogs                             # Contient les cogs pour le bot Discord
│   ├── alarmCog.py                  # Cog pour gérer les alarmes
│   └── scheduleCog.py               # Cog pour gérer les horaires
├── constants                        # Contient des constantes utilisées dans le projet
│   └── constantsDate.py             # Fichier pour les constantes liées aux dates
├── envVar.py                        # Fichier contenant les variables d'environnement
├── error                            # Module pour la gestion des erreurs personnalisées
│   └── exceptionsCustom.py          # Définitions d'exceptions personnalisées
├── exec                             # Contient des exécutables ou des binaires nécessaires
│   └── geckodriver                  # Driver pour contrôler le navigateur via Selenium
├── main.py                          # Point d'entrée principal de l'application
├── requirements.txt                 # Liste des dépendances du projet
├── README.md                        # Documentation du projet
└── utils                            # Contient des utilitaires et des fonctions d'aide
    ├── service.py                   # Fonctions utilitaires pour divers services
    └── tools.py                     # Outils divers pour le projet
```
## Licence

Ce projet est un projet open source réalisé par un Samy OKI, élève de 3ème informatique dans le cadre de son BUT en Informatique.