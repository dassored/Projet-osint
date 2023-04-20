import requests

# Liste des mots-clés pour les Google Dorks
mots_cles = ['hacker','onsint','virus']

# Parcourir les mots-clés et effectuer la recherche sur Google avec les Google Dorks
for mot_cle in mots_cles:
    url = f'https://www.google.com/search?q=site:.com intext:"{mot_cle}"'
    reponse = requests.get (url)
    if reponse.status_code == 200:
        print(f"Résultats sur Google avec le Google Dork'{mot_cle}':")
        print(reponse.text)
    else:
        print(f"Erreur lors de la recherche sur Google avec le Google Dork '{mot_cle}': {reponse.status_code}")
