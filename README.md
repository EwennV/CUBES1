
# Cube 1 - Concevoir une application informatique

Projet du CESI - DI 2023

## Déploiement

Pour déployer le projet en local suivez les étapés suivantes :

### Pour macOS / Linux

```bash
  git clone https://github.com/EwennV/cubes1.git
  cd cubes1/
  python3 -m venv ./
  source bin/activate
  pip install -r requirements.txt
```
Créez le fichier **.env** dans la racine du projet et y ajouter :
```env
SECRET_KEY="your secret_key here"
API_KEY="your api_key here"
```
Vous pouvez maintenant migrer votre base de données avec la commande suivante en vérifiant que vous êtes toujours dans votre environnement (cubes1) :
```bash
python ./manage.py migrate
```
Il ne vous reste plus qu'à lancer votre serveur avec la commande :
```bash
python ./manage.py runserver
```


### Pour Windows
```bash
  git clone https://github.com/EwennV/cubes1.git
  cd cubes1/
  python3 -m venv ./
  .\Scripts\activate.bat
  pip install -r requirements.txt
```
Créez le fichier **.env** dans la racine du projet et y ajouter :
```env
SECRET_KEY="your secret_key here"
API_KEY="your api_key here"
```
Vous pouvez maintenant migrer votre base de données avec la commande suivante en vérifiant que vous êtes toujours dans votre environnement (cubes1) :
```bash
python ./manage.py migrate
```
Il ne vous reste plus qu'à lancer votre serveur avec la commande :
```bash
python ./manage.py runserver
```



## Environment Variables

Pour lancer ce projet, vous avez besoin d'ajouter les variables d'environment suivantes dans un .env que vous devez créer à la racine du projet

`SECRET_KEY`

`API_KEY`



## Auteurs

- [@TerryGyselings](https://github.com/TerryGyselings)
- [@fromeof](https://github.com/fromeof)
- [@EwennV](https://github.com/EwennV)

## Développer avec GIT

Pour correctement push ses modifications sur le dépôt distant suivez les étapes ci-dessous

Commencez par switch vers votre branche

Si votre branche n'existe pas :
```bash
git checkout -b le_nom_de_ma_branche
```
Si elle existe :
```bash
git checkout le_nom_de_ma_branche
```

Développer votre feature / ce que vous voulez

Et ensuite enregistez vos modifications, pour ce faire éxecutez les commandes suivantes :

```bash
git add .
git commit -m "la_description_de_votre_modification"
git push origin le_nom_de_ma_branche
```