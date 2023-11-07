
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
DB_USER=""
DB_PASSWORD=""
DB_HOST=""
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
  python -m venv ./
  .\Scripts\activate.bat
  pip install -r requirements.txt
```
Créez le fichier **.env** dans la racine du projet et y ajouter :
```env
SECRET_KEY="your secret_key here"
API_KEY="your api_key here"
DB_USER=""
DB_PASSWORD=""
DB_HOST=""
```
Vous pouvez maintenant migrer votre base de données avec la commande suivante en vérifiant que vous êtes toujours dans votre environnement (cubes1) :
```bash
python ./manage.py migrate
```
Il ne vous reste plus qu'à lancer votre serveur avec la commande :
```bash
python ./manage.py runserver
```



## Variables d'environment

Pour lancer ce projet, vous avez besoin d'ajouter les variables d'environment suivantes dans un .env que vous devez créer à la racine du projet

`SECRET_KEY`

`API_KEY`

`DB_USER`

`DB_PASSWORD`

`DB_HOST`

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
## Utilisation de l'API

#### Récupérer tous les relevés

```http
  GET /api/survey/list
```

| Paramètre | Défaut| Exemple     | Description                |
| :-------- | :----|:---------| :------------------------- |
| `limit`   | `100`| `100` | **Optionnel** Nombre de relevés à recevoir |
| `order`   | `desc`| `asc` | **Optionnel** Ordre de tri des données par date|
| `id`   | `null`| `06190485`| **Optionnel** Retourne les relevés associés à un id de capteur|

Les différents paramètres peuvent êtres utilisés ensembles.

Exemple de requête comprenant les paramètres précédents :
```http
  GET /api/survey/list?id=06190485&order=asc&limit=10
```

Exemple de retour de l'API:

```json
    {
        "model": "API.survey",
        "pk": "c6f02fb6-792c-45f5-912b-82225f019602",
        "fields": {
            "idSurvey": 146757,
            "temperature": 122,
            "humidity": 90,
            "battery_level": 3571,
            "rssi": 30,
            "date": "2023-10-28T07:51:36Z",
            "sensor_id": "62190434"
        }
    },
```


#### Récupérer tous les capteurs enregistrés

```http
  GET /api/sensor/
```

Par défaut, l'API renverras la liste de tous les capteurs ainsi que leur dernier relevé
| Paramètre | Type     |Défaut| Exemple     | Description                |
| :-------- | :------- | :----|:---------| :------------------------- |
| `id`   | `str`    | `none`| `06190485` | **Optionnel** Récupère les données du capteur avec cet id |

Exemple de retour de l'API:
```json
    {
        "model": "API.sensor",
        "pk": "06190485",
        "fields": {
            "name": "Capteur cuisine",
            "lattitude": null,
            "longitude": null
        }
    }
```

## Auteurs

- [@TerryGyselings](https://github.com/TerryGyselings)
- [@fromeof](https://github.com/fromeof)
- [@EwennV](https://github.com/EwennV)
