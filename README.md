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

## Installation

1. **Clonez le dépôt :**

   ```bash
   git clone https://github.com/username/repository.git
   cd repository


2. **Créez un environnement virtuel (optionnel mais recommandé) :**
  ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows utilisez `venv\Scripts\activate`

3. **Installez les dépendances :**
     ```bash
   pip install -r requirements.txt
    
4. **Configurez les variables d’environnement :**
Assurez-vous de définir les variables d’environnement nécessaires, telles que le token du bot Discord. 
Vous pouvez utiliser un fichier .env pour cela. Exemple de fichier .env :
  ```bash
   DISCORD_TOKEN= your_discord_bot_token

5. **Démarrez le bot :**
 ```bash
   python bot.py

