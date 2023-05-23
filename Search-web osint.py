import requests

def search_social_media(username):
    social_media_sites = [
        'https://www.facebook.com/{}',
        'https://twitter.com/{}',
        'https://www.instagram.com/{}',
        'https://www.linkedin.com/in/{}',
        'https://github.com/{}'
    ]

    print("Recherche d'informations pour l'utilisateur : {}".format(username))
    for site in social_media_sites:
        url = site.format(username)
        response = requests.get(url)
        if response.status_code == 200:
            print("Site : {}".format(url))
        else:
            print("Aucune information trouvée sur : {}".format(url))

# Exemple d'utilisation
username = "rober"
search_social_media(username)
