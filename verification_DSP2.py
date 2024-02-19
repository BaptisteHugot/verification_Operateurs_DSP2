# Bibliothèques à importer
import http.client
import json
import pandas as pd
import time

st = time.time() # Début du chronomètre
print("Programme démarré")

# Fonction qui convertit un SIRET en SIREN
def convertSiretToSiren(siret):
    siret.replace(" ","") # On supprime les espaces
    if(len(siret)<9): # Si le SIRET est inférieur à 9 caractères (taille du SIREN), on ne le prend pas en compte
        siren = ""
    else:
        siren = siret[0:9] # On ne garde que les 9 premiers chiffres du SIRET
    return siren

# URL de connexion à l'API
connection = http.client.HTTPSConnection("api.regafi.banque-france.fr")

# Entêtes nécessaires pour récupérer les éléments de l'API
headers = {
    "X-IBM-Client-Id": "XXXXXXXXX", # Entrez ici votre identifiant personnel
    "accept": "application/json"
    }

# On récupère la liste des opérateurs
data = pd.read_csv("https://www.data.gouv.fr/fr/datasets/r/b0f62183-cd0c-498d-8153-aa1594e5e8d9", sep=";",encoding="latin-1")

numberLines = data.shape[0] # Nombre de lignes à analyser
increment = 0 # Variable incrémentale pour savoir où l'on en est de l'analyse du fichier
dataCompleted = {"Siren":[], "Description":[], "Statut":[], "Code_Opérateur":[], "Nom_Opérateur":[]} # Dictionnaire contenant l'ensemble des informations issues de l'API

# On parcourt la liste des opérateurs
for num in range(0, len(data)):
    sirenFromSiret = convertSiretToSiren(str(data["SIRET_ACTEUR"][num]))
    increment = increment + 1
    if(sirenFromSiret != ""):
        url="/regafi-fr/v1/fr/entities/searchbysiren?siren="+sirenFromSiret # URL d'interrogation de l'API
        connection.request("GET", url, headers=headers)
        response = connection.getresponse()
        dataRegafi = json.loads(response.read())

        dataCompleted["Statut"].append(dataRegafi["status"])
        dataCompleted["Code_Opérateur"].append(data["CODE_OPERATEUR"][num])
        dataCompleted["Nom_Opérateur"].append(data["IDENTITE_OPERATEUR"][num])
        dataCompleted["Siren"].append(sirenFromSiret)

        if int(dataRegafi["status"]) == 200: # Si le Siren existe dans Regafi
            existingData = 0 # Variable pour indiquer si des données sont déjà présentes dans le champ Description
            dataDescription = "" # Variable stockant les descriptions de la société
            
            if "company_description" in dataRegafi["data"][0]: # Si la société est un établissement de paiement
                dataDescription = dataRegafi["data"][0]["company_description"]["description"]
                existingData = 1
                
            if "detail_agent" in dataRegafi["data"][0]: # Si la société est un agent de paiement
                if existingData == 1:
                    dataDescription = dataDescription + " / Agent prestataire de services de paiement"
                else:
                    dataDescription = "Agent prestataire de services de paiement"
                existingData = 2

            if "mandates" in dataRegafi["data"][0]: # Si la société a un mandataire, elle est également un agent de paiement
                if existingData == 1:
                    dataDescription = dataDescription + " / Agent prestataire de services de paiement"
                elif existingData == 0:
                    dataDescription = "Agent prestataire de services de paiement"

            dataCompleted["Description"].append(dataDescription)
        elif int(dataRegafi["status"]) == 404: # Si le Siren n'existe pas dans Regafi
            dataCompleted["Description"].append("N/A")

        print(str(increment) + " / " + str(numberLines)) # On affiche la progression

    time.sleep(12) # Pour prendre en compte la limite maximale de 300 requêtes par heure

# Export des données au format csv
dataframe = pd.DataFrame(dataCompleted)
dataframe.to_csv(r"./MAJOPE_Regafi.csv", header=["SIREN","DESCRIPTION","STATUT","CODE_OPERATEUR","NOM_OPERATEUR"], index=False, sep=";",encoding="latin-1")

et = time.time() # Fin du chronomètre
elapsed_time = time.strftime("%H:%M:%S", time.gmtime(et - st)) # Durée d'exécution du programme
print("Programme exécuté en : ", elapsed_time, ".")
