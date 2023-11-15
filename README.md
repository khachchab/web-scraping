Web Scraping Scripts
Description
Ce référentiel contient deux scripts Python qui effectuent le web scraping de deux sites différents et extraient des informations spécifiques. Les scripts utilisent BeautifulSoup pour analyser le HTML des pages web et Requests pour récupérer le contenu.

Script 1: Web Scraping d'un site d'actualités

Ce script extrait les titres, les descriptions et les dates de publication des actualités d'un site web (exemple: Le Matin - https://lematin.ma/).

Les données sont ensuite stockées dans un DataFrame Pandas et sauvegardées dans un fichier CSV (web_scraping.csv).

De plus, le script génère un graphique pour visualiser la distribution des heures de publication.

Script 2: Web Scraping de la liste des plus grandes entreprises aux États-Unis

Ce script extrait les données de la page Wikipédia sur la Liste des plus grandes entreprises aux États-Unis par revenu.

Les données sont organisées dans un DataFrame Pandas et sauvegardées dans un fichier CSV (web_scraping_companies.csv).

Ce script est destiné à collecter des informations sur les plus grandes entreprises aux États-Unis.

Comment utiliser
Prérequis
Assurez-vous d'installer les bibliothèques nécessaires en exécutant la commande suivante :

bash
Copy code
pip install beautifulsoup4 requests pandas matplotlib
Exécution des scripts
Script 1: Web Scraping d'un site d'actualités

Exécutez le script web_scraping_news.py:

bash
Copy code
python web_scraping_news.py
Le script extraira les données du site d'actualités, créera un fichier CSV et affichera un graphique de distribution des heures de publication.

Script 2: Web Scraping de la liste des plus grandes entreprises aux États-Unis

Exécutez le script web_scraping_companies.py:

bash
Copy code
python web_scraping_companies.py
Le script extraira les données de la page Wikipédia, créera un fichier CSV et le sauvegardera.

