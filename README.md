# verification_Operateurs_DSP2
Ce script vérifie si les opérateurs présents dans le [fichier de l'Arcep](https://www.data.gouv.fr/fr/datasets/identifiants-de-communications-electroniques/), librement téléchargeable, sont des [établissements de paiement](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072026/LEGISCTA000020862288/) ou des [prestataires de services de paiement](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006072026/LEGISCTA000020863201/), en interrogeant la base REGAFI par l'[API de l'ACPR](https://developer.regafi.banque-france.fr/).

## Ecrit avec
* [Python](https://www.python.org/) - Le langage de programmation utilisé

## Prérequis
Vous devez au préalable créer un compte sur le [site de l'ACPR](https://developer.regafi.banque-france.fr/) vous permettant d'utiliser les différentes API, en entrer par la suite dans le script Python vos identifiants adéquats, notamment le jeton d'accès.

## Versions
[SemVer](http://semver.org/) est utilisé pour la gestion des versions. Pour connaître les versions disponibles, veuillez vous référer aux [étiquettes de ce dépôt](https://github.com/BaptisteHugot/verification_Operateurs_DSP2/releases/).

## Auteurs
* **Baptiste Hugot** - *Travail initial* - [BaptisteHugot](https://github.com/BaptisteHugot)

## Licence
Ce projet est disponible sous licence MIT. Veuillez lire le fichier [LICENSE.md](LICENSE.md) pour plus de détails.

## Règles de conduite
Pour connaître l'ensemble des règles de conduite à respecter sur ce dépôt, veuillez lire le fichier [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Contribution au projet
Si vous souhaitez contribuer au projet, que ce soit en corrigeant des bogues ou en proposant de nouvelles fonctionnalités, veuillez lire le fichier [CONTRIBUTING.md](CONTRIBUTING.md) pour plus de détails.