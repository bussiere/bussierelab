import serial,threading,time #importe le module serial pour communiquer avec la voie serie
serhdl = serial.Serial(0) # ouvre le com1
serhdl.open()


class T (threading.Thread) :
    def __init__(self) :
        threading.Thread.__init__(self)
        self.a = 0
    def run(self) :
        while(True):
            output = ord(serhdl.read())
            if (output  != ""):
                self.a+=1
            else :
                self.a = 0
            print "valeur lue chiffre",output 
            print "valeur lue chiffre \"modulo 43\" : ",output %43
            print "compteur",self.a
            print "valeur lue car",chr(output)
            print "\n"
        

t = T()
t.start()


   



 
 