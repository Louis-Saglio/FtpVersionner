from fabric.api import env, get, run
from module import del_first_letters
from os import remove
from shutil import rmtree
from os.path import isdir

env.host_string = '192.168.56.101'
env.user = 'clean'
env.password = '159Ukicz!'

# Categoria in quam limae sunt transmovendae
client_root = "C:\\Users\\Louis Saglio\\Desktop\\Demo\\"
# Via categoriae ubi sunt transmovendae
server_root = "/home/clean/file-server/"
# Via scripti dans viam omniarum limarum
liste_des_fichiers = client_root + ".liste-des-fichiers"

# Delere limas locales
if isdir(client_root):
    rmtree(client_root)


run("/home/clean/list_files")
get("/home/clean/liste-des-fichiers", liste_des_fichiers)

with open(liste_des_fichiers, 'r') as liste_fichiers:
    for fichier in liste_fichiers:
        file = del_first_letters(fichier, server_root)
        file = file[:len(file)-1:]
        get(fichier[:len(fichier)-1:], client_root + file)

remove(liste_des_fichiers)