#! /usr/bin/python3
# coding: utf-8

# Ce fichier est à placer sur le serveur à l'emplacement suivant : /home/clean/file-server

from os import walk

with open('liste-des-fichiers', 'w') as file:
        for dossier, sous_dossiers, fichiers in walk('/home/clean/file-server'):
                for fichier in fichiers:
                        try:
                                print(dossier + '/' + fichier, file=file)
                        except:
                                print(dossier + '/' +fichier)
