import cherrypy
class roote:
    def __init__(self):
        pass
    nom = ""
    passwd = ""
    def doLogin(self, username=None, password=None): 
        self.nom = username
        self.passwd = password
        return self.page()
    def index(self,username=None,password=None):
        return self.page()
    
    
    index.exposed = True
    doLogin.exposed = True 
 
    
        
    def page(self):
        h1 = header_begin()
        h2 = header_end()
        page = """
        <form action="doLogin" method="post"> 
        <p>Username</p> 
              <input type="text" name="username"    size="15" maxlength="40"/> 
        <p>Password</p> 
        <input type="password" name="password" value=""  
                   size="10" maxlength="40"/> 
        <p><input type="submit" value="Login"/></p> 
        <p><input type="reset" value="Clear"/></p> 
    </form> 
        
        """
        page = "%s %s %s %s %s" %(h1.printh(),page,self.nom,self.passwd,h2.printh())
        return page
