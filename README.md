
# Cube 1 - Concevoir une application informatique

Projet du CESI - DI 2023

## Déploiement

Pour déployer le projet en local suivez les étapés suivantes :

### Initialisation du projet

#### Pour macOS / Linux

```bash
  git clone https://github.com/EwennV/cubes1.git
  cd cubes1/
  python3 -m venv ./
  source bin/activate
  pip install -r requirements.txt
```

Vous pouvez passer à l'étape suivante.


#### Pour Windows
```bash
  git clone https://github.com/EwennV/cubes1.git
  cd cubes1/
  python -m venv ./
  .\Scripts\activate.bat
  pip install -r requirements.txt
```

### Variables d'environnement

Créez le fichier **.env** dans la racine du projet et y ajouter :
```sh
SECRET_KEY="your_secret_key"
API_KEY="your_api_key"
DB_USER="your_db_user_name"
DB_PASSWORD="your_db_password"
DB_HOST="your_db_host"
ALLOWED_HOSTS=0.0.0.0,127.0.0.1,localhost
```
Vous pouvez maintenant migrer votre base de données avec la commande suivante en vérifiant que vous êtes toujours dans votre environnement (cubes1) :
```bash
python ./manage.py migrate
```
Il ne vous reste plus qu'à lancer votre serveur avec la commande :
```bash
python ./manage.py runserver
```

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
git pull origin develop
git push origin le_nom_de_ma_branche
```

### Pull request

Pour faire valider vos modifications par vos collègues il est nécessaire de faire un pull request dans la branche **develop**. Pour ce faire, rendez-vous dans la partie Pull request de GitHub.

## Utilisation de l'API

#### Récupérer tous les relevés

```http
  GET /api/survey/list
```

| Paramètre | Type  | Défaut | Exemple     | Description                                                                             |
| :-------- | :---- | :----- | :---------- | :-------------------------------------------------------------------------------------- |
| `limit`   | `int` | `100`  | `100`       | **Optionnel** Nombre de relevés à recevoir                                              |
| `order`   | `str` | `desc` | `asc`       | **Optionnel** Ordre de tri des données par date                                         |
| `id`      | `str` | `null` | `06190485`  | **Optionnel** Retourne les relevés associés à un id de capteur                          |
| `last`    | `int` | `null` | `24`        | **Optionnel** Défini l'heure à laquelle s'arrêter dans la recherche, rendant le paramètre `limit` inutile |

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

#### Récupérer tous les capteurs

```http
  GET /api/sensor/
```

Par défaut, l'API renverras la liste de tous les capteurs ainsi que leur dernier relevé
| Paramètre | Type     |Défaut | Exemple     | Description                |
| :-------- | :------- | :---- | :---------- | :------------------------- |
| `id`      | `str`    | `none`| `06190485`  | **Optionnel** Récupère les données du capteur avec cet id |

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

#### Ajouter un capteur

```http
  GET /api/sensor/create
```

L'API renverras un code 200 avec une clé "message" en JSON si la création du capteur s'est terminée ou un code 400 avec une clé "error" en JSON si une erreur est survenue.
| Paramètre | Type     |Défaut | Exemple     | Description                |
| :-------- | :------- | :---- | :---------- | :------------------------- |
| `id`      | `str`    | `none`| `06190485`  | **Obligatoire** Id du capteur à ajouter |
| `name`      | `str`    | `none`| `06190485`  | **Obligatoire** Nom du capteur à ajouter |
| `lat`      | `float`    | `none`| `-0.55445445`  | **Obligatoire** Lattitude du capteur à ajouter |
| `lng`      | `float`    | `none`| `-0.19725624`  | **Obligatoire** Longitude du capteur à ajouter |

Exemple de retour de l'API:
```json
    {
        "message": "Capteur ajouté !"
    }
```

#### Modifier un capteur

```http
  GET /api/sensor/update
```

L'API renverras un code 200 avec une clé "message" en JSON si la modification du capteur s'est terminée ou un code 400 avec une clé "error" en JSON si une erreur est survenue.
| Paramètre | Type     |Défaut | Exemple     | Description                |
| :-------- | :------- | :---- | :---------- | :------------------------- |
| `id`      | `str`    | `none`| `06190485`  | **Obligatoire** Id du capteur à modifier |
| `name`      | `str`    | `none`| `06190485`  | **Obligatoire** Nom du capteur à modifier |
| `lat`      | `float`    | `none`| `-0.55445445`  | **Obligatoire** Lattitude du capteur à modifier |
| `lng`      | `float`    | `none`| `-0.19725624`  | **Obligatoire** Longitude du capteur à modifier |

Exemple de retour de l'API:
```json
    {
        "message": "Capteur mis à jour !"
    }
```

#### Supprimer un capteur

```http
  GET /api/sensor/delete
