from fabric.api import env, get, run
from module import del_first_letters
from os import remove
from shutil import rmtree
from os.path import isdir

env.host_string = '192.168.56.101'
env.user = 'clean'
env.password = '159Ukicz!'

client_root = "C:\\Users\\Louis Saglio\\Desktop\\Test-pull\\"
server_root = "/home/clean/file-server/"
liste_des_fichiers = client_root + ".liste-des-fichiers"

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