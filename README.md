# Discord Bot

## Description

Ce projet est un bot Discord utilisant `discord.py` pour la gestion des commandes et `selenium` pour l'automatisation de tâches sur le web.

## Fonctionnalités

- Commande `!test` : Vérifie si le bot fonctionne correctement.
- Commande `!getSchedule` : Exécute une tâche avec Selenium et envoie une capture d'écran.

## Prérequis

Assurez-vous d'avoir les éléments suivants installés sur votre machine :
- Python 3.8 ou supérieur
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
├── DriverService
│   ├── __pycache__
│   │   ├── driver.cpython-312.pyc
│   │   └── driverService.cpython-312.pyc
│   └── driverService.py
├── bot
│   ├── __pycache__
│   │   └── botDiscord.cpython-312.pyc
│   └── botDiscord.py
├── cogs
│   ├── __pycache__
│   │   ├── alarmCog.cpython-312.pyc
│   │   ├── cogsCommands.cpython-312.pyc
│   │   └── scheduleCog.cpython-312.pyc
│   ├── alarmCog.py
│   └── scheduleCog.py
├── constants
│   ├── __pycache__
│   │   └── constantsDate.cpython-312.pyc
│   └── constantsDate.py
├── envVar.py
├── error
│   ├── __pycache__
│   │   └── exceptionsCustom.cpython-312.pyc
│   └── exceptionsCustom.py
├── exec
│   └── geckodriver
├── main.py
├── requirements.txt 
├── README.md
└── utils
    ├── __pycache__
    │   ├── service.cpython-312.pyc
    │   └── tools.cpython-312.pyc
    ├── service.py
    └── tools.py