```

L'API renverras un code 200 avec une clé "message" en JSON si la suppression du capteur s'est terminée ou un code 400 avec une clé "error" en JSON si une erreur est survenue.
| Paramètre | Type     |Défaut | Exemple     | Description                |
| :-------- | :------- | :---- | :---------- | :------------------------- |
| `id`      | `str`    | `none`| `06190485`  | **Obligatoire** Id du capteur à supprimer |

Exemple de retour de l'API:
```json
    {
        "message": "Capteur supprimé !"
    }
```


#### Récupérer toutes les alertes

```http
  GET api/alert
```
Par défaut l'API renverras la liste de toutes les alertes de la base de données avec leurs destinaites `recipients` associés
| Paramètre | Type     |Défaut | Exemple     | Description                |
| :-------- | :------- | :---- | :---------- | :------------------------- |
| `id`      | `Uuid`    | `none`| `33028bcc-1e10-4cda-9a30-13e8a36433f0`  | **Optionnel** Récupère les informations de l'alerte avec cet id |

Exemple de retour de l'API:
```json
    {
        "frequency": 240,
        "humidity_inferior": 10,
        "humidity_superior": 100,
        "temperature_inferior": -10.0,
        "temperature_superior": 11.0,
        "recipients": [
            "adresse.mail@test.fr"
        ],
        "id": "33028bcc-1e10-4cda-9a30-13e8a36433f0"
    }
```

#### Créer une alerte

```http
  GET api/alert/create
```
L'API renverras un code 200 avec une clé "message" en JSON si la création du capteur s'est terminée ou un code 400 avec une clé "error" en JSON si une erreur est survenue.
| Paramètre | Type     |Défaut | Exemple     | Description                |
| :-------- | :------- | :---- | :---------- | :------------------------- |
| `frequency`      | `str`    | `none`| `50`  | **Obligatoire** Fréquence de l'envoie d'alerte en minutes|
| `temperature_superior`      | `float`    | `none`| `60`  | **Optionnel** Seuil de température maximum de l'alerte en °C|
| `temperature_inferior`      | `float`    | `none`| `0`  | **Optionnel** Seuil de température minimum de l'alerte °C|
| `humidity_superior`      | `int`    | `none`| `100`  | **Optionnel** Seuil d'humidité maximum de l'alerte en %|
| `humidity_inferior`      | `int`    | `none`| `10`  | **Optionnel** Seuil d'humidité minimum de l'alerte en %|
| `recipients`      | `array`    | `none`| `['test@test.com', 'foo@bar.com']`  | **Obligatoire** Liste des destinataires de l'alerte|

Exemple de retour de l'API:
```json
    {
      "message":"Alerte créée"
    }
```

#### Mettre à jour une alerte

```http
  GET api/alert/update
```
L'API renverras un code 200 avec une clé "message" en JSON si la mise à jour du capteur s'est terminée ou un code 400 avec une clé "error" en JSON si une erreur est survenue.
| Paramètre | Type     |Défaut | Exemple     | Description                |
| :-------- | :------- | :---- | :---------- | :------------------------- |
| `id`      | `Uuid`    | `none`| `33028bcc-1e10-4cda-9a30-13e8a36433f0`  | **Obligatoire** Id de l'alerte à mettre à jour|
| `frequency`      | `str`    | `none`| `50`  | **Obligatoire** Fréquence de l'envoie d'alerte en minutes|
| `temperature_superior`      | `float`    | `none`| `60`  | **Optionnel** Seuil de température maximum de l'alerte en °C|
| `temperature_inferior`      | `float`    | `none`| `0`  | **Optionnel** Seuil de température minimum de l'alerte °C|
| `humidity_superior`      | `int`    | `none`| `100`  | **Optionnel** Seuil d'humidité maximum de l'alerte en %|
| `humidity_inferior`      | `int`    | `none`| `10`  | **Optionnel** Seuil d'humidité minimum de l'alerte en %|
| `recipients`      | `array`    | `none`| `['test@test.com', 'foo@bar.com']`  | **Obligatoire** Liste des destinataires de l'alerte|

Exemple de retour de l'API:
```json
    {
      "message":"Alerte mise à jour"
    }
```

#### Supprimer une alerte

```http
  GET api/alert/delete
```
L'API renverras un code 200 avec une clé "message" en JSON si la suppression du capteur s'est terminée ou un code 400 avec une clé "error" en JSON si une erreur est survenue.
| Paramètre | Type     |Défaut | Exemple     | Description                |
| :-------- | :------- | :---- | :---------- | :------------------------- |
| `id`      | `Uuid`    | `none`| `33028bcc-1e10-4cda-9a30-13e8a36433f0`  | **Obligatoire** Id de l'alerte à mettre à jour|

Exemple de retour de l'API:
```json
    {
      "message":"Alerte supprimée"
    }
```



## Auteurs

- [@TerryGyselings](https://github.com/TerryGyselings)
- [@fromeof](https://github.com/fromeof)
- [@EwennV](https://github.com/EwennV)
