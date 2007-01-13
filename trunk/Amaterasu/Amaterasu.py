import os
import sys
import logging
sys.path.append('Module/')
from MailSend import mxmMail
# Allow us to run using installed `libgmail` or the one in parent directory.
try:
    import libgmail
    ## Wouldn't this the preffered way?
    ## We shouldn't raise a warning about a normal import
    ##logging.warn("Note: Using currently installed `libgmail` version.")
except ImportError:
    # Urghhh...
    sys.path.insert(1,
                    os.path.realpath(os.path.join(os.path.dirname(__file__),
                                                  os.path.pardir)))
    import libgmail
# -*- Encoding: UTF-8 -*-
from MailSend import mxmMail
serveur = '192.168.1.24' # votre serveur SMTP ici

ga = libgmail.GmailAccount("bussidgere@gmail.com", "fdfgdfgdfgfg")
ga.login()
folder = ga.getMessagesByFolder('inbox',True)

for thread in folder:
  for msg in thread:
    
    expediteur  = msg.sender
    print expediteur
    destinataire = "bussiere@gmail.com"
    sujet = msg.subject
    message = msg
    print message
    if  msg.attachments:
        for attach in msg.attachments :
            myMsg.prependFile(attach)
            myMsg.attachmentAppend(attach)
    myMsg = mxmMail("Forward", expediteur, sujet,message,serveur)
    myMsg.recipientAppend('Clients', destinataire)
    myMsg.send()
    
print "done"
