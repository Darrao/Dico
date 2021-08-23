
import string
compteur_lettres = dict(zip(string.ascii_lowercase, [0]*26))
print(compteur_lettres)
fichier_vise = open("j2r","r")
compteur_nbr = 0
for i in fichier_vise:
    for j in i:
        if j in compteur_lettres:
            compteur_lettres[j] +=1
            compteur_nbr +=1
print(compteur_lettres)
print(compteur_nbr)


def compte(nom_fichier):
    import string
    compteur_lettres = dict(zip(string.ascii_lowercase, [0]*26))
    fichier_vise = open(nom_fichier,'r')
    compteur_nbr = 0
    taux_appa = {}
    taux_appa_prct = {}
    lettre_non_trouvee = []
    for i in fichier_vise:
        for j in i:
            if j in compteur_lettres:
                compteur_lettres[j] += 1
                compteur_nbr += 1
    print(compteur_lettres)
  
    for i in compteur_lettres:
        if compteur_lettres[i]!=0:
            print(compteur_lettres[i],"lettre(s) sont présentes",i)
        else:
            print("Pas de lettre",i)
    for i in compteur_lettres:
        if compteur_lettres[i] == 0:
            lettre_non_trouvee.append(i)
    print("Toutes les lettres sont présentes, hormis",lettre_non_trouvee,"dans le fichier",nom_fichier)

    for key in sorted(compteur_lettres, key = compteur_lettres.get, reverse = True):
        taux_appa[key] = compteur_lettres[key]
        taux_appa_prct[key] = str(round((compteur_lettres[key] * 100)/ compteur_nbr,1))+'%'
    print("taux d'apparition des lettres:\n",taux_appa)
    print("En pourcent:\n",taux_appa_prct)

compte("")
