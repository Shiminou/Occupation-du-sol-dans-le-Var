# Ouvrir le fichier index.html
with open("index.html", "r") as file:
    html_content = file.read()

# Remplacer tous les chemins relatifs incorrects
html_content = html_content.replace('href="css/', 'href="carte/css/')
html_content = html_content.replace('src="css/', 'src="carte/css/')

# Sauvegarder le fichier modifié
with open("index.html", "w") as file:
    file.write(html_content)

print("Les chemins ont été modifiés avec succès !")
