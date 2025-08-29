# Guide – Application pour l’affichage de cours boursiers

## Description
Cette application Streamlit permet à l’utilisateur de visualiser l’évolution historique d’une action et de créer un graphique interactif.  
L’utilisateur peut sélectionner l’action, la période historique et l’intervalle d’affichage des données.

---

## Dépendances
  * `streamlit` : pour créer l’interface web interactive.
  * `yfinance` : pour récupérer les données financières historiques des actions.
  * `plotly.express` : pour générer des graphiques interactifs.

1. Récupération du projet.
Ouvrir un terminal et cloner le dépôt avec la commande suivante :  
    ```bash
     git clone https://github.com/MyriamA6/stock-viewer
    ```

2. Installation des dépendances et lancement :

    ```bash
    pip install streamlit yfinance plotly
    streamlit run stock_market.py
    ```

3. Saisie de l’action

    Dans le formulaire affiché dans l’interface : `Nom de l'action`: entrer le symbole boursier de l’entreprise.
        
    **Exemples** :
        
        AAPL pour Apple (US)
        
        AIR.PA pour Airbus (Euronext Paris)
        
        BMW.DE pour BMW (Xetra)

4. Choix de la période historique. 

    Sélectionner la période sur laquelle vous souhaitez récupérer les données :

        1d – 1 jour
        
        5d – 5 jours
        
        1mo – 1 mois
        
        3mo – 3 mois

5. Choix de l’intervalle d’affichage.

    Définir la fréquence des points de données :

        1m – 1 minute (disponible pour les 7 derniers jours uniquement)
        
        15m – 15 minutes
        
        30m – 30 minutes
        
        60m – 1 heure

6. Affichage du graphique

   * Cliquer sur Afficher pour récupérer les données et générer le graphique.
   
   * Le graphique montre le prix de clôture (Close) de l’action sélectionnée.
   
   * Le fuseau horaire est converti à celui d'Europe/Paris.
   
   * Le graphique est interactif (zoom, déplacement, survol des données).


7. Points importants

    Les données à l’intervalle 1m ne sont disponibles que pour les 7 derniers jours.
    
    Si le symbole boursier est incorrect ou introuvable, aucune donnée ne sera affichée.
