from fabric.api import env, run, put
from os import walk, getcwd
from module import *
from ftplib import FTP

env.host_string = '192.168.56.101'
env.user = 'clean'
env.password = '159Ukicz!'

ftp = FTP(env.host_string, env.user, env.password)

server_root = '/home/clean/file-server'
client_root = "C:\\Users\\Louis Saglio\\Demo"

# noinspection PyBroadException
try:
    run('rm -r ' + server_root)
except:
    print("Impossible de supprimer", server_root)


for dossier, sous_dossiers, fichiers in walk(client_root):
    dir_name = server_root + '/' + windows_to_unix_path_style(del_first_letters(dossier, client_root))
    run("mkdir " + dir_name)
    ftp.cwd(dir_name)
    for fichier in fichiers:
        file_name = dossier + '\\' + fichier
        with open(file_name, 'rb') as file:
            ftp.storbinary('STOR ' + fichier, file)
