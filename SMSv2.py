#!/usr/bin/python
#coding:utf-8
import os, sys, time, random

# Creation de la syntaxe pour inter-agir avec Gammu
syntax = ['gammu sendsms TEXT', '+33_YOUR_NUMBER_HERE', '-text']

# Commande passer par SMS et lu par le programme
hlp = ['help', 'Help']

# Declaration des chemins pour les boites de reception et denvoie
inbox = "/home/pi/app/inbox/"
reponse = "/home/pi/app/reponse/"

# Fonction qui permet de lire le SMS dans la boite de reception
def read_sms(path):
        for files in os.listdir(path):
                os.chdir(path)
                intxt = open(files, "r").read()
                intxt = intxt.strip('\n')
                if(intxt in hlp):
                        return True;
                else:
                        return False;

# Fonction qui permet de SEND l'aide pour l'utilisateur 
def send_help():
        cmd = " ".join(syntax)
        for files in os.listdir(reponse):
                os.chdir(reponse)
                intxt = open(files, "r").read()
                intxt = intxt.strip('\n')
                send = '%s "%s"' %(cmd, intxt)
                os.system(send)

# Debut du code
try:
        if(read_sms(inbox) == True):
                send_help()
except:
        print("Error : No command")
