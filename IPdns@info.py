import dns.resolver

domain = input("Entrez le nom de domaine à rechercher: ")
print("\n")

# Résolution de l'enregistrement A
try:
    a_records = dns.resolver.resolve(domain, 'A')
    for record in a_records:
        print("Adresse IP : ", record.address)
        print("Serveur DNS : ", record.target)
        print("TTL : ", record.ttl)
        print("\n")
except dns.resolver.NoAnswer:
    print("Aucun enregistrement A trouvé.\n")

# Résolution de l'enregistrement MX
try:
    mx_records = dns.resolver.resolve(domain, 'MX')
    for record in mx_records:
        print("Serveur MX : ", record.exchange)
        print("Priorité : ", record.preference)
        print("TTL : ", record.ttl)
        print("\n")
except dns.resolver.NoAnswer:
    print("Aucun enregistrement MX trouvé.\n")

# Résolution de l'enregistrement NS
try:
    ns_records = dns.resolver.resolve(domain, 'NS')
    for record in ns_records:
        print("Serveur de noms : ", record.target)
        print("TTL : ", record.ttl)
        print("\n")
except dns.resolver.NoAnswer:
    print("Aucun enregistrement NS trouvé.\n")
