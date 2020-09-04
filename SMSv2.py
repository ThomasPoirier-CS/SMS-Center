#!/usr/bin/python
#coding:utf-8

import os, sys, time, random


""" Variable pour construire la Syntaxe qui permet d'envoyer le SMS """
""" Changer le numéro ci dessous """

number = "+33_your_number"
txt = "-text"
gam = "gammu sendsms TEXT"
""" -------------------------------------------------------------- """
""" Action sur une machine du réseau, utilisant une connection SSH """
""" -------------------------------------------------------------- """
sht = open("/root/Command/SRV2Cmd-shut.txt", "r")
sht = sht.read()
scn = open("/root/Command/Scancmd.txt", "r")
scn = scn.read()
srva = open("/root/Command/SRV2cmd-reboot.txt", "r")
srva = srva.read()
""" ---------------------------------------------------------------- """
""" Transfere d'un SMS reçue n'executant pas un commande enregistrer """
""" ---------------------------------------------------------------- """
trsf = open("/root/Command/Transfert-cmd.txt", "r")
trsf = trsf.read()
flsh = open("/root/Command/Flush-cmd.txt", "r")
flsh = flsh.read()
rmvar = open("/root/Command/Flush-Archive-cmd.txt", "r")
rmvar = rmvar.read()
""" ---------------------------------------------------------------- """
""" -----------Action Diverse Executé par le Serveur SMS------------ """
fun = open("/root/Command/Fun.txt", "r")
fun = fun.read()
vex = open("/root/Command/Vexer.txt", "r")
vex = vex.read()
ques = open("/root/Command/Question.txt", "r")
ques = ques.read()
rep2 = open("/root/Command/Reponse.txt", "r")
rep2 = rep2.read()
rep3 = open("/root/Command/Reponse2.txt", "r")
rep3 = rep3.read()
""" ---------------------------------------------------------------- """
""" --- Liste des Helpers pour obtenir les Commandes Exécutable ---- """
hlp = open("/root/Command/Help-cmd.txt", "r")
hlp = hlp.read()
hlpwb = open("/root/Command/Help-Web.txt", "r")
hlpwb = hlpwb.read()
""" ---------------------------------------------------------------- """
""" ---------------------- Début du programme ici ------------------ """
""" ---------------------------------------------------------------- """
for extension in os.listdir("/var/spool/gammu/inbox/"):
        sms = "/var/spool/gammu/inbox/%s" %(extension)
        contener = open(sms, "r").readlines()
        for act in contener:
                act = act.strip('\n')
                if act in hlp != False:
                        os.system("rm /var/spool/gammu/inbox/*.txt")
                        hlp = open("/home/parrot/SRV-SMS/Fun/Helper/1", "r")
                        hlp = hlp.read()
                        send = "%s %s %s %s" %(gam, number, txt, hlp)
                        os.system(send)
                        exit()
                if act in hlpwb != False:
                		os.system("rm /var/spool/gammu/inbox/*.txt")
                		os.system("cp /home/parrot/SRV-SMS/Fun/Helper/List-Command.txt /var/www/html/transfert/")
                		os.system("python /home/parrot/SRV-SMS/sshcphlp.py")
                		hlpwb = open("/home/parrot/SRV-SMS/Fun/Helper/3", "r")
                		hlpwb = hlpwb.read()
                		send = "%s %s %s %s" %(gam, number, txt, hlpwb)
                		os.system(send)                		
                		exit()
                if act in sht != False:
                        os.system("python /home/parrot/SRV-SMS/sshs.py")
                        os.system("rm /var/spool/gammu/inbox/*.txt")
                        shut = open("/var/spool/gammu/SMS/shutdownsrv2.txt", "r")
                        shut = shut.read()
                        ext = "%s %s %s %s" %(gam, number, txt, shut)
                        os.system(ext)
                        sign = open("/var/spool/gammu/SMS/sign.txt", "r")
                        sign = sign.read()
                        foot = "%s %s %s %s" %(gam, number, txt, sign)
                        os.system(foot)
                        exit()
                if act in fun != False:
                        os.system("rm /var/spool/gammu/inbox/*.txt")
                        os.system("python /root/Random-rep/random-reponseFun.py")
                        exit()
                if act in rep2 != False:
                        os.system("rm /var/spool/gammu/inbox/*.txt")
                        os.system("python /root/Random-rep/random-reponseRep.py")
                        exit()
                if act in rep3 != False:
                        os.system("rm /var/spool/gammu/inbox/*.txt")
                        os.system("python /root/Random-rep/random-reponseRep2.py")
                        exit()                        
                if act in ques != False:
                        os.system("rm /var/spool/gammu/inbox/*.txt")
                        os.system("python /root/Random-rep/random-reponseQues.py")
                        exit()
                if act in scn != False:
                        os.system("iwconfig wlan0 down")
                        os.system("iwlist wlan0 scan > /home/parrot/SRV-SMS/result.txt")
                        scan = open("/var/spool/gammu/SMS/Wifi-scan.txt")
                        scan = scan.read()
                        send = "%s %s %s %s" %(gam, number, txt, scan)
                        os.system(send)
                        os.system("rm /var/spool/gammu/inbox/*.txt")
                        sign = open("/var/spool/gammu/SMS/sign.txt", "r")
                        sign = sign.read()
                        foot = "%s %s %s %s" %(gam, number, txt, sign)
                        os.system(foot)
                        exit()
                if act in srva != False:
                        os.system("python /home/parrot/SRV-SMS/sshr.py")
                        os.system("mv /var/spool/gammu/inbox/*.txt /home/parrot/archive")
                        reb = open("/var/spool/gammu/SMS/rebootsrv2.txt", "r")
                        reb = reb.read()
                        rel = "%s %s %s %s" %(gam, number, txt, reb)
                        os.system(rel)
                        sign = open("/var/spool/gammu/SMS/sign.txt", "r")
                        sign = sign.read()
                        foot = "%s %s %s %s" %(gam, number, txt, sign)
                        os.system(foot)
                        exit()                      
                if act in trsf != False:
                        os.system("rm /var/spool/gammu/inbox/*.txt")
                        os.system("mv /home/parrot/archive/*.txt /var/www/html/transfert/")
                        os.system("python /home/parrot/SRV-SMS/sshcp.py")
                        cont = open("/root/send/Transfert/Transfert-notify.txt", "r")
                        cont = cont.read()
                        send = "%s %s %s %s" %(gam, number, txt, cont)
                        os.system(send)
                        time.sleep(5)
                        os.system("rm /var/www/html/transfert/*")
                        exit()
                if act in rmvar != False:
                        os.system("rm /home/parrot/archive/*")
                        rem = open("/root/send/Delete-Archive/del-sms.txt", "r")
                        rem = rem.read()
                        send = "%s %s %s %s" %(gam, number, txt, rem)
                        os.system(send)
                        exit()
                if act in flsh != False:
                        os.system("python /home/parrot/SRV-SMS/sshflsh.py")
                        os.system("rm /var/spool/gammu/inbox/*.txt")
                        os.system("rm /var/www/html/transfert/*.txt")
                        conf = open("/root/send/WebAction/Flush/Flush-sms.txt", "r")
                        conf = conf.read()
                        send = "%s %s %s %s" %(gam, number, txt, conf)
                        os.system(send)
                        exit()
                else:
                        os.system("mv /var/spool/gammu/inbox/*.txt /home/parrot/archive")
                        model = open("/var/spool/gammu/SMS/response-no-command.txt", "r")
                        model = model.read()
                        body = "%s %s %s %s" %(gam, number, txt, model)
                        os.system(body)
                        sign = open("/var/spool/gammu/SMS/sign.txt", "r")
                        sign = sign.read()
                        foot = "%s %s %s %s" %(gam, number, txt, sign)
                        os.system(foot)
                        exit()
        exit()                
exit()

