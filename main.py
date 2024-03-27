#Importation des modules 
import pandas as pd
import mysql.connector
from mysql.connector import Error

#Chargement des données
Raisin = pd.read_excel(r'C:\Users\LAB-MND\Desktop\TP\Raisin_Dataset.xlsx')
print(Raisin.columns)

colonnes = ['Area','MajorAxisLength','MinorAxisLength','Eccentricity','ConvexArea','Extent','Perimeter',"Class"]
Raisin.columns = colonnes 
print('----------------------------------------------------------------')
print(Raisin.columns)

# Chargement du dataframe dans MYSQL
try:
    connexion = mysql.connector.connect(host='localhost',
                                       database='raisins',
                                       user='root',
                                       password='')
    if connexion.is_connected():
        print('Connexion à MySQL réussie')
except Error as e:
    print(f"Erreur lors de la connexion à MySQL: {e}")

try:
    cursor = connexion.cursor()

    for i,row in Raisin.iterrows():
        sql = """INSERT INTO raisin_grains(Area, MajorAxisLength, MinorAxisLength, Eccentricity, ConvexArea, Extent, Perimeter, Class) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        #print(sql)
        cursor.execute(sql, tuple(row))

    connexion.commit()
    connexion.close()
    print("DataFrame chargé dans MySQL avec succès!")
except Exception as e:
    print(f"Erreur lors du chargement du DataFrame dans MySQL: {e}")
