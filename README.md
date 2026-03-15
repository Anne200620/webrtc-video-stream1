# WebRTC Video Streaming Lab

## Description

Ce projet implémente un système simple de streaming vidéo en utilisant WebRTC avec Python.

Le serveur capture les images de la webcam avec OpenCV et les transmet aux clients.  
Le client reçoit les trames vidéo et les affiche à l'écran.

## Technologies utilisées

- Python
- WebRTC
- aiortc
- OpenCV

## Installation

Créer l'environnement conda :

conda env create -f environment.yaml

Activer l'environnement :

conda activate webrtc-env

## Exécution

Lancer le serveur :

python server.py

Puis lancer le client :

python client.py

Le client affichera la vidéo provenant de la webcam du serveur.
