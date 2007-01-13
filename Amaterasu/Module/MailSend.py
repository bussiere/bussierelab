#!/usr/bin/env python
# -*- Encoding: UTF-8 -*-
"""
Ceci est une reprise du programme mxmail. 

24/03/2006 -utilisation du module email
"""
import string, sys, types, os, tempfile, time
import email
from email import Encoders
from email.MIMEAudio import MIMEAudio
from email.MIMEBase import MIMEBase
from email.MIMEImage import MIMEImage
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import mimetypes
import smtplib

def FICHIER( chemin ):
    """Guess the content type based on the file's extension. Encoding
    will be ignored, altough we should check for simple things like
    gzip'd or compressed files."""
    ctype, encoding = mimetypes.guess_type(chemin)
    if ctype is None or encoding is not None:
        # No guess could be made, or the file is encoded (compresses), so
        # use a generic bag-of-bits type.
        ctype = 'application.octet-stream'
    maintype, subtype = ctype.split('/', 1)
    if maintype == 'text':
        fp = open(chemin)
        # Note : we should handle calculating the charset
        msg = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == 'image':
        fp = open(chemin, 'rb')
        msg = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == 'audio':
        fp = open(chemin, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(chemin, 'rb')
        msg = MIMEBase(maintype, subtype)
        msg.set_payload(fp.read())
        fp.close()
        # Encode the payload using Base64
        Encoders.encode_base64(msg)
    # Set the filename parameter
    fichier = os.path.basename(chemin)
    msg.add_header('Content-Disposition','attachment',filename=fichier)
    return msg

class mxmMail:
    """
    mxmMail est client e-mail qui permet d'envoyer un e-mail de la même façon
    qu'en utilisant un simple client e-mail comme outlook express ou le client
    mail de netscape.
    Licence: TIUISICIIDC (Take it, use it, sell it, change it. I dont care.)
    contact: maxm@normik.dk, maxmcorp@worldonline.dk, maxm@mxm.dk
    """

    def __init__(self, fromName='', fromAddress='', subject='', message='', SMTPServer=''):
        self.fromName     = fromName
        self.fromAddress  = fromAddress
        self.subject      = subject
        self.message      = message
        self.recipients   = []
        self.attachments  = []
        self.SMTPServer   = SMTPServer

    def __str__(self):
        return self.message

    def prepend(self, text):
        """
        Ajoute une chaine avant le corps du message.
        """
        self.message = text + self.message

    def append(self, text):
        """
        Ajoute une chaine après le corps du message.
        """
        self.message = self.message + text

    def prependFile(self, fileName):
        """
        Cette méthode ajoute le contenu d'un fichier texte avant le corps du
        message.
        Une utilisation est d'ajouter fichier d'entête commun au début du
        message.
        Cela peut être fait plusieurs fois pour ajouter différents fichiers
        texte dans un ordre spécifique.
        Si le fichier ne peut être ouvert, la méthode va échoué silencieusement.
        C'est un choix délibéré pour que les mailings automatiques ne soient pas
        arrêtés par des fichiers entêtes/pieds manquants.
        """
        try:
            file = open(fileName)
            self.prepend(file.read())
        except:
            pass # Just fail silently

    def appendFile(self, fileName):
        """
        Cette méthode ajoute le contenu d'un fichier texte avant le corps du
        message.
        Une utilisation est d'ajouter un fichier signature à la fin du message.
        Cela peut être fait plusieurs fois pour ajouter différents fichiers
        texte dans un ordre spécifique.
        Si le fichier ne peut être ouvert, la méthode va échouer silencieusement.
        C'est un choix délibéré pour que les mailings automatiques ne soient pas
        arrêtés par des fichiers entêtes/pieds manquants.
        """
        try:
            file = open(fileName)
            self.append(file.read())
        except:
            pass # Just fail silently

    def recipientAppend(self, toName, toAddress):
        """
        Ajoute un destinataire de plus au message.
        """
        self.recipients.append({'toName':toName, 'toAddress':toAddress})

    def setRecipients(self, recipients=[]):
        self.recipients = recipients

    def attachmentAppend(self, fileName):
        """
        Ajoute une pièce jointe au message. Elle est automatiquement converti
        dans un type mime.
        """
        self.attachments.append(fileName)

    def send(self):
        """Envoie le message."""
        message = MIMEMultipart()
        message['From'] = self.fromAddress
        message['Subject'] = self.subject

        recipientList = []
        for recipient in self.recipients:
            recipientList.append(recipient['toAddress'])
            adressList = string.join(recipientList, '; ')
            message['To'] = adressList
            if type(self.message) == str:
                message.attach(MIMEText(self.message,'html') )
            elif type(self.message) == unicode:
                message.attach( MIMEText(self.message.encode('utf-8'), 'html', 'utf-8') )
            for attachFile in self.attachments:
                # encodes the attached files
                if type(attachFile) == types.StringType:
                    fileName = attachFile
                    filePath = attachFile
                elif type(attachFile) == types.TupleType and len(attachFile) == 2:
                    filePath,fileName = attachFile
                else:
                    raise "Attachments Error: must be pathname string or path,filename tuple"
                message.attach( FICHIER(attachFile) )

        #try:
        server = smtplib.SMTP(self.SMTPServer)
        server.sendmail(self.fromAddress, recipientList, message.as_string())
        #finally:
        server.quit()

    def save(self, fileName):
        """
        Saves the message to a file. Including attachements and pre/appended files.
        """
        file = open(fileName, 'w')
        file.write(str(self))
        file.close()

if __name__ == '__main__':
    # Exemple d'utilisation de la classe mxmMail
    serveur = 'smtp.wanadoo.fr' # votre serveur SMTP ici
    expediteur = 'bussiere@gmail.com' # Votre adresse email
    destinataire = 'sandrine.imp@wanadoo.fr' # L'adresse de votre destinataire
    sujet = u"Un message du président de la république"
    message = u'<html><body><a href="http://www.bussieresama.net">bussiere</a></body></html>'
    #myMsg = mxmMail(NomExpéditeur, AdresseExpediteur, Sujet, Texte, serveurSMTP)
    myMsg = mxmMail("Jacques Chirac", expediteur, sujet,message,serveur)
    # Ajoute un destinataire : myMsg.recipientAppend(Nom, Adresse)
    myMsg.recipientAppend('Bussiere', destinataire)
    #myMsg.prependFile('D:/Programmation/MailSend/test.txt')
    #myMsg.appendFile('C:/root/desktop/sig.txt')
    myMsg.attachmentAppend('D:/Programmation/MailSend/test.txt')
    #myMsg.setRecipients([{'toName':'fghdfg','toAddress':'fghdfg@slkdhf.com'}, {'toName':'xcvxcv','toAddress':'xcvxcv@cvxv.dk'}])
    myMsg.send()
# vim:ts=4